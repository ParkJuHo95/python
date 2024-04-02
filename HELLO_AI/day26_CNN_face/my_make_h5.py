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

start = time.time()

x_train = np.load("x_train.npy")
y_train = np.load("y_train.npy")

# for i in range(10):
#     cv2.imshow(x_train[i])

x_train = x_train.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)

# width = 32
# height = 32
# channel = 3

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

model.add(Dense(4, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

time.time()

hist = model.fit(x_train, y_train, epochs=15, batch_size=32)
model.save('face.h5')
end = time.time()

print(f"걸린 시간 : {math.floor(end-start)}s", )
