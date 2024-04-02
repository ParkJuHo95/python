from tensorflow import keras
from keras.models import load_model
from tensorboard.compat import tf
import numpy as np
import cv2

x_test = cv2.imread("1.png")
x_test = cv2.resize(x_test,(28,28))
x_test = np.reshape(x_test,(-1,28,28,1))

model = keras.applications.resnet.ResNet50(weights=None, input_tensor=keras.layers.Input(shape=(28, 28, 1)), classes=10)

pred = model.predict(x_test)
print(np.argmax(pred))
