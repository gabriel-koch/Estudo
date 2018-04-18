# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 18:54:12 2017

@author: Hugo
"""
import timeit

start = timeit.default_timer()

import mnist_loader
import network3

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = network3.Network([784, 100, 10], 10)
net.SGD(training_data, 30, 10, 100, test_data=test_data)


stop = timeit.default_timer()

print (stop - start)