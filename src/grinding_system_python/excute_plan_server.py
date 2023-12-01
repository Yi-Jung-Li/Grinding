#!/usr/bin/env python
# coding: utf-8

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from std_msgs.msg import String
import numpy as np
import time
import tf
import trajectory_function
from tm_msgs.srv import robot_motion
from tm_msgs.srv import *
from tm_msgs.srv import defect_detect
from moveit_msgs.msg import RobotState, Constraints, OrientationConstraint, JointConstraint
import yaml
from yaml.loader import SafeLoader

def move_to_initial_point(group, joint_angle):
    group.set_max_velocity_scaling_factor(0.08)
    joint_goal = group.get_current_joint_values()
    for i,joint_a in enumerate(joint_angle):
        joint_goal[i] = joint_a

    group.go(joint_goal, wait=True)

def wait_for_state_update(box_name,box_is_known=False, box_is_attached=False, timeout=4):
    # Copy class variables to local variables to make the web tutorials more clear.
    # In practice, you should use the class variables directly unless you have a good
    # reason not to.
    box_name = box_name

    ## BEGIN_SUB_TUTORIAL wait_for_scene_update
    ##
    ## Ensuring Collision Updates Are Receieved
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ## If the Python node dies before publishing a collision object update message, the message
    ## could get lost and the box will not appear. To ensure that the updates are
    ## made, we wait until we see the changes reflected in the
    ## ``get_attached_objects()`` and ``get_known_object_names()`` lists.
    ## For the purpose of this tutorial, we call this function after adding,
    ## removing, attaching or detaching an object in the planning scene. We then wait
    ## until the updates have been made or ``timeout`` seconds have passed
    start = rospy.get_time()
    seconds = rospy.get_time()
    while (seconds - start < timeout) and not rospy.is_shutdown():
        # Test if the box is in attached objects
        attached_objects = scene.get_attached_objects([box_name])
        is_attached = len(attached_objects.keys()) > 0

        # Test if the box is in the scene.
        # Note that attaching the box will remove it from known_objects
        is_known = box_name in scene.get_known_object_names()

        # Test if we are in the expected state
        if (box_is_attached == is_attached) and (box_is_known == is_known):
            return True

        # Sleep so that we give other threads time on the processor
        rospy.sleep(0.1)
        seconds = rospy.get_time()

    # If we exited the while loop without returning then we timed out
    return False
    ## END_SUB_TUTORIAL

def set_constraints(group):
    constraint = Constraints()
    constraint.name = "joint constraint"
    joint_constraint = JointConstraint()
    joint_constraint.position = 1.35
    joint_constraint.tolerance_above = 0.5
    joint_constraint.tolerance_below = 0.5
    joint_constraint.weight = 1
    joint_constraint.joint_name = "joint_1"

    joint_constraint2 = JointConstraint()
    joint_constraint2.position = -0.55
    joint_constraint2.tolerance_above = 0.5
    joint_constraint2.tolerance_below = 0.5
    joint_constraint2.weight = 1
    joint_constraint2.joint_name = "joint_2"

    joint_constraint3 = JointConstraint()
    joint_constraint3.position = 1.48
    joint_constraint3.tolerance_above = 1
    joint_constraint3.tolerance_below = 1
    joint_constraint3.weight = 1
    joint_constraint3.joint_name = "joint_4"

    joint_constraint4 = JointConstraint()
    joint_constraint4.position = -2.03
    joint_constraint4.tolerance_above = 3.14
    joint_constraint4.tolerance_below = 3.14
    joint_constraint4.weight = 1
    joint_constraint4.joint_name = "joint_6"

    # constraint.joint_constraints = [joint_constraint]
    constraint.joint_constraints = [joint_constraint, joint_constraint2, joint_constraint3, joint_constraint4]
    group.set_path_constraints(constraint)

def add_objection(group):
    rospy.sleep(1)
    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "base"
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.z = -0.355 # slightly above the end effector
    box_name = "box"
    scene.add_box(box_name, box_pose, size=(3.0, 3.0, 0.7))

    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "base"
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.z = 0.05 # slightly above the end effector
    box_pose.pose.position.x = -0.6
    box_name = "box3"
    scene.add_box(box_name, box_pose, size=(0.1, 1.0, 0.1))

    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "base"
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.z = 0.05+0.5 # slightly above the end effector
    box_pose.pose.position.x = -0.75
    box_name = "wall1"
    scene.add_box(box_name, box_pose, size=(0.1, 3.0, 2))

    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "base"
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.z = 0.05+0.5 # slightly above the end effector
    box_pose.pose.position.y = 1.270
    box_name = "wall2"
    scene.add_box(box_name, box_pose, size=(1.5, 0.1, 2))

    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "base"
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.x = -0.08+0.14 # slightly above the end effector
    box_pose.pose.position.y = -0.70375-0.2875/2
    box_pose.pose.position.z = 0.3743819/2
    box_name = "cam"
    scene.add_box(box_name, box_pose, size=(0.28, 0.2875, 0.3743819))
    # # xyz="-0.08 -0.70375 0.3743819" rpy="1.5707963267949 0 0"
    # # box: 180*287.5

    # box_pose = geometry_msgs.msg.PoseStamped()
    # box_pose.header.frame_id = "base"
    # box_pose.pose.orientation.w = 1.0
    # box_pose.pose.position.x = -0.08+0.14 # slightly above the end effector
    # box_pose.pose.position.y = -0.70375-0.2875/2
    # box_pose.pose.position.z = 0.28/2
    # box_name = "macro_cam_box"
    # scene.add_box(box_name, box_pose, size=(0.28, 0.2875, 0.28/2+0.08))

    # box_pose = geometry_msgs.msg.PoseStamped()
    # box_pose.header.frame_id = "base"
    # box_pose.pose.orientation.w = 1.0
    # box_pose.pose.position.x = -0.08+0.14 # slightly above the end effector
    # box_pose.pose.position.y = -0.70375-0.28750+0.07
    # box_pose.pose.position.z = 0.28+0.035
    # box_name = "macro-lens"
    # scene.add_box(box_name, box_pose, size=(0.28, 0.14, 0.07))

    # box_pose = geometry_msgs.msg.PoseStamped()
    # box_pose.header.frame_id = "base"
    # box_pose.pose.orientation.w = 1.0
    # box_pose.pose.position.x = -0.08+0.14 # slightly above the end effector
    # box_pose.pose.position.y = -0.70375-0.2875/2+0.07965
    # box_pose.pose.position.z = 0.28+0.015
    # box_name = "cam_support"
    # scene.add_box(box_name, box_pose, size=(0.28, 0.01, 0.03))

    # box_pose = geometry_msgs.msg.PoseStamped()
    # box_pose.header.frame_id = "base"
    # box_pose.pose.orientation.w = 1.0
    # box_pose.pose.position.z = 0.1055-0.015-0.02
    # box_pose.pose.position.y = 0.89446 #0.8925, 0.8938372 # slightly above the end effector
    # box_pose.pose.position.x = -0.18248 #-0.18, -0.1820069
    # box_name = "tool_point"
    # scene.add_box(box_name, box_pose, size=(0.01, 0.01, 0.01))

    # box_pose = geometry_msgs.msg.PoseStamped()
    # box_pose.header.frame_id = "link_6"
    # box_pose.pose.orientation.w = 1.0
    # box_pose.pose.position.z = 0.008+0.06895519/2
    # box_pose.pose.position.y = -0.045983 # slightly above the end effector
    # box_pose.pose.position.x = 0
    # box_name = "faucet_T"
    # scene.add_box(box_name, box_pose, size=(0.16290126, 0.15240165, 0.06895519))

    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "base"
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.z = 0
    box_pose.pose.position.y = 0.8925
    box_pose.pose.position.x = -0.06
    box_name = "grinding_tool"
    scene.add_box(box_name, box_pose, size=(0.17, 0.17, 0.27)) # D=0.15

    return wait_for_state_update(box_name="faucet_T",box_is_known=True)

def attach_box():
    # robot = moveit_commander.RobotCommander()
    grasping_group = 'manipulator'
    touch_links = robot.get_link_names(group=grasping_group)
    scene.attach_box("link_6", "faucet_T", touch_links=touch_links)

def detach_box(timeout=4):
    # Copy class variables to local variables to make the web tutorials more clear.
    # In practice, you should use the class variables directly unless you have a good
    # reason not to.

    ## BEGIN_SUB_TUTORIAL detach_object
    ##
    ## Detaching Objects from the Robot
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ## We can also detach and remove the object from the planning scene:
    scene.remove_attached_object("link_6", name="faucet_T")
    ## END_SUB_TUTORIAL

    # We wait for the planning scene to update.
    return wait_for_state_update(box_name="faucet_T", box_is_known=True, box_is_attached=False, timeout=timeout)


def remove_box(timeout=4):
    # Copy class variables to local variables to make the web tutorials more clear.
    # In practice, you should use the class variables directly unless you have a good
    # reason not to.

    ## BEGIN_SUB_TUTORIAL remove_object
    ##
    ## Removing Objects from the Planning Scene
    ## ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ## We can remove the box from the world.
    scene.remove_world_object("box")
    scene.remove_world_object("box3")
    scene.remove_world_object("wall1")
    scene.remove_world_object("wall2")
    scene.remove_world_object("cam")
    scene.remove_world_object("grinding_tool")
    # scene.remove_world_object("tool_point")
    # scene.remove_world_object("faucet_T")

    ## **Note:** The object must be detached before we can remove it from the world
    ## END_SUB_TUTORIAL

    # We wait for the planning scene to update.
    return wait_for_state_update(box_name="grinding_tool", box_is_attached=False, box_is_known=False, timeout=timeout)

def move_robot_to_certain_point(req):
    global loaded_plan
    global last_loaded_path
    global plans
    if req.goal_format == 'init':
        plans = []
        loaded_plan = None
        last_loaded_path = None
        init_pose = [1.3496422652236157, -0.5497141274793291, -2.455721694439394, 1.4843550932907825, 1.5915318664201388, -2.815100289222657]
        move_to_initial_point(group, init_pose)
        return robot_motionResponse(True)

    # Excute certain motion plan
    if req.goal_format == 'plan':
        pub_motion_type.publish('PTP')
        file_path = req.plan_name
        plan_idx = req.plan_index
        move_to_plan_first_pose = req.move_to_plan_first_pose
        print("Loading plan ...")
        load_path = file_path+".yaml"
        if last_loaded_path != load_path:
            last_loaded_path = load_path
            with open(load_path, 'r') as file_open:
                loaded_plan = list(yaml.load_all(file_open, Loader=SafeLoader))
        if move_to_plan_first_pose:
            print("Move to first position ...")
            first_pos = loaded_plan[plan_idx]['joint_trajectory']['points'][0]['positions']
            move_to_initial_point(group, first_pos)
        
        print("Start excuting plan " + str(plan_idx))
        plan = loaded_plan[plan_idx]
        plan_moveit_format = trajectory_function.yaml_to_plan(plan)
        group.execute(plan_moveit_format)
        return robot_motionResponse(True)

    # Test the format of goal
    velocity_scale = req.velocity_scaling_factor
    last_time = time.time()
    group.set_max_velocity_scaling_factor(velocity_scale)
    if len(req.goal)%6!=0:
        print('The format of the goal point does not match, please input joint angel [j1,j2,...j6] or pose [x,y,z,roll,pitch,yaw]')
        return robot_motionResponse(False)

    if req.constraints:
        set_constraints(group)
    else: 
        group.clear_path_constraints()


    # Planning to a Joint Goal
    if req.goal_format == 'JPP':
        print('goal format is joint_state')
        # pub_motion_type.publish('PTP')
        joint_goal = group.get_current_joint_values()
        for i, value in enumerate(req.goal):
            joint_goal[i] = value
        print('start moving')
        group.go(joint_goal, wait=True)
        group.stop()
        now_time = time.time()
        use_time = now_time-last_time
        print("time:",use_time)
        group.clear_path_constraints()
        return robot_motionResponse(True)
    # Planning to a Pose Goal
    else:
        print('goal format is eef')
        # Joint space plan
        if req.motion_type == 'PTP':
            print('motion type is PTP')
            # pub_motion_type.publish('PTP')
            roll = req.goal[3]
            pitch = req.goal[4]
            yaw = req.goal[5]
            quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
            pose_goal = geometry_msgs.msg.Pose()
            pose_goal.orientation.x = quaternion[0]
            pose_goal.orientation.y = quaternion[1]
            pose_goal.orientation.z = quaternion[2]
            pose_goal.orientation.w = quaternion[3]
            pose_goal.position.x = req.goal[0]
            pose_goal.position.y = req.goal[1]
            pose_goal.position.z = req.goal[2]
            group.set_pose_target(pose_goal)
            print('start moving')

            # plan = group.go(wait=True)
            plan = group.plan()
            group.execute(plan, wait=True)
            plans.append(plan)
            group.stop()
            now_time = time.time()
            use_time = now_time-last_time
            print("time:",use_time)
            group.clear_pose_targets()
            group.clear_path_constraints()
            return robot_motionResponse(True)
        # Cartesian space plan
        else:
            print('motion type is line')
            waypoints = []
            print('line points: ', len(req.goal)//6)
            for i in range(len(req.goal)//6):
                # pub_motion_type.publish('Line')
                roll = req.goal[i*6+3]
                pitch = req.goal[i*6+4]
                yaw = req.goal[i*6+5]
                quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
                wpose = group.get_current_pose().pose
                wpose.position.x = req.goal[i*6+0]
                wpose.position.y = req.goal[i*6+1]
                wpose.position.z = req.goal[i*6+2]
                wpose.orientation.x = quaternion[0]
                wpose.orientation.y = quaternion[1]
                wpose.orientation.z = quaternion[2]
                wpose.orientation.w = quaternion[3]
                waypoints.append(copy.deepcopy(wpose))

            (plan, fraction) = group.compute_cartesian_path(
                                    waypoints,   # waypoints to follown
                                    0.001,        # eef_step
                                    0.0)  
            print('start moving')
            plan = group.retime_trajectory(group.get_current_state(), plan, velocity_scale)
            # plans.append(plan)
            group.execute(plan, wait=True)
            now_time = time.time()
            use_time = now_time-last_time
            print("time:",use_time)
            group.clear_path_constraints()
            return robot_motionResponse(True)

# Setup ROS and Moveit
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_robot',anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "manipulator"
group = moveit_commander.MoveGroupCommander(group_name)

save_plan = True

print("eff_link: ",group.get_end_effector_link())
print("original tol: ", group.get_goal_tolerance())
# group.set_goal_position_tolerance(0.000001)
# group.set_goal_joint_tolerance(0.001)
# group.set_goal_orientation_tolerance(0.000001)
print("tol: ", group.get_goal_tolerance())

add_objection(group)
# attach_box()

global loaded_plan
global last_loaded_path
global plans
plans = []
loaded_plan = None
last_loaded_path = None
s = rospy.Service('move_robot', robot_motion, move_robot_to_certain_point)
pub_motion_type = rospy.Publisher('/motion_type', String, queue_size = 100)
pub_motion_type.publish('PTP')

rospy.spin()
# try:
#     rospy.spin()
# except KeyboardInterrupt:
#     print("remove")
#     print(remove_box())
# print("detach_box: ", detach_box())
# print("remove")
# print(remove_box())
if save_plan:
    save_path = 'plan_path/Capture_plan.yaml'
    trajectory_function.plan_to_yaml(plans,save_path)

