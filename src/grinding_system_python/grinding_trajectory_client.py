#!/usr/bin/env python
# coding: utf-8

import sys
import copy
import rospy
import numpy as np
import time
from tm_msgs.srv import SendScript
from tm_msgs.srv import *

# Setup ROS and Moveit
print('wait for service')
rospy.wait_for_service("tm_driver/send_script")
client_motion = rospy.ServiceProxy("tm_driver/send_script", SendScript)
ids = "demo"
cmd = "PTP(\"CPP\",309,558,300,-150,0,90,40,200,0,false)"
res = client_motion(ids,cmd)
f = open('A30.txt')
speed = 20
for line in f.readlines():
    cmd = line.split()
    if cmd[0] == 'movlspdque':
        if cmd[2] == '1':
            speed = 15
        else:
            speed = 80
    elif cmd[0] == 'movl':
        cmd_mov = f"Line(\"CPP\",{cmd[2]},{float(cmd[3])+60},{float(cmd[4])-30},{cmd[5]},{cmd[6]},{cmd[7]},{speed},200,0,false)"
        res = client_motion(ids,cmd_mov)
        print(cmd_mov)
#res = client_motion(ids,cmd_mov)
#cmd = "PTP(\"CPP\",309,558,300,-150,0,90,40,200,0,false)"
#print('start moving')
#res = client_motion(ids,cmd)




