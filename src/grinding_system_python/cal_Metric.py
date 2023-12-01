#!/usr/bin/env python
# coding: utf-8


"""
Created on Sun Aug 15 2021
@author: Samuel
"""

import numpy as np


def softmax(x):   
    f_x = np.exp(x) / np.sum(np.exp(x))
    return f_x


def tpr95(test,other,start,end):    
    gap = (end- start)/10000
    total = 0.0
    fpr = 0.0
    for delta in np.arange(start, end, gap):
        tpr = np.sum(np.sum(test >= delta)) / np.float(len(test))
        error2 = np.sum(np.sum(other > delta)) / np.float(len(other))
        if tpr <= 0.965 and tpr >= 0.935:
            fpr += error2
            total += 1
    fprBase = fpr/total
    
    return fprBase

def auroc(test,other,start,end):
    gap = (end - start)/1000
    precisionVec = []
    recallVec = []
    aurocBase = 0.0
    fprTemp = 1.0
    for delta in np.arange(start, end, gap):
        tpr = np.sum(np.sum(test >= delta)) / np.float(len(test))
        fpr = np.sum(np.sum(other> delta)) / np.float(len(other))
        aurocBase += (-fpr+fprTemp)*tpr
        fprTemp = fpr
    aurocBase += fpr * tpr
    
    return aurocBase

def auprIn(test,other,start,end):
    gap = (end - start)/1000
    auprBase = 0.0
    recallTemp = 1.0
    precisionVec = []
    recallVec = []
    for delta in np.arange(start, end, gap):
        tp = np.sum(np.sum(test >= delta)) / np.float(len(test))
        fp = np.sum(np.sum(other >= delta)) / np.float(len(other))
        if tp + fp == 0:continue
        precision = tp / (tp + fp)
        recall = tp
        auprBase += (recallTemp-recall)*precision
        recallTemp = recall
    auprBase += recall * precision
    
    return auprBase


def auprOut(test,other,start,end):
    gap = (end - start)/1000
    auprBase = 0.0
    recallTemp = 1.0
    precisionVec = []
    recallVec = []
    for delta in np.arange(end, start, -gap):
        fp = np.sum(np.sum(test <= delta)) / np.float(len(test))
        tp = np.sum(np.sum(other <= delta)) / np.float(len(other))
        if tp + fp == 0: break
        precision = tp / (tp + fp)
        recall = tp
        auprBase += (recallTemp-recall)*precision
        recallTemp = recall
    auprBase += recall * precision
    
    return auprBase






