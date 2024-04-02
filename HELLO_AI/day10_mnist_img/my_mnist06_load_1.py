from tensorflow import keras
from keras.models import load_model
import cv2
import numpy as np

img = cv2.imread('9_1.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_28 = cv2.resize(img_gray,(28,28))

x_test1 = np.reshape(img_gray_28,(1,28,28,1)) / 255

model = load_model('first.h5')

model.summary()

pred = model.predict(x_test1)
result = np.argmax(pred)
print(result)
