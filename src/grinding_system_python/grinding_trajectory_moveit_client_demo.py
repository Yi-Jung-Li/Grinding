#!/usr/bin/env python
# coding: utf-8

import sys
import copy
import rospy
import numpy as np
import time
import math
import yaml
from yaml.loader import SafeLoader
from tm_msgs.srv import robot_motion
from tm_msgs.srv import *
from math import pi
from tm_msgs.msg import FeedbackState
from sensor_msgs.msg import JointState
import argparse

from std_msgs.msg import String
from std_msgs.msg import Float64
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import MultiArrayDimension

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sim", help="true for simulation", action="store_true")
parser.add_argument("-c", "--cap", help="true for capture", action="store_true")
parser.add_argument("-g", "--grind", help="true for grinding", action="store_true")
parser.add_argument("-t", "--testing", help="true for grinding", action="store_true")
args = parser.parse_args()
sim = args.sim
cap = args.cap
grind = args.grind
testing = args.testing
print(cap)
print(sim)
print(grind)
if cap:
    print("Capture!")
if sim:
    print("Simulation!")
if grind:
    print("Grinding!")
if testing:
    print("Testing")


# Setup ROS and connect service
# Waiting for service
print('wait for service')
rospy.init_node('Grind_system',anonymous=True)
rospy.wait_for_service('move_robot')
# rospy.wait_for_service('Camera_service')
rospy.wait_for_service('defect_detection_service')
client_motion = rospy.ServiceProxy('move_robot', robot_motion)
# client_camera = rospy.ServiceProxy('Camera_service', Ask_img)
client_defect_detection = rospy.ServiceProxy('defect_detection_service', defect_detect)
client_image_anomaly_detection = rospy.ServiceProxy('Image_anomaly_detection_service', Ask_img_AD)
pub_img_AD_score = rospy.Publisher('/Image_AD_score_plot', Float64MultiArray, queue_size = 100)
pub_motion_type = rospy.Publisher('/motion_type', String, queue_size = 100)

pub_motion_type.publish('PTP')
msg = Float64MultiArray()
msg.layout.dim = [MultiArrayDimension()]
msg.layout.dim[0].size = 2
msg.layout.dim[0].stride = 1
msg.layout.dim[0].label = "x"

#### for test #####
# print('start grinding path')
# goal_format = 'CPP' # "JPP" for joint_angle(rad), and "CPP" for end_effector(m)
# motion_type = 'line' # "PTP" for plan on joint space, and "line" for planning on Cartesian space
# velocity_scale = 0.03
# pose = [0.2905524, 0.5587873, 0.2315059, -2.6179938779914944, 0.0, 1.5707963267948966]
# res = client_motion(goal_format, motion_type,pose, velocity_scale)
# pose = [0.3096945, 0.5587873, 0.3002751, -2.6179938779914944, 0.0, 1.5707963267948966]
# res = client_motion(goal_format, motion_type,pose, velocity_scale)

if cap:
    # Capture path
    cap_trajectory = np.genfromtxt('path/20220721_capture_modify35.csv', delimiter=',') #cmd_0, 20220721_capture_modify35, grinding_pose, path_20220623-2, two_grinding_pose, geometry, path_grinding, three_grinding_pose
    print(cap_trajectory)
    goal_format = 'JPP' # "JPP" for joint_angle(rad), and "CPP" for end_effector(m)
    motion_type = 'PTP' # "PTP" for plan on joint space, and "line" for planning on Cartesian space
    # goal_format = 'CPP'
    velocity_scale = 0.06 # Max velocity scale for "PTP", and cartesian velocity(m/s) for "line"
    set_constraints = False
    #pose = [0.3693565, -0.18058459999999998, 0.390164, -0.05236336821833387, 0.016324064493902966, -1.0035538479212276]
    # pose = [-1.2756666790050786, 0.7099618618340273, 2.0786310529526895, -1.3514991257806488, -1.610319368426381, -1.9792654500465794]
    # pose = [-1.700819235042528, -0.14546525427051785, -2.564468867454755, 1.115553239790798, 1.5218679322996338, 1.4271773755291035]

    print('Moving to initial position')
    pose = [1.3496422652236157, -0.5497141274793291, -2.455721694439394, 1.4843550932907825, 1.5915318664201388, -2.815100289222657]
    # pose = [0,0,0,0,0,0]
    # pose = [-0.5,-0.5,0.5,0,0,0]
    req = robot_motionRequest()
    req.goal_format = goal_format
    req.motion_type = motion_type
    req.goal = pose
    req.velocity_scaling_factor = velocity_scale
    req.constraints = set_constraints

    res = client_motion(req) #####

    # res = client_motion(goal_format, motion_type,pose, velocity_scale, set_constraints)

    print("Initial variables")
    # res_frcnn = client_defect_detection("Var_ReInitialize")

    goal_format = 'CPP' # "JPP" for joint_angle(rad), and "CPP" for end_effector(m)
    set_constraints = True
    start_time = time.time()
    Execute_preproduct_plan = True
    print('start capture path')
    velocity_scale = 0.1 #0.06

    res_frcnn = client_defect_detection("Var_ReInitialize")
    req = robot_motionRequest()
    print("req: ",req)
    if Execute_preproduct_plan:
        for idx in range(48):
            print("idx:", idx)
            req.goal_format = 'plan'
            req.plan_name = 'plan_path/Capture_plan_20220905' # file name of plan
            req.plan_index = idx
            if idx==0:
                req.move_to_plan_first_pose = True
            else:
                req.move_to_plan_first_pose = False
            res = client_motion(req)
            print("Capturing image")
            res_frcnn = client_defect_detection("FasterRCNN_predict")
            # res_camera = client_camera(img_name)
            # if idx==6:
            # break
            print("Image_anomaly_detection")
            img_path = './image_AD'
            res_img_AD = client_image_anomaly_detection(img_path)
            print(f'AD_score is {res_img_AD.anomaly_score[0]}')
            msg.data = [idx,res_img_AD.anomaly_score[0]]
            print("Pub. img ad_score")
            pub_img_AD_score.publish(msg)

    else:
        # for idx,path in enumerate(cap_trajectory[:48]):
        #     pose = [float(path[2])/1000, float(path[3]/1000), float(path[4])/1000, float(path[5])/180*pi, float(path[6])/180*pi, float(path[7])/180*pi]
        #     # img_name = f'image/Capture_img_{idx}'
        #     print("idx:", idx)
        #     print("pose:", pose)
        #     res = client_motion(goal_format, motion_type,pose, velocity_scale, set_constraints)
        #     # res_camera = client_camera(img_name)
        #     print("Capturing image")
        #     break

        for idx,path in enumerate(cap_trajectory[:48]):
            pose = [float(path[2])/1000, float(path[3]/1000), float(path[4])/1000, float(path[5])/180*pi, float(path[6])/180*pi, float(path[7])/180*pi]
            print("idx:", idx)
            print("pose:", pose)
            req.goal_format = goal_format
            req.motion_type = motion_type
            req.goal = pose
            req.velocity_scaling_factor = velocity_scale
            req.constraints = set_constraints
            res = client_motion(req)
            # res = client_motion(goal_format, motion_type,pose, velocity_scale, set_constraints)
            print("Capturing image")
            res_frcnn = client_defect_detection("FasterRCNN_predict")
            # res_camera = client_camera(img_name)
            # if idx==6:
            #     break
            print("Image_anomaly_detection")
            img_path = './image_AD'
            res_img_AD = client_image_anomaly_detection(img_path)
            print(f'AD_score is {res_img_AD}')
    total_time = time.time()-start_time
    print("Total_capture_time:",total_time)


# for idx, path in enumerate(cap_trajectory[:48]):
#     pose = [float(path[2])/1000, float(path[3]/1000), float(path[4])/1000, float(path[5]), float(path[6]), float(path[7])]
#     print("idx:", idx)
#     print("pose:", pose)
#     res = client_motion(goal_format, motion_type,pose, velocity_scale, set_constraints)
#     print("Capturing image")
#     if idx==1:
#         break
#     break

# path = cap_trajectory
# pose = [float(path[2])/1000, float(path[3]/1000), float(path[4])/1000, float(path[5]), float(path[6]), float(path[7])]
# print("pose:", pose)
# res = client_motion(goal_format, motion_type,pose, velocity_scale, set_constraints)
# print("Capturing image")

    # res_frcnn = client_defect_detection("FasterRCNN_predict")
# capture_imgae_time = time.time()-start_time
# print("Capture_imgae_time:",capture_imgae_time)
# print('Start detection refine')
# res_frcnn = client_defect_detection("DetectionRefinement")

    

# res_frcnn = client_defect_detection("DetectionRefinement")
if grind:
    # Moving to initial position
    init_position = [-1.610123883482176, -0.7452320519245961, -1.3511192303467066, 2.1414749886221216, -1.53048521309263, 0.5937667469630724] # faucet grinding
    # init_position = [-1.6874324456889025, -0.5149424947966802, -1.7156670441386725, 1.1811958434098755, -1.5124628694588138, -0.10086152648860781] # plate grinding
    goal_format = 'JPP' # "JPP" for joint_angle(rad), and "CPP" for end_effector(m)
    motion_type = 'PTP' # "PTP" for plan on joint space, and "line" for planning on Cartesian space
    velocity_scale = 0.03 # Set a scaling factor for optionally reducing the maximum joint velocity. Allowed values are in (0,1]
    set_constraints = False
    print('Moving to initial position')
    req = robot_motionRequest()
    req.goal_format = goal_format
    req.motion_type = motion_type
    req.goal = init_position
    req.velocity_scaling_factor = velocity_scale
    req.constraints = set_constraints
    res = client_motion(req)
    # res = client_motion(goal_format, motion_type,init_position, velocity_scale, set_constraints) # [goal_format, motion_type, goal]

    if testing:
        rospy.wait_for_service('tm_driver/set_io')
        client_grinding = rospy.ServiceProxy('tm_driver/set_io', SetIO)
        module = 0 # 0 for control box, 1 for end effector
        IO_type = 1 # 0 for DI, 1 for DO
        pin = 7
        state = 1 # 1 for ON, 0 for OFF
        print('Set IO')
        res_grinding = client_grinding(module, IO_type, pin, state)

    if not sim:
        # Waiting for grinding head
        print('wait for grinding head service')
        rospy.wait_for_service('tm_driver/set_io')
        client_grinding = rospy.ServiceProxy('tm_driver/set_io', SetIO)
        module = 0 # 0 for control box, 1 for end effector
        IO_type = 1 # 0 for DI, 1 for DO
        pin = 7
        state = 1 # 1 for ON, 0 for OFF
        print('Set IO')
        res_grinding = client_grinding(module, IO_type, pin, state)
        if res_grinding.ok == 0:
            print('Set IO error!!!')

        # Waiting for calibration
        print('Waiting for calibration ...')
        while True:
            feedback_states = rospy.wait_for_message('/feedback_states', FeedbackState)
            calibration_state = list(feedback_states.cb_digital_input)[7]
            # print(calibration_state)
            # rospy.sleep(200)
            if calibration_state:
                break
    

    # Excute grinding path
    goal_format = 'CPP' # "JPP" for joint_angle(rad), and "CPP" for end_effector(m)
    motion_type = 'PTP' # "PTP" for plan on joint space, and "line" for planning on Cartesian space
    print('start grinding path')
    # grinding_path_file = 'path/grinding/plate_grinding_1018.csv' # ReGrinding_Cmd_20220907.txt path/20220723_grinding_big0.csv A30 S1 0312_minus3mm.csv plate_grinding_1006_space15x3.5
    grinding_path_file = 'path/20220723_grinding_big0.csv'
    grinding_trajectory = np.genfromtxt(grinding_path_file, delimiter=',')

    req = robot_motionRequest()
    # pub_motion_type.publish('PTP')

    Execute_preproduct_plan = True
    if Execute_preproduct_plan:
        grind_plan_name = 'plan_path/Grinding_T'
        with open(grind_plan_name+".yaml", 'r') as file_open:
            plan_len = len(list(yaml.load_all(file_open, Loader=SafeLoader)))
        for idx in range(plan_len):
            print("idx:", idx)
            req.goal_format = 'plan'
            req.plan_name = grind_plan_name # file name of plan
            req.plan_index = idx
            if idx==0:
                req.move_to_plan_first_pose = True
            else:
                req.move_to_plan_first_pose = False
            res = client_motion(req)
            print("Grinding")
            # if idx<3:
            #     print("press any key to continue...")
            #     input()
            # res_camera = client_camera(img_name)
            # if idx==6:
            # break
    else:
        for idx,path in enumerate(grinding_trajectory):
            # if idx==0:
            #     continue
            # if math.isnan(path[-1]):
            #     continue
            pose = [float(path[2])/1000, float(path[3]/1000), float(path[4])/1000, float(path[5])/180*pi, float(path[6])/180*pi, float(path[7])/180*pi]
            print("idx:", idx)
            print("pose:", pose)
            req.goal_format = goal_format
            req.motion_type = motion_type
            req.goal = pose
            req.velocity_scaling_factor = velocity_scale
            req.constraints = set_constraints
            res = client_motion(req)
            # res = client_motion(goal_format, motion_type,pose, velocity_scale, set_constraints)

            # break
    print("End of grinding !!")
client_grinding = rospy.ServiceProxy('tm_driver/set_io', SetIO)
module = 0 # 0 for control box, 1 for end effector
IO_type = 1 # 0 for DI, 1 for DO
pin = 7
state = 1 # 1 for ON, 0 for OFF
rospy.sleep(2)
state = 0
res_grinding = client_grinding(module, IO_type, pin, state)












# f = open('A30.txt')
# speed = 20
# for line in f.readlines():
#     cmd = line.split()
#     if cmd[0] == 'movlspdque':
#         if cmd[2] == '1':
#             velocity_scale = 0.005
#         else:
#             velocity_scale = 0.03
#     elif cmd[0] == 'movl':
#         pose = [float(cmd[2])/1000, float(cmd[3])/1000, float(cmd[4])/1000, float(cmd[5])/180*pi, float(cmd[6])/180*pi, float(cmd[7])/180*pi]
#         # print(pose)
#         res = client_motion(goal_format,motion_type,pose, velocity_scale, set_constraints)
