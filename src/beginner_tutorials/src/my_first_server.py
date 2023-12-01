import rospy
from beginner_tutorials.srv import ask_BMI, ask_BMIResponse


def callback(req):
    height = float(req.height)
    weight = float(req.weight)
    BMI = weight/(height/100)**2
    print(BMI)
    res = ask_BMIResponse()
    res.BMI = BMI
    return res

rospy.init_node('BMI_server', anonymous=True)
s = rospy.Service('/Cal_BMI_service', ask_BMI, callback)
rospy.spin()
