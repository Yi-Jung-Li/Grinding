#!/usr/bin/env python
#from home.biorola.cps_ros.src.trajectory_function import plan_to_yaml, yaml_to_plan
import os
import sys
import copy

from numpy.core.defchararray import index
import rospy
import moveit_commander
import moveit_msgs.msg
import tf
import geometry_msgs.msg
import trajectory_msgs.msg
import moveit_msgs.msg
import numpy as np
import trajectory_function
from std_msgs.msg import Int32
from math import pi
# Utils
import aoi_moveit_utils
# light & camera library
from std_msgs.msg import String
#from light.srv import SetLight
#from flir_camera.srv import SetCamera
from yaml.loader import SafeLoader
import time
# # constraint library
# from moveit_msgs.msg import RobotState, Constraints, OrientationConstraint, JointConstraint
# from geometry_msgs.msg import Quaternion
# subprocess for capture video
import subprocess
import glob
from rosparam import upload_params
from yaml import dump, load, loader
import yaml
from tqdm import tqdm
import trajectory_function
import argparse
from time import sleep

def move_to_origin(group):
    group.set_max_velocity_scaling_factor(0.1)
    joint_goal = group.get_current_joint_values()
    joint_goal[0] = 0
    joint_goal[1] = 0
    joint_goal[2] = 0
    joint_goal[3] = 0
    joint_goal[4] = 0
    joint_goal[5] = 0

    group.go(joint_goal, wait=True)

def move_to_origin_point(group):
    group.set_max_velocity_scaling_factor(0.1)
    joint_goal = group.get_current_joint_values()
    joint_goal[0] = 0.562647974292831
    joint_goal[1] = -0.41026778896240873
    joint_goal[2] = -1.791002331531134
    joint_goal[3] = 0.6311767683578862
    joint_goal[4] = 1.5708613079254945
    joint_goal[5] = -2.1340667484135065

    group.go(joint_goal, wait=True)

def move_to_initial_point(group):
    group.set_max_velocity_scaling_factor(0.1)
    roll = 0
    pitch = 0
    yaw = 0
    path_cords = [-0.5,-0.5,0.5]
    quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position.x = float(path_cords[0])#sys.argv[1])
    pose_goal.position.y = float(path_cords[1])#sys.argv[2])
    pose_goal.position.z = float(path_cords[2]) #0.271#0.242
    pose_goal.orientation.x = quaternion[0]
    pose_goal.orientation.y = quaternion[1]
    pose_goal.orientation.z = quaternion[2]
    pose_goal.orientation.w = quaternion[3]
    group.set_pose_target(pose_goal)
    plan = group.plan()
    group.execute(plan)



parser = argparse.ArgumentParser()
parser.add_argument("-a", "--arm", help="disable robot arm", action="store_false", default=True)
parser.add_argument("-c", "--camera", help="disable camera capture", action="store_false", default=True)
parser.add_argument("-l", "--light", help="disable light", action="store_false", default=True)
parser.add_argument("-n", "--number", type=int, help="number of plan", default=10)
parser.add_argument("-v", "--velocity", type=str, help="max velocity", default="normal")
args = parser.parse_args()
print(args)
if not args.arm:
    print("disable arm")
if not args.camera:
    print("disable camera")
if not args.light:
    print("disable light")

############### start init ###################
if args.arm:
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_group_python_interface_tutorial',anonymous=True)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    group = moveit_commander.MoveGroupCommander(group_name)
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)
    motion_state_pub = rospy.Publisher('/motion_state',Int32,queue_size=10)
    
    rospy.sleep(2)
    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "base"
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.z = -0.355 # slightly above the end effector
    box_name = "box"
    scene.add_box(box_name, box_pose, size=(3.0, 3.0, 0.7))

    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "base"
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.z = 0.05 # slightly above the end effector
    box_pose.pose.position.x = -0.6
    box_name = "box3"
    scene.add_box(box_name, box_pose, size=(0.1, 1.0, 0.1))

    print("ref frame: ", group.get_pose_reference_frame())
    # group.set_pose_reference_frame('/workcell_turntable')
    # speed scaling factor
    # group.set_max_velocity_scaling_factor(0.001)
    print("new ref frame: ", group.get_pose_reference_frame())


roll = 0
pitch = 0
yaw = 0
quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
# Generate random goal
 
# Number of goal  
num = args.number
# x,y,z position limits
Mean = [0.5,0.5,0.6] 
Range = [0.2,0.2,0.1]
path_cords = np.random.rand(num,3)
path_cords = (path_cords-0.5)*2
path_cords = path_cords*Range+Mean
#path_cords[:,0:2] = np.sign(np.random.randn(num,2))*path_cords[:,0:2]

# for x is always positive
path_cords[:,1] = np.sign(np.random.randn(num))*path_cords[:,1]
path_cords = np.ndarray.tolist(path_cords)

plans = []

# Set plan time threshold
time_threshold = 1 # planning time must larger than threshold (s)


# Move to origin position
print("Move to origin position")
# move_to_origin(group)
move_to_origin_point(group)
move_to_initial_point(group)

#Set max velocity for robot(Fast,normal.slow)
if args.velocity == 'fast':
   velocity_scaling_factor = 0.2
elif args.velocity == 'slow':
    velocity_scaling_factor = 0.03
else:
    velocity_scaling_factor = 0.1
    
print("Start planning ...")
bar = tqdm(total = len(path_cords),position = 0, leave=True)
cord_idx = 0
cart_plan_iter = 0
group.set_max_velocity_scaling_factor(1)
while 1:

    # path_cords = np.random.rand(3)
    # path_cords = (path_cords-0.5)*2
    # path_cords = path_cords*Range+Mean
    # path_cords[1] = np.sign(np.random.randn(1))*path_cords[1]
    # path_cords = np.ndarray.tolist(path_cords)

    path_cords = np.random.rand(3)
    path_cords = (path_cords-0.5)*2
    path_cords = path_cords*Range+Mean
    path_cords[:2] = np.sign(np.random.randn(2))*path_cords[:2]
    path_cords = np.ndarray.tolist(path_cords)

    bar.set_description('Generating | {}/{}'.format(cord_idx,num))
    # if cord_idx == (num-1):
    #     path_cords = [0.5,0.5,0.5]
    waypoints = []
    wpose = group.get_current_pose().pose
    wpose.position.x = float(path_cords[0])
    wpose.position.y = float(path_cords[1])  # First move up (z)
    wpose.position.z = float(path_cords[2])  # and sideways (y)
    # wpose.orientation.x = quaternion[0]
    # wpose.orientation.y = quaternion[1]
    # wpose.orientation.z = quaternion[2]
    # wpose.orientation.w = quaternion[3]
    waypoints.append(copy.deepcopy(wpose))

    group.set_goal_tolerance(0.005)


    #print (group.get_planning_time())
    group.set_planning_time(1)
    group.set_num_planning_attempts(10)
    # move arm

    (plan, fraction) = group.compute_cartesian_path(
                                    waypoints,   # waypoints to follow
                                    0.01,        # eef_step
                                    0.0)  
    # plan = group.retime_trajectory(group.get_current_state(), plan, 0.2)
    if len(plan.joint_trajectory.points)==0:
        print('plan fail')
        continue
    # plan = trajectory_function.setAvgCartesianSpeed(group, plan, 0.05)
    s = plan.joint_trajectory.points[-1].time_from_start.secs
    ns = plan.joint_trajectory.points[-1].time_from_start.nsecs
    plan_time = s+ns*10**(-9)
    p = yaml.load(str(plan), Loader=SafeLoader)
    plan_l = len(p['joint_trajectory']['points'])
    speed = 0.1 # m/s
    if plan_l > 5 and plan_time > time_threshold and plan_time < 30:
        plan = trajectory_function.setAvgCartesianSpeed(group, plan, speed)
        if plan ==0:
            cart_plan_iter += 1
            if cart_plan_iter > 30 and cord_idx >0:
                print('reset the pos')
                cart_plan_iter = 0
                plans.pop()
                cord_idx -= 1
                bar.n = len(plans)
                bar.refresh() 
                sleep(2)
                new_pos = group.get_current_state()
                new_pos_joint_value = plans[-1].joint_trajectory.points[-1].positions
                new_pos.joint_state.position = new_pos_joint_value
                group.set_start_state(new_pos)
            continue
        else:    
            cart_plan_iter = 0
        plans.append(plan)
        #group.clear_path_constraints()
        bar.update()

        #  Set start state as pose goal
        new_pos = group.get_current_state()
        new_pos_joint_value = plan.joint_trajectory.points[-1].positions
        new_pos.joint_state.position = new_pos_joint_value
        group.set_start_state(new_pos)
        cord_idx += 1
    if cord_idx >= num:
        break



print('save plan as yaml file ...')
if args.velocity == 'fast':
    save_path = 'motion_plan/continuous_cartesian_plan_fast.yaml'
elif args.velocity == 'slow':
    save_path = 'motion_plan/continuous_cartesian_plan_slow.yaml'
else:
    save_path = 'motion_plan/continuous_cartesian_plan.yaml'
trajectory_function.plan_to_yaml(plans,save_path)


if args.arm:
    moveit_commander.roscpp_shutdown()
