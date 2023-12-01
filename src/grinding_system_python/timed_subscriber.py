from tm_msgs.msg import FeedbackState
import rospy
import time
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sim", help="true for simulation", action="store_true") # -s, when no DIO
args = parser.parse_args()
sim = args.sim

rospy.init_node('timed_subscriber')
state = rospy.wait_for_message('/feedback_states', FeedbackState)
print("Wait for start...")
if sim:
    while True:
        feedback_states = rospy.wait_for_message('/feedback_states', FeedbackState)
        calibration_state = list(feedback_states.cb_digital_output)[7]
        # print(calibration_state)
        # rospy.sleep(200)
        if calibration_state:
            print("start!!!")
            break
else:
    while True:
        feedback_states = rospy.wait_for_message('/feedback_states', FeedbackState)
        calibration_state = list(feedback_states.cb_digital_input)[7]
        # print(calibration_state)
        # rospy.sleep(200)
        if calibration_state:
            print("start!!!")
            break

All_states = []

start_time = time.time()
seconds = 0.01
file_name = 'feedback.json'
try:
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        # if elapsed_time > seconds:
        # print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        feedback_states = rospy.wait_for_message('/feedback_states', FeedbackState)
        calibration_state = list(feedback_states.cb_digital_output)[7]
        if not calibration_state:
            print("Break!!!")
            break

        state = {}
        state["time"] = current_time
        state["joint_pos"] = feedback_states.joint_pos
        state["joint_vel"] = feedback_states.joint_vel
        state["joint_tor"] = feedback_states.joint_tor
        state["tool_pose"] = feedback_states.tool_pose
        state["tcp_speed"] = feedback_states.tcp_speed
        state["tcp_force"] = feedback_states.tcp_force
        All_states.append(state)

        start_time = current_time
            # break

    with open(file_name,'w') as jsonfile:
        # jsonfile.write(json.dumps(All_states))
        json.dump(All_states, jsonfile)

    print("Save file!!!")

except KeyboardInterrupt:
    with open(file_name,'w') as jsonfile:
        # jsonfile.write(json.dumps(All_states))
        json.dump(All_states, jsonfile)

    print("Save file!!!")


# print(type(state))