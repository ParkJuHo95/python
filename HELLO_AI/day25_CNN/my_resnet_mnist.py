from tensorflow import keras
from keras.models import load_model
from tensorboard.compat import tf
import numpy as np
import cv2

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_test_ori = x_test

x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

model = keras.applications.resnet.ResNet50(weights=None, input_tensor=keras.layers.Input(shape=(28, 28, 1)), classes=4)
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=1)

pred = model.predict(x_test)
print(np.argmax(pred))