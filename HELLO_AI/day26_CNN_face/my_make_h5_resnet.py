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
from tensorflow import keras
start = time.time()

x_train = np.load("x_train.npy")
y_train = np.load("y_train.npy")
print(x_train.shape)
# for i in range(10):
#     cv2.imshow(x_train[i])

# x_train = x_train.astype('float32')
x_train = x_train.astype('float32') / 255.0

# y_train = np_utils.to_categorical(y_train)

model = keras.applications.resnet.ResNet50(weights=None, input_tensor=keras.layers.Input(shape=(32, 32, 3)), classes=4)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# time.time()

model.fit(x_train, y_train, epochs=10)
model.save('face.h5')
# end = time.time()

# print(f"걸린 시간 : {math.floor(end-start)}s", )
