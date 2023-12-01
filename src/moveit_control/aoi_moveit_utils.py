import rospy
import copy
# ros message format lib
import geometry_msgs.msg
# constraint library
from moveit_msgs.msg import RobotState, Constraints, OrientationConstraint, JointConstraint
from geometry_msgs.msg import Quaternion
# ROS TF library
import tf
roll = 0
pitch = 0
yaw = 0
quaternion = tf.transformations.quaternion_from_euler(roll, pitch, yaw)

def go_origin(group, z=0.266):
    """move arm to origin of turntable
    """
    waypoints = []
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position.x = 0
    pose_goal.position.y = 0
    pose_goal.position.z = z#0.266#0.271#0.259#0.242
    pose_goal.orientation.x = quaternion[0]
    pose_goal.orientation.y = quaternion[1]
    pose_goal.orientation.z = quaternion[2]
    pose_goal.orientation.w = quaternion[3]
    waypoints.append(copy.deepcopy(pose_goal))
    # group.set_pose_target(pose_goal)
    (cartesian_plan, fraction) = group.compute_cartesian_path(
                                    waypoints,   # waypoints to follow
                                    0.01,        # eef_step
                                    0.0)         # jump_threshold
    exe1 = group.execute(cartesian_plan, wait=True)
    group.stop()

def upright_constraint():
    """Planing constraint for joint axis
    # Return
        Robot arm planing constraint message for keeping upright
    """
    rospy.loginfo("add joint constraint")
    constraint = Constraints()
    constraint.name = "joint constraint"
    joint_constraint = JointConstraint()
    joint_constraint.position = 0
    joint_constraint.tolerance_above = 3.14/3
    joint_constraint.tolerance_below = 3.14/3
    joint_constraint.weight = 1
    joint_constraint.joint_name = "motoman_gp8_joint_6_t"

    joint_constraint2 = JointConstraint()
    joint_constraint2.position = 0
    joint_constraint2.tolerance_above = 3.14/3
    joint_constraint2.tolerance_below = 3.14/3
    joint_constraint2.weight = 1
    joint_constraint2.joint_name = "motoman_gp8_joint_4_r"

    constraint.joint_constraints = [joint_constraint,joint_constraint2]
    return constraint

def tilt_constraint():
    """Planing constraint for joint axis
    # Return
        Robot arm planing constraint message for keeping upright
    """
    rospy.loginfo("add orientation constraint")
    constraint = Constraints()
    constraint.name = "orientation constraint"
    tilt_constraint = OrientationConstraint()
    tilt_constraint.header.frame_id = "workcell_base"
    tilt_constraint.link_name = "motoman_gp8_camera"
    tilt_constraint.orientation = Quaternion(0, 0, 1, 0)
    tilt_constraint.absolute_x_axis_tolerance = 3.14/8
    tilt_constraint.absolute_y_axis_tolerance = 3.14/8
    tilt_constraint.absolute_z_axis_tolerance = 3.14/8
    tilt_constraint.weight = 1

    constraint.orientation_constraints = [upright_constraint]
    return constraint

def enable_constraint(group,constraint):
    """Enable constraint for motion planing
    # Argument
        group: Planing group (MoveGroupCommander)
        constraint: constraint message (joint, orientation)
    # Return
        group: with constraint
    """
    group.set_path_constraints(constraint)