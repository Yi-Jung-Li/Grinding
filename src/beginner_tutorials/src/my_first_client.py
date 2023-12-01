import rospy
from beginner_tutorials.srv import ask_BMI, ask_BMIRequest
from std_msgs.msg import String

print(String)

rospy.init_node('BMI_client', anonymous=True)
rospy.wait_for_service('/Cal_BMI_service')
client = rospy.ServiceProxy('/Cal_BMI_service', ask_BMI)
while True:
    input('Press Enter to start calcular your BMI!!')
    height = input('Input your height')
    weight = input('Input your weight')
    request = ask_BMIRequest()
    request.height = float(height)
    request.weight = float(weight)
    response = client(request)
    BMI = response.BMI
    if BMI > 25:
        print(f'Your BMI is {BMI}, and you are so fat!!')
    else:
        print(f'Your BMI is {BMI}')