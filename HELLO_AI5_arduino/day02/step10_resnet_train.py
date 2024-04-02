import cv2
from keras.models import load_model
from keras.utils import np_utils
from tensorboard.compat import tf
from tensorflow import keras

import numpy as np


x_train = np.load("x_train.npy") / 255.0
y_train = np.load("y_train.npy")
print(x_train.shape)
print(y_train.shape)
# x_train = x_train / 255.0
# img = cv2.imread("A00.jpg")
# img = cv2.resize(img,(112,112))
# x_test = img
# x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
# x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

model = keras.applications.resnet.ResNet50(weights=None, input_tensor=keras.layers.Input(shape=(112,112,3)), classes=5)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(np.array(x_train), y_train, epochs=5)