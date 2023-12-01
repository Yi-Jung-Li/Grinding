import rospy
from beginner_tutorials.msg import my_info

rospy.init_node('my_info_pub', anonymous=True)
pub = rospy.Publisher('/My_infomation', my_info, queue_size=20)
print('start pub!!')
while True:
    input('Press Enter to start!!')
    name = input('Input your name')
    height = input('Input your height')
    weight = input('Input your weight')
    info = my_info()
    info.name = str(name)
    info.height = float(height)
    info.weight = float(weight)
    pub.publish(info)



