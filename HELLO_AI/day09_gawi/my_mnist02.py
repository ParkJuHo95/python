import tensorflow as tf
import numpy as np

x_train = np.array([
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ])

y_train = np.array([
        0,1,2
    ])

# 모델 구성 = 뇌
model = tf.keras.models.load_model('gawi.h5')

pred = model.predict(x_train)

for p in pred:
    myidx = np.argmax(p)
    print("myidx",myidx,p)
#
x_rf = np.array([
        [1,0,0]
    ])

pred_rf = model.predict(x_rf)

print(np.argmax(pred_rf))










