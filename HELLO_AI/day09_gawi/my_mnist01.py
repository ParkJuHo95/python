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
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(3,)),
    tf.keras.layers.Dense(512, activation = tf.nn.relu),
    tf.keras.layers.Dense(512, activation = tf.nn.relu),
    tf.keras.layers.Dense(3, activation=tf.nn.softmax)
])

# 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 학습 (값,값,돌릴횟수,램사용?클수록 실행하면 분모가 줄어듬,옵션) - 뒤에 3개는 없어도 기본값으로 들어감 - accuracy:정확도
model.fit(x_train, y_train, epochs=20)
model.save('gawi.h5')

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










