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
# mqtt
#import paho.mqtt.client as mqtt
#import paho.mqtt.subscribe as subscribe
#import ssl
import argparse

def move_to_origin(group):
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
    box_pose.pose.position.z = -0.35 # slightly above the end effector
    box_name = "box"
    scene.add_box(box_name, box_pose, size=(2.0, 2.0, 0.7))

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
Mean = [0.3,0.3,0.6] 
Range = [0.2,0.2,0.1]
path_cords = np.random.rand(num,3)
path_cords = (path_cords-0.5)*2
path_cords = path_cords*Range+Mean
#path_cords[:,0:2] = np.sign(np.random.randn(num,2))*path_cords[:,0:2]

# for x is always positive
path_cords[:,1] = np.sign(np.random.randn(num))*path_cords[:,1]
path_cords = np.ndarray.tolist(path_cords)

plans = []

#Set max velocity for robot(Fast,normal.slow)
if args.velocity == 'fast':
    group.set_max_velocity_scaling_factor(1)
elif args.velocity == 'slow':
    group.set_max_velocity_scaling_factor(0.03)
else:
    group.set_max_velocity_scaling_factor(0.1)
#group.set_max_velocity_scaling_factor(1)
#group.set_max_velocity_scaling_factor(0.1)
#group.set_max_velocity_scaling_factor(0.03)
#group.set_max_velocity_scaling_factor(0.01)
move_to_origin(group)

#aoi_moveit_utils.go_origin(group)
bar = tqdm(total = len(path_cords),position = 0, leave=True)
for cord_idx, cord in enumerate(path_cords):
    bar.set_description('Generating | {}/{}'.format(cord_idx,len(path_cords)))
    #print('index = {}'.format(cord_idx))
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position.x = float(cord[0])#sys.argv[1])
    pose_goal.position.y = float(cord[1])#sys.argv[2])
    pose_goal.position.z = float(cord[2]) #0.271#0.242
    pose_goal.orientation.x = quaternion[0]
    pose_goal.orientation.y = quaternion[1]
    pose_goal.orientation.z = quaternion[2]
    pose_goal.orientation.w = quaternion[3]
    group.set_pose_target(pose_goal)
    # setup constraint
    # constraint = aoi_moveit_utils.upright_constraint()
    # constraint = tilt_constraint() ## unstable
    #aoi_moveit_utils.enable_constraint(group, constraint)
    #rospy.loginfo("Known path constraints:\n{}".format(group.get_path_constraints()))
    # show goal tolerance
    #print (group.get_goal_joint_tolerance())
    #print (group.get_goal_orientation_tolerance())
    #print (group.get_goal_position_tolerance())
    #print (group.get_goal_tolerance())
    # set goal tolerance
    group.set_goal_tolerance(0.005)

    # show & set planning time
    #print (group.get_planning_time())
    group.set_planning_time(1)
    group.set_num_planning_attempts(10)
    # move arm
    group.set_start_state_to_current_state()
    motion_state_pub.publish(1)
    plan1 = group.plan()
    plans.append(plan1)
    #group.clear_path_constraints()
    bar.update()
    #print ('done point %d' % cord_idx)
    # video capture
    # if cord_idx == 0:
    #     subprocess.Popen("pwd")
    #     subprocess.Popen(['python', 'SaveToAvi.py'])
    # light # capture images
    #light_capture(cord_idx)

print('save plan as yaml file...')
if args.velocity == 'fast':
    save_path = 'plan_fast.yaml'
elif args.velocity == 'slow':
    save_path = 'plan_slow.yaml'
else:
    save_path = 'plan.yaml'
trajectory_function.plan_to_yaml(plans,save_path)


if args.arm:
    moveit_commander.roscpp_shutdown()
