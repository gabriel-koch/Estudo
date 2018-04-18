# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 13:14:35 2018

@author: R210
"""

import timeit

start = timeit.default_timer()

import mnist_loader
import network3

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = network3.Network([784, 30, 10]) #mini_batch_size=10)

evaluation_cost, evaluation_accuracy,\
training_cost, training_accuracy =\
net.SGD(training_data, 30, 10, 0.1)
#        lmbda = 20,
#        evaluation_data=validation_data,
#        monitor_evaluation_accuracy=True)
#        monitor_evaluation_cost=True,
#        monitor_training_accuracy=True,
#        monitor_training_cost=True)


stop = timeit.default_timer()

print (stop - start)