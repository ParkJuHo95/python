import tensorflow as tf
import numpy as np

x_train = np.array([
        [1,0],
        [0,1]
    ])

y_train = np.array([
        1,0
    ])

model = tf.keras.models.load_model('holl.h5')

pred_rf = model.predict(np.array([ [0,1] ]))

print(np.argmax(pred_rf))










