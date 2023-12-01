#!/usr/bin/env python
# coding: utf-8




import sys
import copy
import rospy
import numpy as np
import time

from geometry_msgs.msg import PoseStamped
from tf.transformations import euler_from_quaternion

poses = np.array([])

# Setup ROS
rospy.init_node('Camera_pose')

state = rospy.wait_for_message('/tool_pose', PoseStamped)
ori = state.pose.orientation
ori = euler_from_quaternion([ori.x, ori.y, ori.z, ori.w])
print(state)
# print(state.pose)
# print("Rx: ", np.rad2deg(ori[0]))
# print("Rx: ", np.rad2deg(ori[1]))
# print("Rx: ", np.rad2deg(ori[2]))
count = 0

try:
    while 1:
        raw_input("next")
        state = rospy.wait_for_message('/tool_pose', PoseStamped)
        pos = state.pose.position
        ori = state.pose.orientation
        ori = euler_from_quaternion([ori.x, ori.y, ori.z, ori.w])

        temp_pose = np.array([[pos.x, pos.y, pos.z, ori[0], ori[1], ori[2]]])
        poses = temp_pose if poses.shape[0]==0 else np.append(poses, temp_pose, axis=0)
        print(count)
        print(state)
        count = count + 1
        
except KeyboardInterrupt:
    np.savetxt('toolpoints_20220719.txt', poses)
    print('good')
