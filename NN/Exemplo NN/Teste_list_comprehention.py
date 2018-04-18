# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 16:43:19 2018

@author: R210
"""

layers = [784, 30, 10]

params = [param for layer in layers for param in layer.params]

print(params)