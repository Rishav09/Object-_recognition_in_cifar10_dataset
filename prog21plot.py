#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 23:10:18 2018

@author: rishav
"""
from keras.datasets import cifar10
from matplotlib import pyplot
from scipy.misc import toimage

(X_train,y_train),(X_test,y_test)=cifar10.load_data()

for i in range(0,9):
    pyplot.subplot(330+1+i)
    pyplot.imshow(toimage(X_train[i]))

pyplot.show()    


