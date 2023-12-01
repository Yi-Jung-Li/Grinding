import rospy
from beginner_tutorials.msg import my_info

def callback(data):
    print(f"I am {data.name}, my height is {data.height} cm and weight is {data.weight} kg.")

rospy.init_node('my_info_sub', anonymous=True)
rospy.Subscriber('/My_infomation', my_info, callback)
rospy.spin()