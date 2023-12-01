#!/usr/bin/env python
# coding: utf-8



from std_msgs.msg import Header
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import MultiArrayDimension
from std_msgs.msg import String
from std_msgs.msg import Float64


import sys
import copy
import rospy
import numpy as np
import time
import numpy as np
import matplotlib.pyplot as plt

rospy.init_node('plot_AD_score_of_image')
pub_AD_score = rospy.Publisher('/Image_AD_score_plot', Float64, queue_size = 100)

plt.ion()
fig, ax = plt.subplots()
# this example doesn't work because array only contains zeroes
# array = np.zeros(shape=(IMAGE_SIZE, IMAGE_SIZE), dtype=np.uint8)
# axim1 = ax1.imshow(array)
array = np.zeros(shape=(256, 256,3), dtype=np.uint8)
axim2 = ax.imshow(array)
# alternatively this process can be automated from the data
# array[0, 0,0] = 99 # this value allow imshow to initialise it's color scale
# axim3 = ax3.imshow(array)
del array


fig, ax = plt.subplots()
array = np.zeros(shape=(256, 256,3), dtype=np.uint8)
axim = ax.imshow(array)

try:
    while 1:
        # AD_score = rospy.wait_for_message('/AD_score_cart', Float64)
        # AD_score = AD_score.data
        file_path = 'image_AD/data/Img.jpg'
        test_img = plt.imread(file_path, format=None)
        axim.set_data(test_img)
        # fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.5)

except KeyboardInterrupt:
    plt.close()
