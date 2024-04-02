from tensorflow import keras
from keras.models import load_model
from tensorboard.compat import tf
import numpy as np
import cv2

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_test_ori = x_test

x_train = x_train.reshape((-1, 28, 28, 1))
x_test = x_test.reshape((-1, 28, 28, 1))

model = keras.applications.VGG16(weights=None, input_tensor=keras.layers.Input(shape=(28, 28, 1)), classes=10)

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

pred = model.predict(x_test)
print(np.argmax(pred))
# for idx,img in enumerate(x_test_ori):
#     myidx = np.argmax(pred[idx])
#     goog = y_test[idx]
#     print(idx,"myidx",myidx,goog)
#     if myidx != goog:
#         cv2.imwrite('x/{}_{}_{}.png'.format(myidx,goog,idx),img)