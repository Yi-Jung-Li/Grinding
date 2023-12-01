#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import tf
import geometry_msgs.msg
import numpy as np

from std_msgs.msg import Int32
from math import pi
# Utils
import aoi_moveit_utils
# light & camera library
from std_msgs.msg import String
#from light.srv import SetLight
#from flir_camera.srv import SetCamera
import time
# # constraint library
# from moveit_msgs.msg import RobotState, Constraints, OrientationConstraint, JointConstraint
# from geometry_msgs.msg import Quaternion
# subprocess for capture video
import subprocess
import glob
from rosparam import upload_params
from yaml import load
# mqtt
#import paho.mqtt.client as mqtt
#import paho.mqtt.subscribe as subscribe
#import ssl
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--arm", help="disable robot arm", action="store_false", default=True)
parser.add_argument("-c", "--camera", help="disable camera capture", action="store_false", default=True)
parser.add_argument("-l", "--light", help="disable light", action="store_false", default=True)
#parser.add_argument("-n", "--number", type=int, help="loop times", default=1)
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


    print("ref frame: ", group.get_pose_reference_frame())
    group.set_pose_reference_frame('/workcell_turntable')
    # speed scaling factor
    # group.set_max_velocity_scaling_factor(0.001)
    print("new ref frame: ", group.get_pose_reference_frame())


import sensor_msgs.msg
from sensor_msgs.msg import JointState
from std_msgs.msg import Int32

JointStates = []
Index = []
global state
state  = None

def callback2(data):
    global state 
    state = data.data



idx = 0
# wait for robot arm start move
while state is None:
    try:
        sub2 = rospy.Subscriber('/motion_state',Int32,callback2)
    except:
        pass
    
while state != 2:
    while state == 0:
        sub2 = rospy.Subscriber('/motion_state',Int32,callback2)
        rospy.loginfo(state)
        rospy.sleep(0.05)
    
    while state == 1:
        JointData = group.get_current_joint_values()
        End_effect = group.get_current_pose().pose
        T = time.time()
        end_effect = [End_effect.position.x,End_effect.position.y,End_effect.position.z]
        data = JointData+end_effect+[T]+[idx] # JointData(6 joints) + end_effect(x,y,z) + index
        #print('joint=',data)
        #print('End_effect=',end_effect)
        JointStates.append(data)
        Index.append(idx) 
        rospy.sleep(0.01)
        sub2 = rospy.Subscriber('/motion_state',Int32,callback2)
        #if state != None:
        #rospy.loginfo(state)
        #rospy.loginfo(JointData)
    idx += 1
#rospy.loginfo(JointStates)
output = np.array(JointStates)
np.savetxt("output.csv",output,delimiter=",")




if args.arm:
    moveit_commander.roscpp_shutdown()
