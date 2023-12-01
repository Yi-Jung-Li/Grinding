#!/usr/bin/env python
#from home.biorola.cps_ros.src.trajectory_function import plan_to_yaml, yaml_to_plan
import os
import sys
import copy
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

def move_to_origin(group):
    joint_goal = group.get_current_joint_values()
    joint_goal[0] = 0
    joint_goal[1] = 0
    joint_goal[2] = 0
    joint_goal[3] = 0
    joint_goal[4] = 0
    joint_goal[5] = 0

    group.go(joint_goal, wait=True)


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--arm", help="disable robot arm", action="store_false", default=True)
parser.add_argument("-c", "--camera", help="disable camera capture", action="store_false", default=True)
parser.add_argument("-l", "--light", help="disable light", action="store_false", default=True)
parser.add_argument("-f", "--file", type=str, help="yaml file name", default="plan")
#parser.add_argument("-o", "--object", type=str, help="objects name", default="none")
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

    print("ref frame: ", group.get_pose_reference_frame())
    # group.set_pose_reference_frame('/workcell_turntable')
    # speed scaling factor
    # group.set_max_velocity_scaling_factor(0.001)
    print("new ref frame: ", group.get_pose_reference_frame())



motion_state_pub.publish(0)
rospy.sleep(0.4)
move_to_origin(group)
#aoi_moveit_utils.go_origin(group)

load_path = str(args.file)+'.yaml'
with open(load_path, 'r') as file_open:
        loaded_plan = list(yaml.load_all(file_open, Loader=SafeLoader))
bar = tqdm(total = len(loaded_plan),position = 0, leave=True)
for idx,plan in enumerate(loaded_plan):
    bar.set_description('Excuting | {}/{}'.format(idx+1,len(loaded_plan)))
    #print('index = {}'.format(idx))
    motion_state_pub.publish(1)
    rospy.sleep(0.2)
    plan3 = trajectory_function.yaml_to_plan(plan)
    group.execute(plan3)
    motion_state_pub.publish(0)
    rospy.sleep(0.2)
    move_to_origin(group)
    #aoi_moveit_utils.go_origin(group)
    bar.update()
motion_state_pub.publish(2)
if args.arm:
    moveit_commander.roscpp_shutdown()
