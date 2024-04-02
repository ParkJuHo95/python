from tensorflow import keras
from keras.models import load_model
import cv2
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

model = load_model('first.h5')

model.summary()

# 이미지 로드 및 그레이로 벼환
img = cv2.imread('9.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)
# 크기 조절
size = (28,28)
img_resize = cv2.resize(img_gray,size)
print(img_resize.shape)

# 이미지 출력해봄
cv2.imshow('image', img_resize)
cv2.waitKey(1000)

# 이미지 shape
img_resize2 = img_resize.reshape((1, 28, 28, 1)) / 255.0
print(img_resize2.shape)
# 예측
pred = model.predict(img_resize2)

print(pred)
print(np.argmax(pred))