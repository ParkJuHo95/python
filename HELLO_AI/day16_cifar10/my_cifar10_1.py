# 0:airplane
# 1:automobile
# 2:bird
# 3:cat
# 4:deer
# 5:dog
# 6:frog
# 7:horse
# 8:ship
# 9:truck

import numpy as np
from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
import tensorflow as tf
from keras.layers import Conv2D, MaxPooling2D, Flatten
import cv2
import matplotlib.pyplot as plt
import time
import math


(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print("x_train.shape",x_train.shape)
print("y_train.shape",y_train.shape)
print("x_test.shape",x_test.shape)
print("y_test.shape",y_test.shape)

tf.config.experimental.list_physical_devices('GPU')


for idx,x in enumerate(x_train):
    cv2.imwrite(f'img/{y_train[idx][0]}/{idx}.png',x_train[idx])
    if idx == 1000:
        break