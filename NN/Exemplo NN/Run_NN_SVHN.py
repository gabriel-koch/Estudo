# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 13:14:35 2018

@author: R210
"""

import timeit

start = timeit.default_timer()

import network3

training_data, validation_data, test_data = network3.load_data_shared()

mini_batch_size = 10

net = network3.Network([
        network3.ConvPoolLayer(input_shape=(mini_batch_size, 1, 28, 28),
                      filter_shape=(20, 1, 5, 5),
                      poolsize=(2,2)),
        network3.FullyConnectedLayer(n_in=20*12*12, n_out=100),
        network3.SoftmaxLayer(n_in=100, n_out=10)], mini_batch_size)

net.SGD(training_data, 60, mini_batch_size, 0.1, validation_data, test_data)

stop = timeit.default_timer()

print (stop - start)