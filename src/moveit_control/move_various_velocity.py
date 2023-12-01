#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import tf
import geometry_msgs.msg
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
velocity = object_configure_yaml['velocity']
print('velocity = ',velocity)
print ('detect object waypoints:', path_cords)

# parameter for light and capture delay
camera_capture_delay_time = 1
loop_idx=1
image_folder = '/home/drciv-dev/aoi_machine/src/output/'+detect_object+'/'
rospy.set_param('image_save_folder', image_folder)
light_patterns_list = rospy.get_param("/light_pattern",[[0,0]])

# wait until light service init done
if args.light:
    print("wait for light service")
    rospy.wait_for_service('light')
    setLights = rospy.ServiceProxy('light', SetLight)
    print("light service init done")
    light_delay_time = rospy.get_param("/light_delay_time",0.07)
# wait until camera service init done
if args.camera:
    print("wait for flir service")
    rospy.wait_for_service('flir')
    setCamera = rospy.ServiceProxy('flir', SetCamera)
    print("flir_camera service init done")

############### end init ###################


# mq function
def on_pub(client, userdata, result):
    print(userdata)
    print(result)

def on_connect(client, userdata, flags, rc):
    print('connect to bridge')
    client.subscribe(subscribe_topic)
    # print(userdata)
    print('connect to bridge done')


# Light and capture image
def light_capture(cord_idx):
    """Light and image capture
    # Argument
        cord_idx: image index
    """

    # Set cord_idx for image filename
    rospy.set_param('cord_idx', str(cord_idx))
    print(light_patterns_list)

    for light_idx, light_patterns in enumerate(light_patterns_list):
        if args.light:
            print("lights_pattern:", light_patterns)
            # init lights with all 0
            light_response = setLights(0,0,light_delay_time)
            print (light_response.success, light_response.message)

            # turn on lights pattern
            for light_para in light_patterns:
                print(light_para)
                light_response = setLights(light_para[0],light_para[1],light_delay_time)
                print (light_response.success, light_response.message)
        
        #start capture image
        rospy.set_param('image_name_str', str(  ) + '_' + str(light_idx) + '_' + str(light_patterns))
        if args.camera:
            flir_response = setCamera("trigger")
            print(flir_response.message, flir_response.message)
    
    if args.light:
        # turn off light
        light_response = setLights(0,0,light_delay_time)
        print (light_response.success, light_response.message)
    if args.camera:
        # retrieve images
        flir_response = setCamera("retrieve")
        print(flir_response.message)

roll = 0
pitch = 0
yaw = 0
quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)


group.set_max_velocity_scaling_factor(velocity)

group.set_max_velocity_scaling_factor(1)
group.set_max_acceleration_scaling_factor(0.0001)

start_time = time.time()
if args.arm:
    aoi_moveit_utils.go_origin(group)
rospy.set_param('loop_idx', str(loop_idx))
for cord_idx, cord in enumerate(path_cords):
    if args.arm:
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
        plan1 = group.plan()
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
    light_capture(cord_idx)
    

if args.arm:
    aoi_moveit_utils.go_origin(group)
elapsed_time = time.time() - start_time
print('round '+ str(loop_idx) +' complete')
print ('files count in round '+ str(loop_idx) +' is ' + str(len(glob.glob1(image_folder,'Image_'+str(loop_idx)+'_*'))))
print('elapsed: ' + str(elapsed_time)+' secs')

if args.arm:
    moveit_commander.roscpp_shutdown()
