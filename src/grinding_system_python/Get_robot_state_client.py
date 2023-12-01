#!/usr/bin/env python
# coding: utf-8

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
        num_workers=0,
        pin_memory=torch.cuda.is_available()
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

# Hyper-parameters
sequence_length = 5
shift = 1
# input = 6 joint angles
input_size = 15
hidden_size = 64
num_layers = 2
# output = 6 joint angles(next 10 time step)
num_classes = 15
batch_size = 16
num_epochs = 20
learning_rate = 0.01

model = torch.load('model_transform.pth')
#model = torch.load('model.pth')
model.eval()

# Load mean and std.
mean = np.genfromtxt('mean.csv', delimiter=',')
std = np.genfromtxt('std.csv', delimiter=',')

# Setup ROS and Moveit
dt = 0.1
print('wait for service')
rospy.wait_for_service('get_robot_state')
c = rospy.ServiceProxy('get_robot_state', robot_state)
res = c(1)

# Initialize the initaial value 
test_data = np.zeros((1, sequence_length, input_size))
res = c(1)  # Request 1
last_JointData = np.array(res.joint_state)
for i in range(5):
    
    res = c(1)
    JointData = np.array(res.joint_state)
    end_effect =  np.array(res.end_effect)
    velocity = (JointData-last_JointData)/dt
    last_JointData = JointData
    # Normalize
    JointData = (JointData-mean[:6])/std[:6]
    end_effect =  (end_effect-mean[6:9])/std[6:9]
    velocity = (velocity-mean[9:15])/std[9:15]


    # Updata the test data by shifting data
    test_data[0,:4] = test_data[0,1:]
    test_data[0,4,:6] = JointData
    test_data[0,4,9:] = velocity
    test_data[0,4,6:9] = end_effect
    rospy.sleep(0.1)
#print(test_data)
test_target = np.zeros((1,input_size))
mse = np.zeros((20))
x = np.arange(20)
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_ylim(0.0,4)
line1, = ax.plot(x, mse, 'b-')
while 1:
    res = c(1)
    JointData = np.array(res.joint_state)
    end_effect =  np.array(res.end_effect)
    velocity = (JointData-last_JointData)/dt
    last_JointData = JointData
    # Normalize
    JointData = (JointData-mean[:6])/std[:6]
    end_effect =  (end_effect-mean[6:9])/std[6:9]
    velocity = (velocity-mean[9:15])/std[9:15]

    test_target[0,:6] = JointData
    test_target[0,9:] = velocity
    test_target[0,6:9] = end_effect

    # Anomaly detect
    test_mse = Max_SE_cal(test_data, test_target)
    print(test_mse)
    # updata the MSE
    mse[:-1] = mse[1:]
    mse[-1] = test_mse
    #plt.plot(mse)
    line1.set_ydata(mse)
    fig.canvas.draw()
    fig.canvas.flush_events()

    #updata the test data
    test_data[0,:4] = test_data[0,1:]
    test_data[0,4] = test_target
    rospy.sleep(0.1)






