#!/usr/bin/env python

import trajectory_msgs.msg
import moveit_msgs.msg
import numpy as np
from yaml.loader import SafeLoader
import time
import yaml
import rospy

from moveit_msgs.srv import GetPositionFK
from moveit_msgs.srv import GetPositionFKRequest
from moveit_msgs.srv import GetPositionFKResponse
from std_msgs.msg import Header


# tranfer moveit trajectory plan objection into yaml file

def plan_to_yaml(plan,save_path):
    plans = []
    for p in plan: 
        y = yaml.load(str(p), Loader=SafeLoader)
        plans.append(y)
    with open(save_path, 'w') as file_save:
        yaml.dump_all(plans, file_save, default_flow_style=False) 
    

# tranfer yaml file info into moveit trajectory objection 

# http://docs.ros.org/en/melodic/api/moveit_msgs/html/msg/RobotTrajectory.html
# http://docs.ros.org/en/melodic/api/trajectory_msgs/html/msg/JointTrajectory.html
def yaml_to_plan(yaml_f):
    plan = moveit_msgs.msg.RobotTrajectory()
    load_tra = yaml_f['joint_trajectory']
    plan.joint_trajectory.header.frame_id = load_tra['header']['frame_id']
    plan.joint_trajectory.joint_names = load_tra['joint_names']
    points = []
    for points_info in load_tra['points']:
        p = trajectory_msgs.msg.JointTrajectoryPoint()
        p.positions = points_info['positions']
        p.velocities = points_info['velocities']
        p.accelerations = points_info['accelerations']
        p.time_from_start.secs = points_info['time_from_start']['secs']
        p.time_from_start.nsecs = points_info['time_from_start']['nsecs']
        points.append(p)
    plan.joint_trajectory.points = points

    return plan

def compute_fk(group, fk_link, frame_id, joint_pos):
    client_fk = rospy.ServiceProxy("/compute_fk", GetPositionFK)
    robot_state = group.get_current_state()
    robot_state.joint_state.position = joint_pos
    link_name = fk_link
    header = Header()
    header.frame_id = frame_id
    req = GetPositionFKRequest()
    req.header = header
    req.robot_state = robot_state
    req.fk_link_names = [link_name]
    res = client_fk(req)
    return res


def setAvgCartesianSpeed(group, plan, speed):
    num_waypoints = len(plan.joint_trajectory.points)
    time = []
    time.append(0)
    max_vel = 2
    print('num:',num_waypoints)
    for i in range(num_waypoints-1):
        curr_waypoint = plan.joint_trajectory.points[i]
        next_waypoint = plan.joint_trajectory.points[i+1]

        curr_pos = curr_waypoint.positions
        next_pos = next_waypoint.positions

        # Get end effector
        fk_link = "link_6"
        frame_id = 'base'
        
        curr_eff = compute_fk(group, fk_link, frame_id, curr_pos)
        next_eff = compute_fk(group, fk_link, frame_id, next_pos)

        curr_eff_pos = [curr_eff.pose_stamped[0].pose.position.x, curr_eff.pose_stamped[0].pose.position.y, curr_eff.pose_stamped[0].pose.position.z]
        next_eff_pos = [next_eff.pose_stamped[0].pose.position.x, next_eff.pose_stamped[0].pose.position.y, next_eff.pose_stamped[0].pose.position.z]

        curr_eff_pos = np.array(curr_eff_pos)
        next_eff_pos = np.array(next_eff_pos)

        # Cal. euclidean_distance
        euclidean_distance = np.sqrt(np.sum((next_eff_pos-curr_eff_pos)**2))

        if euclidean_distance > 0.2:
            print('distance is too large')
            return 0
        # print(euclidean_distance)

        # Cal. new timestamp
        s = curr_waypoint.time_from_start.secs
        ns = curr_waypoint.time_from_start.nsecs
        plan_time = s+ns*10**(-9)
        
        # Reduce vel. for last 4 point
        if i < 3:
            num = i+1
            low_speed = np.sqrt((float(num)/4))*speed
            new_timestamp = plan_time + euclidean_distance/low_speed
        # Reduce vel. for last 4 point
        elif i > num_waypoints-5:
            num = i-(num_waypoints-5)
            low_speed = np.sqrt(1-(float(num)/4))*speed
            new_timestamp = plan_time + euclidean_distance/low_speed
        else:
            new_timestamp = plan_time + euclidean_distance/speed


        s = next_waypoint.time_from_start.secs
        ns = next_waypoint.time_from_start.nsecs
        plan_time = s+ns*10**(-9)
        old_timestamp = plan_time
        # print('new',new_timestamp)
        # print('old',old_timestamp)
        if new_timestamp>old_timestamp/2:
            time.append(new_timestamp)
            s = float(int(new_timestamp))
            ns = (new_timestamp-s)*10**(9)
            plan.joint_trajectory.points[i+1].time_from_start.secs = s
            plan.joint_trajectory.points[i+1].time_from_start.nsecs = ns
        else:
            print('too fast!!')
            return 0


    for i in range(num_waypoints):
        curr_waypoint = plan.joint_trajectory.points[i]
        if i>0:
            prev_waypoint = plan.joint_trajectory.points[i-1]
        if i<num_waypoints-1:
            next_waypoint = plan.joint_trajectory.points[i+1]
        if(i==0):
            dt1 = time[i+1]-time[i]
            dt2 = dt1
        elif(i<num_waypoints-1):
            dt1 = time[i]-time[i-1]
            dt2 = time[i+1]-time[i]
        else:
            dt1 = time[i]-time[i-1]
            dt2 = dt1

        
        if i == 0:    
            p1 = np.array(next_waypoint.positions)
            p2 = np.array(curr_waypoint.positions)
            p3 = p1
        elif(i<num_waypoints-1):
            p1 = np.array(prev_waypoint.positions)
            p2 = np.array(curr_waypoint.positions)
            p3 = np.array(next_waypoint.positions)
        else:
            p1 = np.array(prev_waypoint.positions)
            p2 = np.array(curr_waypoint.positions)
            p3 = p1

        if(dt1 == 0 or dt2 == 0):
            v1 = v2 = a = 0
        else:
            v1 = (p2-p1)/dt1
            v2 = (p3-p2)/dt2
            a = 2*(v2-v1)/(dt1+dt2)
        V = (v1+v2)/2
        if np.max(np.abs(V)) > max_vel:
            print('V is ', V)
            return 0
        plan.joint_trajectory.points[i].velocities = V.tolist()
        plan.joint_trajectory.points[i].accelerations = a.tolist()

    return plan