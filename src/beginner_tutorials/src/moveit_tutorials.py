import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import numpy as np
import tf


# Setup ROS and Moveit
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('moveit_tutorials',anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "manipulator"
group = moveit_commander.MoveGroupCommander(group_name)

# Setting planning conditions
velocity_scale = 0.5
group.set_max_velocity_scaling_factor(velocity_scale)
group.set_goal_tolerance(0.001)

print('Press Enter to start motion!!')
raw_input()
# Setting goal pose
goal = [0.5,0.5,0,5,0,3.14,0]
roll = goal[3]
pitch = goal[4]
yaw = goal[5]
quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x = quaternion[0]
pose_goal.orientation.y = quaternion[1]
pose_goal.orientation.z = quaternion[2]
pose_goal.orientation.w = quaternion[3]
pose_goal.position.x = goal[0]
pose_goal.position.y = goal[1]
pose_goal.position.z = goal[2]
group.set_pose_target(pose_goal)

# Motion plan and excution
plan = group.plan()
group.execute(plan, wait=True)

# Move to another pose
print('Press Enter to move to another pose!!')
raw_input()
goal = [0.5,0.5,0,5,0,0.5,0]
roll = goal[3]
pitch = goal[4]
yaw = goal[5]
quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)

pose_goal = geometry_msgs.msg.Pose()
pose_goal.orientation.x = quaternion[0]
pose_goal.orientation.y = quaternion[1]
pose_goal.orientation.z = quaternion[2]
pose_goal.orientation.w = quaternion[3]
pose_goal.position.x = goal[0]
pose_goal.position.y = goal[1]
pose_goal.position.z = goal[2]
group.set_pose_target(pose_goal)


plan = group.plan()
group.execute(plan, wait=True)

group.stop()
