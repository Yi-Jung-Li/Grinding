#!/usr/bin/env python
# coding: utf-8

import sys
import copy
import rospy
import numpy as np
import time
from tm_msgs.srv import robot_motion
from tm_msgs.srv import *
from math import pi

# Setup ROS and Moveit
print('wait for service')
rospy.wait_for_service('move_robot')
client_motion = rospy.ServiceProxy('move_robot', robot_motion)



pose0 = [0.3693565, -0.3805846, 0.390164, -0.05236336821833387, 0.016324064493902966, 0.567242478873669]
pose1 = [0.4742192, -0.39098220000000006-0.1, 0.3962182, 0.02242224490037115, 0.050258501140428714, 0.5673629065920567+0.5*pi]
pose2 = [0.46374950000000004, -0.3834543-0.1, 0.4009536, 0.034257322558144704, -0.12379271318545382, 0.5624323514551727+0.5*pi]
pose3 = [0.4851592, -0.3989288-0.1, 0.39379270000000005, 0.011175343200519692, 0.2243533486976111, 0.5703107676986751+0.5*pi]
goal_format = 'JPP' # "JPP" for joint_angle(rad), and "CPP" for end_effector(m)
motion_type = 'PTP' # "PTP" for plan on joint space, and "line" for planning on Cartesian space
velocity_scale = 0.05 # Set a scaling factor for optionally reducing the maximum joint velocity. Allowed values are in (0,1]

pose = [-4.000819235042528, -0.14546525427051785, -2.564468867454755, 1.115553239790798, 1.5218679322996338, 1.4271773755291035]
print('Moving to initial position')
res = client_motion(goal_format, motion_type,pose, velocity_scale, False)

goal_format = 'CPP' # "JPP" for joint_angle(rad), and "CPP" for end_effector(m)
set_constraints = True
res = client_motion(goal_format, motion_type, pose0, velocity_scale, set_constraints)
print('start moving')
print("move 1")
res = client_motion(goal_format, motion_type, pose1, velocity_scale, set_constraints)
print("move 2")
res = client_motion(goal_format, motion_type, pose2, velocity_scale, set_constraints)
print("move 3")
res = client_motion(goal_format, motion_type, pose3, velocity_scale, set_constraints)