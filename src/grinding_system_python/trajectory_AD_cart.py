#!/usr/bin/env python
# coding: utf-8


from moveit_msgs.srv import GetPositionFK
from moveit_msgs.srv import GetPositionFKRequest
from moveit_msgs.srv import GetPositionFKResponse
from std_msgs.msg import Header
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import MultiArrayDimension

from geometry_msgs.msg import PoseStamped
from sensor_msgs.msg import JointState
from moveit_msgs.msg import RobotState


import sys
import copy
import rospy
import numpy as np
import time
import torch 
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from tm_msgs.srv import robot_state
from tm_msgs.srv import *
from tm_msgs.msg import FeedbackState


# Recurrent neural network (many-to-one)
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        # Set initial hidden and cell states 
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        
        # Forward propagate LSTM
        out, _ = self.lstm(x, (h0, c0))  # out: tensor of shape (batch_size, seq_length, hidden_size)
        
        # Decode the hidden state of the last time step
        out = self.fc(out[:, -1, :])
        return out
    
class MyDataset(Dataset):
    def __init__(self, data, target, transform=None):
        self.data = torch.from_numpy(data).float()
        self.target = torch.from_numpy(target).float()
        self.transform = transform
        
    def __getitem__(self, index):
        x = self.data[index]
        y = self.target[index]
        
        if self.transform:
            x = self.transform(x)
        
        return x, y
    
    def __len__(self):
        return len(self.data)
    

def coodination_trasform(data):
    R = np.array([[0,-1,0],[1,0,0],[0,0,1]])
    T = np.array([0.21,0,-0.87])
    for i,value in enumerate(data):
        ee = value[6:9]
        new_ee = np.dot(ee,R.T)+T
        data[i,6:9] = new_ee 
    return data

def MSE(label,predict):
    SE = (label-predict)**2
    MSE = np.mean(SE)
    return MSE

def Max_SE_cal(test_data, test_target):
    test_dataset = MyDataset(test_data, test_target)
    test_loader = DataLoader(
        test_dataset,
        batch_size=1,
        shuffle=False,
        num_workers=0
        # pin_memory=torch.cuda.is_available()
    )

    for k, (inputs, labels) in enumerate(test_loader):
        outputs = model(inputs)
        outputs = outputs.detach().numpy()[0]
        label = labels.detach().numpy()[0]
        mse = MSE(label,outputs)
    return mse


#Setup RNN

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
device = torch.device('cuda')

# Hyper-parameters
sequence_length = 5
shift = 1
input_size = 6
hidden_size = 64
num_layers = 2
num_classes = 6
batch_size = 32


# model = torch.load('model/model_real_MA_sl8_hs64_bs16_num_epochs30_g0.9_l1.pth')
model = torch.load('model/model_cart_real_MA_NS_v01_sl5_hs64_bs32_num_epochs40_g0.9_l2.pth')
#model = torch.load('model.pth')
model.eval()

# Load mean and std.
mean = np.genfromtxt('model/mean_cart.csv', delimiter=',')
std = np.genfromtxt('model/std_cart.csv', delimiter=',')

# Setup ROS
rospy.init_node('Trajectory_anomaly_detection_cart')
client_fk = rospy.ServiceProxy("/compute_fk", GetPositionFK)
pub_AD_score = rospy.Publisher('/AD_score_cart', Float64MultiArray, queue_size = 100)
msg = Float64MultiArray()
msg.layout.dim = [MultiArrayDimension()]
msg.layout.dim[0].size = 40
msg.layout.dim[0].stride = 1
msg.layout.dim[0].label = "x"

# Initialize the initaial value 
sample_size = 3
sampling_time = 0.03
test_data = np.zeros((1, sequence_length, input_size))
raw_data_one = np.zeros((input_size))
end_effect = np.zeros(3)
last_time = time.time()

# EWMA
L = 8
Lambda = 0.05
test_mse_mean = 0.0034
test_mse_std = 0.009
UCL_ss = test_mse_mean +L*test_mse_std*np.sqrt(Lambda/(2-Lambda))
UCL_ss = 0.1932
Z_0 = test_mse_mean
Z = np.ones(20)*test_mse_mean
mse_all = []
# Def. RobotState (for fk)
robot_state = RobotState()
robot_state.joint_state.header.frame_id = "base"
robot_state.joint_state.name = ['joint_1','joint_2','joint_3','joint_4','joint_5','joint_6']
robot_state.multi_dof_joint_state.header.frame_id = "base"
for i in range(sequence_length):
    # Down-sample
    raw_data = np.zeros((input_size))
    for i in range(sample_size):
        # Get eef. and velocity of eef.
        feedback_states = rospy.wait_for_message('/feedback_states', FeedbackState)

        end_effect = list(feedback_states.tool_pose)[:3]
        end_effect_velocity = list(feedback_states.tcp_speed)[:3]

        end_effect = np.array(end_effect)
        end_effect_velocity = np.array(end_effect_velocity)

        # Normalize
        end_effect = (end_effect-mean[:3])/std[:3]
        end_effect_velocity = (end_effect_velocity-mean[3:6])/std[3:6]

        raw_data_one[:3] = end_effect
        raw_data_one[3:6] = end_effect_velocity

        
        raw_data = raw_data + raw_data_one
        T = time.time()
        while T-last_time < sampling_time:
            rospy.sleep(0.0005)
            T = time.time()
        last_time = T

    # Updata the test data by shifting data
    test_data[0,:-1] = test_data[0,1:]
    test_data[0,-1] = raw_data/sample_size
    # rospy.sleep(0.1)
#print(test_data)
plt.close()
test_target = np.zeros((1,input_size))
threshold_value = 0.02314
mse = np.zeros((20))
mse_buffer = np.zeros((40))
max_mse_buffer = np.zeros((20))
ad_sample_lengh = 10
threshold = np.ones((20))*threshold_value
threshold_EWMA = np.ones((20))*UCL_ss
x = np.arange(20)
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_ylim(0.0,0.2)
ax.set_xlabel('Timestep')
ax.set_ylabel('Anomaly score(MSE)')
ax.set_title("Anomaly Detection")
line1, = ax.plot(x, mse, 'b-')
line2, = ax.plot(x, threshold, 'r-')
# ax2 = fig.add_subplot(122)
# ax2.set_xlabel('Timestep')
# ax2.set_ylabel('Anomaly score(Z)')
# ax2.set_title("EWMA Anomaly Detection")
# ax2.set_ylim(0.0,0.03)
# line3, = ax2.plot(x, Z, 'b-')
# line4, = ax2.plot(x, threshold_EWMA, 'r-')


try:
    while 1:


        raw_data = np.zeros((input_size))
        for i in range(sample_size):
            # Get eef. and velocity of eef.
            feedback_states = rospy.wait_for_message('/feedback_states', FeedbackState)

            end_effect = list(feedback_states.tool_pose)[:3]
            end_effect_velocity = list(feedback_states.tcp_speed)[:3]

            end_effect = np.array(end_effect)
            end_effect_velocity = np.array(end_effect_velocity)

            # Normalize
            end_effect = (end_effect-mean[:3])/std[:3]
            end_effect_velocity = (end_effect_velocity-mean[3:6])/std[3:6]

            raw_data_one[:3] = end_effect
            raw_data_one[3:6] = end_effect_velocity

            raw_data = raw_data + raw_data_one

            T = time.time()
            while T-last_time < sampling_time:
                rospy.sleep(0.0001)
                T = time.time()
            # print('T:',T-last_time)
            last_time = T
        test_target[0] = raw_data/sample_size

        # Anomaly detect
        test_mse = Max_SE_cal(test_data, test_target)
        # print(test_mse)
        # updata the MSE
        mse[:-1] = mse[1:]
        mse[-1] = test_mse
        # updata the MSE
        mse_buffer[:-1] = mse_buffer[1:]
        mse_buffer[-1] = test_mse

        # Calculate max MSE (AD score)
        mse_sort = np.sort(mse_buffer)
        max_mse = np.mean(mse_sort[-ad_sample_lengh])

        # updata the max_mse
        max_mse_buffer[:-1] = max_mse_buffer[1:]
        max_mse_buffer[-1] = max_mse

        # updata the EWMA
        Z[:-1] = Z[1:]
        # Z_now = (1-Lambda)*Z[-1]+Lambda*test_mse**(1/3.6)
        Z[-1] = (1-Lambda)*Z[-1]+Lambda*(test_mse**(1/3.6))
        print(Z[-1], max_mse_buffer[-1])

        # AD_score = np.append(mse,Z)
        AD_score = np.append(max_mse_buffer,Z)
        msg.data = AD_score.tolist()
        pub_AD_score.publish(msg)

        #plt.plot(mse)
        # line1.set_ydata(mse)
        # line3.set_ydata(Z)
        # fig.canvas.draw()
        # fig.canvas.flush_events()

        #updata the test data
        test_data[0,:-1] = test_data[0,1:] 
        test_data[0,-1] = test_target
except KeyboardInterrupt:
    mse_all = np.array(mse_all)
    print(np.mean(mse_all))
    print(np.std(mse_all))
    plt.close()
# Setup ROS and Moveit
# rospy.init_node('Trajectory_anomaly_detection')
# pose = rospy.wait_for_message('/tool_pose', PoseStamped)
# joint_state = rospy.wait_for_message('/joint_states', JointState)
# print(pose.pose.position)
# print(joint_state.position)
# print(joint_state.velocity)
