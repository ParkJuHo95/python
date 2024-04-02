from tensorflow import keras
from keras.models import load_model
from tensorboard.compat import tf
import numpy as np
import cv2
from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_test_ori = x_test

model = keras.applications.InceptionV3(weights=None, input_tensor=keras.layers.Input(shape=(32, 32, 3)),input_shape=(32, 32, 3), classes=10)
#inceptionV3는 최소 사이즈가 75*75가 넘어야해서 현재는 오류남
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()
model.fit(x_train, y_train)

pred = model.predict(x_test)
print(np.argmax(pred))
# for idx,img in enumerate(x_test_ori):
#     myidx = np.argmax(pred[idx])
#     goog = y_test[idx]
#     print(idx,"myidx",myidx,goog)
#     if myidx != goog:
#         cv2.imwrite('x/{}_{}_{}.png'.format(myidx,goog,idx),img)