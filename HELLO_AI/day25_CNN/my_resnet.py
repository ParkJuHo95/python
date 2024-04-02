import tensorflow.keras as keras
import cv2
import numpy as np
from day25_CNN.imageLabel import ImageLabel


li = ImageLabel()
# img1 = cv2.imread('iu.png')
# img1 = cv2.imread('dong.jpg')
img1 = cv2.imread('images.jpg')
# img1 = cv2.imread('dongs.jpg')
img1_1 = cv2.resize(img1,(224,224))
img_result = np.reshape(img1_1,(-1,224,224,3))
print(img_result.shape)

model = keras.applications.resnet.ResNet50()

pred = model.predict(img_result)
first = np.argmax(pred)
print(li.label[first])
pred[0][first] = 0
second = np.argmax(pred)
print(li.label[second])
pred[0][second] = 0
third = np.argmax(pred)
print(li.label[third])
pred[0][third] = 0
fourth = np.argmax(pred)
print(li.label[fourth])
