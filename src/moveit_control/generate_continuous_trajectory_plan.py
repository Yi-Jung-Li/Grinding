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
from yaml.loader import SafeLoader
import time
import subprocess
import glob
from rosparam import upload_params
from yaml import dump, load, loader
import yaml
from tqdm import tqdm
import argparse

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
    print("new ref frame: ", group.get_pose_reference_frame())


roll = 0
pitch = 0
yaw = 0
quaternion_1 = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
roll = pi/2
pitch = 0
yaw = 0
quaternion_2 = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
roll = 0
pitch = pi/2
yaw = 0
quaternion_3 = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
Quaternion = [quaternion_1, quaternion_2, quaternion_3]
# Generate random goal
quaternion = quaternion_3
# Number of goal  
num = args.number
# x,y,z position limits
Mean = [0.5,0.5,0.6] 
Range = [0.2,0.2,0.1]
# path_cords = np.random.rand(num,3)
# path_cords = (path_cords-0.5)*2
# path_cords = path_cords*Range+Mean
# #path_cords[:,0:2] = np.sign(np.random.randn(num,2))*path_cords[:,0:2]

# # for x is always positive
# path_cords[:,1] = np.sign(np.random.randn(num))*path_cords[:,1]
# path_cords = np.ndarray.tolist(path_cords)

plans = []

# Set plan time threshold
time_threshold = 1 # planning time must larger than threshold (s)


# Move to origin position
print("Move to origin position")
move_to_origin(group)

#Set max velocity for robot(Fast,normal.slow)
if args.velocity == 'fast':
    group.set_max_velocity_scaling_factor(0.2)
elif args.velocity == 'slow':
    group.set_max_velocity_scaling_factor(0.03)
else:
    group.set_max_velocity_scaling_factor(0.1)

    
print("Start planning ...")
bar = tqdm(total = num, position = 0, leave=True)
cord_idx = 0
Pose_all = []
while 1:
    # Generate random pose goal
    path_cords = np.random.rand(3)
    path_cords = (path_cords-0.5)*2
    path_cords = path_cords*Range+Mean
    # Randomly transfer to negative
    # path_cords[1] = np.sign(np.random.randn(1))*path_cords[1]
    path_cords[:2] = np.sign(np.random.randn(2))*path_cords[:2]
    path_cords = np.ndarray.tolist(path_cords)
    quaternion = Quaternion[np.random.randint(3)]
    bar.set_description('Generating | {}/{}'.format(cord_idx,num))

    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position.x = float(path_cords[0])#sys.argv[1])
    pose_goal.position.y = float(path_cords[1])#sys.argv[2])
    pose_goal.position.z = float(path_cords[2]) #0.271#0.242
    pose_goal.orientation.x = quaternion[0]
    pose_goal.orientation.y = quaternion[1]
    pose_goal.orientation.z = quaternion[2]
    pose_goal.orientation.w = quaternion[3]
    group.set_pose_target(pose_goal)

    group.set_goal_tolerance(0.0001)

    pose = path_cords+list(quaternion)
    # print (group.get_planning_time())
    group.set_planning_time(1)
    group.set_num_planning_attempts(10)
    # move arm

    motion_state_pub.publish(1)
    # Generate motion plan
    plan1 = group.plan()
    # Calculate planning time

    if len(plan1.joint_trajectory.points)==0:
        print('plan fail')
        continue

    s = plan1.joint_trajectory.points[-1].time_from_start.secs
    ns = plan1.joint_trajectory.points[-1].time_from_start.nsecs
    plan_time = s+ns*10**(-9)

    # Delete short motion plan 
    if plan_time > time_threshold:
        plans.append(plan1)
        Pose_all.append(pose)
        bar.update()

        #  Reset the start state as pose goal
        new_pos = group.get_current_state()
        new_pos_joint_value = plan1.joint_trajectory.points[-1].positions
        new_pos.joint_state.position = new_pos_joint_value
        group.set_start_state(new_pos)
        cord_idx += 1
    if cord_idx >= num:
        break


print('save plan as yaml file ...')
if args.velocity == 'fast':
    save_path = 'motion_plan/continuous_plan_fast.yaml'
elif args.velocity == 'slow':
    save_path = 'motion_plan/continuous_plan_slow.yaml'
else:
    save_path = 'motion_plan/continuous_plan.yaml'
trajectory_function.plan_to_yaml(plans,save_path)

np.savetxt('motion_plan/pose.csv',np.array(Pose_all))
if args.arm:
    moveit_commander.roscpp_shutdown()
