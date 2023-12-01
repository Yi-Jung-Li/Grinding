#!/usr/bin/env python
#from home.biorola.cps_ros.src.trajectory_function import plan_to_yaml, yaml_to_plan
import os
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
from moveit_msgs.srv import GetPositionFK
from moveit_msgs.srv import GetPositionFKRequest
from moveit_msgs.srv import GetPositionFKResponse
from std_msgs.msg import Header
import numpy as np
from std_msgs.msg import Int32
from math import pi
import time
import trajectory_function



############### start init ###################

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial',anonymous=True)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "manipulator"
group = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)


# FK
# rospy.wait_for_service("/compute_fk ")
# http://docs.ros.org/en/noetic/api/moveit_msgs/html/srv/GetPositionFK.html
client_fk = rospy.ServiceProxy("/compute_fk", GetPositionFK)
new_pos = group.get_current_state()
link_name = "link_6"
header = Header()
header.frame_id = 'base'
req = GetPositionFKRequest()
req.header = header
req.robot_state = new_pos
req.fk_link_names = [link_name]
res = client_fk(req)
# print(res.pose_stamped[0].pose)
pos = trajectory_function.compute_fk(group, link_name, 'base')
print(list(new_pos.joint_state.position))
