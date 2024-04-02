from tensorflow import keras
from keras.models import load_model
from tensorboard.compat import tf
import cv2
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_test_ori = x_test

x_train = x_train.reshape((60000, 28, 28, 1)) / 255.0
x_test = x_test.reshape((10000, 28, 28, 1)) / 255.0

model = tf.keras.models.load_model('first.h5')
model.summary()

pred = model.predict(x_test)

for idx,img in enumerate(x_test_ori):
    myidx = np.argmax(pred[idx])
    goog = y_test[idx]
    print(idx,"myidx",myidx,goog)
    if myidx != goog:
        cv2.imwrite('x/{}_{}_{}.png'.format(idx,myidx,goog),img)