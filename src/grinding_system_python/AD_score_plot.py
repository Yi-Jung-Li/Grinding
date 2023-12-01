#!/usr/bin/env python
# coding: utf-8



from tkinter import constants
from std_msgs.msg import Header
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import String


import sys
import copy
import rospy
import numpy as np
import time
import numpy as np
import matplotlib.pyplot as plt



# Setup ROS
rospy.init_node('Trajectory_anomaly_detection_plot')
AD_score = rospy.wait_for_message('/AD_score', Float64MultiArray)
AD_score = AD_score.data
# sub2 = rospy.Subscriber('/motion_type',String,callback)


# EWMA
L = 2.6
Lambda = 0.05
test_mse_mean = 0.0034
test_mse_std = 0.009
UCL_ss = 0.193235*1.5
Z_0 = test_mse_mean
Z = np.ones(20)*test_mse_mean
mse_all = []

plt.close()
threshold_value = 0.02314
mse = np.zeros((20))
threshold = np.ones((20))*threshold_value
threshold_EWMA = np.ones((20))*UCL_ss
x = np.arange(20)
plt.ion()
fig = plt.figure(figsize=(8,4) ,constrained_layout = True)
ax = fig.add_subplot(121)

ax.set_ylim(0.0,0.05)
ax.set_xlabel('Time-step')
ax.set_ylabel('Anomaly score(MSE)')
ax.set_title("Anomaly Detection")
line1, = ax.plot(x, mse, 'b-', label='A.D. score')
line2, = ax.plot(x, threshold, 'r-', label='Threshold')
ax.legend(loc="upper right")
ax2 = fig.add_subplot(122)
ax2.set_xlabel('Time-step')
ax2.set_ylabel('Anomaly score(Z)')
ax2.set_title("EWMA Anomaly Detection")
ax2.set_ylim(0.0,0.6)
line3, = ax2.plot(x, Z, 'b-', label='A.D. score')
line4, = ax2.plot(x, threshold_EWMA, 'r-', label='Threshold')
ax2.legend(loc="upper right")

global state
state  = None

def callback(data):
    global state
    print(data) 
    state = data.data


try:
    while 1:
        sub2 = rospy.Subscriber('/motion_type',String,callback)
        print(state)
        if state == 'line':
            AD_score = rospy.wait_for_message('/AD_score_cart', Float64MultiArray)
            ax.set_title("Anomaly Detection: Line")
        else:
            AD_score = rospy.wait_for_message('/AD_score', Float64MultiArray)
            ax.set_title("Anomaly Detection: PTP")
        AD_score = AD_score.data
        mse = AD_score[:20]
        Z = AD_score[20:]
        print(Z[-1])
        #plt.plot(mse)
        line1.set_ydata(mse)
        line3.set_ydata(Z)
        fig.canvas.draw()
        fig.canvas.flush_events()

except KeyboardInterrupt:
    plt.close()
# Setup ROS and Moveit
# rospy.init_node('Trajectory_anomaly_detection')
# pose = rospy.wait_for_message('/tool_pose', PoseStamped)
# joint_state = rospy.wait_for_message('/joint_states', JointState)
# print(pose.pose.position)
# print(joint_state.position)
# print(joint_state.velocity)
