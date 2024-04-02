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

import os

os.environ["CUDA_VISIBLE_DEVICES"]="-1"
#숫자는 gpu의 몇번째것을 사용할지 -1은 gpu사용하지않는다 => cpu를 사용한다
start = time.time()

x_train = np.load("x_train5.npy")
y_train = np.load("y_train5.npy")
x_test = np.load("x_test5.npy")
y_test = np.load("y_test5.npy")

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

model = Sequential(name='CIFAR10_CNN')

model.add(Conv2D(filters=32, kernel_size=(3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)))
model.add(Conv2D(filters=32, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(Conv2D(filters=64, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(10, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

time.time()

hist = model.fit(x_train, y_train, epochs=1, batch_size=32, validation_data=(x_test, y_test))
end = time.time()

print(f"2번째 데이터 걸린 시간 : {math.floor(end-start)}s", )
    
