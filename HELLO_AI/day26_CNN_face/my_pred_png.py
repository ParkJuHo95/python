from keras.utils import np_utils
from keras.datasets import cifar10
import numpy as np
import tensorflow as tf
import cv2

arr = [
    {'lbl':0,'f':'00','n':'박주호'},
    {'lbl':1,'f':'01','n':'박지원'},
    {'lbl':2,'f':'02','n':'이미소'},
    {'lbl':3,'f':'03','n':'하예종'}
]

img = cv2.imread("132.png")
img = cv2.resize(img,(32,32))
# x_test = x_test.reshape(-1,32,32,3)
img = np.reshape(img,(-1,32,32,3))/255

# x_test = x_test.astype('float32') / 255.0

model = tf.keras.models.load_model('face.h5')
model.summary()

pred = model.predict(img)

# for i in arr:
#     if i['lbl'] == np.argmax(pred):
#         print(i['n']) 

myidx = np.argmax(pred)
print(arr[myidx]['n'])

