from keras.utils import np_utils
from keras.datasets import cifar10
import numpy as np
import tensorflow as tf
import cv2


(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_test_ori = x_test
# for i in range(10):
#     cv2.imshow(x_train[i])

x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

# width = 32
# height = 32
# channel = 3
model = tf.keras.models.load_model('cifar10.h5')
model.summary()

pred = model.predict(x_test)

for idx,img in enumerate(x_test_ori):
    myidx = np.argmax(pred[idx])
    goog = np.argmax(y_test[idx])
    print(idx,"myidx",myidx,goog)
    if myidx != goog:
        cv2.imwrite('x/{}_{}_{}.png'.format(myidx,goog,idx),img)