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
# import aoi_moveit_utils
# light & camera library
from std_msgs.msg import String
from moveit_msgs.srv import GetPositionFK
from moveit_msgs.srv import GetPositionFKRequest
from moveit_msgs.srv import GetPositionFKResponse
from std_msgs.msg import Header
import time

from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import JointState

import subprocess
import glob
from rosparam import upload_params
from yaml import load

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--arm", help="disable robot arm", action="store_false", default=True)
parser.add_argument("-c", "--camera", help="disable camera capture", action="store_false", default=True)
parser.add_argument("-l", "--light", help="disable light", action="store_false", default=True)
parser.add_argument("-dt", "--sampling_time", type=float, default=0.1)
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
    client_fk = rospy.ServiceProxy("/compute_fk", GetPositionFK)

    print("ref frame: ", group.get_pose_reference_frame())
    group.set_pose_reference_frame('/workcell_turntable')
    # speed scaling factor
    # group.set_max_velocity_scaling_factor(0.001)
    print("new ref frame: ", group.get_pose_reference_frame())


import sensor_msgs.msg
from sensor_msgs.msg import JointState
from std_msgs.msg import Int32

sampling_time = args.sampling_time
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
last_time = time.time()
robot_state = group.get_current_state()
while state != 2:
    while state == 0:
        sub2 = rospy.Subscriber('/motion_state',Int32,callback2)
        rospy.loginfo(state)
        rospy.sleep(0.02)
        last_time = time.time()
    
    while state == 1:
        t1 = time.time()
        # joint_state = rospy.wait_for_message('/joint_states', JointState)
        # JointData = np.array(joint_state.position).tolist()

        JointData = group.get_current_joint_values()
        End_effect = group.get_current_pose().pose

        T = time.time()
        while T-last_time < sampling_time:
            rospy.sleep(0.0005)
            T = time.time()
        last_time = T
        print(T-t1)
        end_effect = [End_effect.position.x,End_effect.position.y,End_effect.position.z]
        end_effect_orientation = [End_effect.orientation.x, End_effect.orientation.y, End_effect.orientation.z, End_effect.orientation.w]
        # data = JointData+end_effect+velocity+[T]+[idx] # JointData(6 joints) + end_effect(x,y,z) + index
        data = JointData+end_effect+end_effect_orientation+[T]+[idx]
        JointStates.append(data)
        Index.append(idx) 
        # rospy.sleep(0.01)
        sub2 = rospy.Subscriber('/motion_state',Int32,callback2)
        #if state != None:
        #rospy.loginfo(state)
        #rospy.loginfo(JointData)
    idx += 1
#rospy.loginfo(JointStates)
output = np.array(JointStates)
print("Save file")
np.savetxt("output.csv",output,delimiter=",")




if args.arm:
    moveit_commander.roscpp_shutdown()
