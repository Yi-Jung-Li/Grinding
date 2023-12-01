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
Mean = [0.4,0.4,0.6] 
Range = [0.2,0.2,0.1]
path_cords = np.random.rand(num,3)
path_cords = (path_cords-0.5)*2
path_cords = path_cords*Range+Mean
path_cords[:,0:2] = np.sign(np.random.randn(num,2))*path_cords[:,0:2]
path_cords = np.ndarray.tolist(path_cords)

plans = []

#Set max velocity for robot(Fast,normal.slow)
if args.velocity == 'fast':
   velocity_scaling_factor = 0.2
elif args.velocity == 'slow':
    velocity_scaling_factor = 0.03
else:
    velocity_scaling_factor = 0.1

move_to_origin(group)
#waypoints = []
#aoi_moveit_utils.go_origin(group)
bar = tqdm(total = num,position = 0, leave=True)
cord_idx = 0
while 1:
    bar.set_description('Generating | {}/{}'.format(cord_idx+1,num))
    # set goal tolerance
    group.set_goal_tolerance(0.005)

    #print (group.get_planning_time())
    group.set_planning_time(1)
    group.set_num_planning_attempts(10)
    # move arm
    group.set_start_state_to_current_state()
    waypoints = []

    path_cords = np.random.rand(3)
    path_cords = (path_cords-0.5)*2
    path_cords = path_cords*Range+Mean
    path_cords[0:2] = np.sign(np.random.randn(2))*path_cords[0:2]
    path_cords = np.ndarray.tolist(path_cords)

    wpose = group.get_current_pose().pose
    wpose.position.x = float(path_cords[0])
    wpose.position.y = float(path_cords[1])  # First move up (z)
    wpose.position.z = float(path_cords[2])  # and sideways (y)
    waypoints.append(copy.deepcopy(wpose))

    # We want the Cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in Cartesian
    # translation.  We will disable the jump threshold by setting it to 0.0,
    # ignoring the check for infeasible jumps in joint space, which is sufficient
    # for this tutorial.

    (plan, fraction) = group.compute_cartesian_path(
                                    waypoints,   # waypoints to follow
                                    0.01,        # eef_step
                                    0.0)  
    plan = group.retime_trajectory(group.get_current_state(), plan, velocity_scaling_factor)
    p = yaml.load(str(plan), Loader=SafeLoader)
    #print(p)
    plan_l = len(p['joint_trajectory']['points'])
    if plan_l > 5:
        cord_idx += 1
        plans.append(plan)
        bar.update()
    #group.execute(plan)
    if cord_idx >= num:
        break
    
    #move_to_origin(group)

print('save plan as yaml file...')
if args.velocity == 'fast':
    save_path = 'cart_plan_fast.yaml'
elif args.velocity == 'slow':
    save_path = 'cart_plan_slow.yaml'
else:
    save_path = 'cart_plan.yaml'
trajectory_function.plan_to_yaml(plans,save_path)


if args.arm:
    moveit_commander.roscpp_shutdown()
