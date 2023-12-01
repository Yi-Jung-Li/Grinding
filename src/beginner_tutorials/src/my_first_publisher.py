import rospy
from std_msgs.msg import String

rospy.init_node('new_pub', anonymous=True)
pub = rospy.Publisher('/Time', String, queue_size=10)
print('start pub!!')
while True:
    time = f'Now time is {rospy.get_time()}'
    pub.publish(time)
    rospy.sleep(1)


