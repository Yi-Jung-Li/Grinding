#!/usr/bin/env python
# coding: utf-8

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import numpy as np
import time
from tm_msgs.srv import robot_state
from tm_msgs.srv import *

def output_robot_info(req):
    #robot_stateResponse.joint_state = group.get_current_joint_values()
    #robot_stateResponse.joint_state = [1.0 , 3.0]
    End_effect = group.get_current_pose().pose
    end_effect =  [End_effect.position.x,End_effect.position.y,End_effect.position.z]
    print('state:',req.state)
    return robot_stateResponse(group.get_current_joint_values(),end_effect)

# Setup ROS and Moveit
moveit_commander.roscpp_initialize(sys.argv)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "manipulator"
group = moveit_commander.MoveGroupCommander(group_name)
rospy.init_node('robot_state',anonymous=True)
s = rospy.Service('get_robot_state', robot_state, output_robot_info)
print('Ready for request !!')
rospy.spin()

