# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:51:51 2018

@author: R210
"""
import numpy as np

inputs= [1, 2, 3, 4]
weights = [[4, 5, 6, 7], [8,9,10,11]]

def soma(inputs, weights, bias):
    
    total = 0
    for i,j in zip(inputs, weights):
        total = total + i*j
    
    v = total + bias
    return v


def sigmoidal(v, a):
    y= 1/ (1 + np.exp(-v*a))
    return y

def linear(v):
    return v

v = soma(inputs, weights, 1)
y = sigmoidal(v,0.1)
print(y)