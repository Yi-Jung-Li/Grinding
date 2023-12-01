import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import datasets, transforms
import torch.optim as optim
import matplotlib.pyplot as plt
import torch.utils.data as data
import os
import torchvision.models as models
#from sklearn.metrics import confusion_matrix
#import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
from torch.autograd import Variable
from cal_Metric import *
from tqdm import tqdm

TEST_DATA_PATH =  "image/"

img_size = 256
b_size = 1
test_transform = transforms.Compose([
                                    transforms.Resize((img_size,img_size)),
                                    transforms.ToTensor(),
                                    transforms.Normalize((0.485,0.456,0.406), (0.229,0.224,0.225))
                                    ])
test_data = datasets.ImageFolder(root=TEST_DATA_PATH,transform=test_transform)
test_data_loader  = data.DataLoader(test_data, batch_size=b_size, shuffle=False, num_workers=4) 


def ODIN(model,data_loader,temper,noiseMagnitude1):
    T = 1
    model.eval()
    ODIN_out = []
    bar = tqdm(total = len(data_loader), position=0, leave=True)
    for i, (datas, target) in enumerate(data_loader):
        bar.set_description('ODIN_score')
        bar.update()
        datas, target = datas.to(device), target.to(device)
        inputs = Variable(datas, requires_grad = True)
        scores = model(inputs)
        
        max_scores, _ = torch.max(scores, dim = 1)
        max_scores.backward(torch.ones(len(max_scores)).to(device))
        
        # Normalizing the gradient to binary in {-1, 1}
        gradient = torch.ge(inputs.grad.data, 0)
        gradient = (gradient.float() - 0.5) * 2
        # Normalizing the gradient to the same space of image
        gradient[::, 0] = (gradient[::, 0] )/(0.229)
        gradient[::, 1] = (gradient[::, 1] )/(0.224)
        gradient[::, 2] = (gradient[::, 2] )/(0.225)
        # Adding small perturbations to images
        tempInputs = torch.add(inputs.data, gradient, alpha=noiseMagnitude1)

        # Now calculate score
        scores = model(tempInputs)
        scores = scores / temper
        for score in scores:
            score = score - torch.max(score) # scale the output value to avoide overflow of exp.
            score = torch.exp(torch.max(score))/torch.sum(torch.exp(score))
            ODIN_out.append(score.data.cpu().numpy())

    return np.array(ODIN_out)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.load("resnet18_gan_tune_model_best.pth").to(device)
resnet18_test_odin = ODIN(model,test_data_loader,1000,0.0014)
print(resnet18_test_odin)