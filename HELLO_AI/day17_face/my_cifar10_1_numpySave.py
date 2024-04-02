from keras.utils import np_utils
from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten
import cv2
import matplotlib.pyplot as plt
import time
import math
import numpy as np


(x_train, y_train), (x_test, y_test) = cifar10.load_data()

np.save("x_train",x_train)
# np.save("y_train",y_train)
# np.save("x_test",x_test)
# np.save("y_test",y_test)


# np_x = np.load("x_train.npy")
# np_x2 = np.append(np_x,np_x)
# np_x2 = np.reshape(np_x2,(100000,32,32,3))
# np_x2 = np_x.reshape(-1,32,32,3)        
# -1 은 알아서 처리해라

# print(np_x2)
# print(np_x2.shape)
# np.save("x_train2",np_x2)
# np.save("x_train",np_x2)
