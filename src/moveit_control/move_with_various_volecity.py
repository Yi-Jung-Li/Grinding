#!/usr/bin/env python

from os import wait
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import tf
import geometry_msgs.msg
import trajectory_function
import numpy as np

from std_msgs.msg import Int32
from math import pi
# Utils
import aoi_moveit_utils
# light & camera library
from std_msgs.msg import String
from light.srv import SetLight
from flir_camera.srv import SetCamera
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
import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
import ssl
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--arm", help="disable robot arm", action="store_false", default=True)
parser.add_argument("-c", "--camera", help="disable camera capture", action="store_false", default=True)
parser.add_argument("-l", "--light", help="disable light", action="store_false", default=True)
parser.add_argument("-n", "--number", type=int, help="loop times", default=1)
parser.add_argument("-o", "--object", type=str, help="objects name", default="none")
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
    group_name = "gp8_camera"
    group = moveit_commander.MoveGroupCommander(group_name)
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)
    motion_state_pub = rospy.Publisher('/motion_state',Int32,queue_size=10)

    print("ref frame: ", group.get_pose_reference_frame())
    group.set_pose_reference_frame('/workcell_turntable')
    # speed scaling factor
    # group.set_max_velocity_scaling_factor(0.001)
    print("new ref frame: ", group.get_pose_reference_frame())

# Load detect object from parameter server
if args.object is not 'none':
    rospy.set_param('detect_object', args.object)
detect_object = rospy.get_param("/detect_object", args.object)
print ('detect object name:', detect_object)
f = open('config/'+detect_object+'.yaml', 'r')
object_configure_yaml = load(f)
f.close()
upload_params('/', object_configure_yaml)
print(object_configure_yaml)
path_cords = object_configure_yaml['way_points']
velocity = rospy.get_param("/velocity",0.1)
velocity = object_configure_yaml['velocity']
print('velocity = ',velocity)
print ('detect object waypoints:', path_cords)



roll = 0
pitch = 0
yaw = 0
quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)

plans = []
group.set_max_velocity_scaling_factor(velocity)
motion_state_pub.publish(0)
origin_point = geometry_msgs.msg.Pose()
origin_point.position.z = 0.266
aoi_moveit_utils.go_origin(group)
#while 1:
for cord_idx, cord in enumerate(path_cords):
    motion_state_pub.publish(0)
    #rospy.sleep(0.3)
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position.x = 0.025*float(cord[0])#sys.argv[1])
    pose_goal.position.y = 0.025*float(cord[1])#sys.argv[2])
    pose_goal.position.z = float(cord[2]) #0.271#0.242
    pose_goal.orientation.x = quaternion[0]
    pose_goal.orientation.y = quaternion[1]
    pose_goal.orientation.z = quaternion[2]
    pose_goal.orientation.w = quaternion[3]
    group.set_pose_target(pose_goal)
    # setup constraint
    constraint = aoi_moveit_utils.upright_constraint()
    # constraint = tilt_constraint() ## unstable
    aoi_moveit_utils.enable_constraint(group, constraint)
    rospy.loginfo("Known path constraints:\n{}".format(group.get_path_constraints()))
    # show goal tolerance
    print (group.get_goal_joint_tolerance())
    print (group.get_goal_orientation_tolerance())
    print (group.get_goal_position_tolerance())
    print (group.get_goal_tolerance())
    # set goal tolerance
    group.set_goal_tolerance(0.005)
    print (group.get_goal_tolerance())
    # show & set planning time
    print (group.get_planning_time())
    # group.set_planning_time(1)
    # group.set_num_planning_attempts(10)
    # move arm
    group.set_start_state_to_current_state()
    motion_state_pub.publish(1)
    plan1 = group.plan()
    plans.append(plan1)
    exe1 = group.go()
    while exe1 == False:
        rospy.logerr("Execute Failed Re-Run")
        exe1 = group.go()
    group.stop()
    group.clear_path_constraints()
    print ('done point %d' % cord_idx)
    # video capture
    # if cord_idx == 0:
    #     subprocess.Popen("pwd")
    #     subprocess.Popen(['python', 'SaveToAvi.py'])
    # light # capture images
   # light_capture(cord_idx)
motion_state_pub.publish(2)

group.set_pose_target(origin_point)
plan1 = group.plan()
plans.append(plan1)
exe1 = group.go()

if velocity == 1:
    v = 'fast'
elif velocity == 0.01:
    v = 'slow'
else:
    v = 'mid'
save_path = 'various_velocity_trajectory/'+v+'.yaml'
trajectory_function.plan_to_yaml(plans,save_path)

if args.arm:
    moveit_commander.roscpp_shutdown()
