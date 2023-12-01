import rospy
from std_msgs.msg import String

def callback(data):
    print("I heard that:",data.data)

rospy.init_node('new_sub', anonymous=True)
rospy.Subscriber("/Time", String, callback)
rospy.spin()