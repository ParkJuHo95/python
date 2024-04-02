import os
import numpy as np
import cv2

x_train = np.load("x_train.npy")
y_train = np.load("y_train.npy")

print(x_train.shape)
print(y_train.shape)
