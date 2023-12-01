#!/usr/bin/env python

import numpy as np
import yaml
from yaml.loader import SafeLoader
import argparse
from tqdm import tqdm
import math


parser = argparse.ArgumentParser()
parser.add_argument("-r", "--noise_range", type=float, default=0.5)
parser.add_argument("-f", "--file", type=str, help="yaml file name", default="plan")
parser.add_argument("-s", "--save_path", type=str, help="yaml saved path", default="motion_plan/plan")
args = parser.parse_args()


load_path = str(args.file)+'.yaml'
save_path = str(args.save_path)+'.yaml'

print("Loading plan ...")
with open(load_path, 'r') as file_open:
        loaded_plan = list(yaml.load_all(file_open, Loader=SafeLoader))

spoof_plan = []
mean = 1
# Set max noise angle(degree)
if args.noise_range > 1:
    print("Noise is too large, set noise as 0.5")
    range = 0.5
else:
    range = args.noise_range
    print('noise_range is {}'.format(range))

num = len(loaded_plan)
bar = tqdm(total = num,position = 0, leave=True)
# Spoof trajectory positions values with uniform noise
for index, plan in  enumerate(loaded_plan):
    bar.set_description('Generating | {}/{}'.format(index+1,num))
    bar.update()
    plan_len = len(plan['joint_trajectory']['points'])
    for idx,points in enumerate(plan['joint_trajectory']['points']):
        if idx < 2 or idx > int(plan_len/2):continue
        scale = np.random.rand(6)
        scale = (scale-0.5)*2
        scale = scale*range/180*math.pi
        points['positions'] = (np.array(points['positions']) + scale).tolist()
    spoof_plan.append(plan)

print('saving file ...')
with open(save_path, 'w') as file_save:
    yaml.dump_all(spoof_plan, file_save, default_flow_style=False) 

