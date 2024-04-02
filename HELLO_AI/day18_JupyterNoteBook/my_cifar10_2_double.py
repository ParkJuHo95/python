from keras.datasets import cifar10
import numpy as np


(x_train, y_train), (x_test, y_test) = cifar10.load_data()

x_train1 = x_train
y_train1 = y_train
x_test1 = x_test
y_test1 = y_test


for i in range(1,20):
    x_train = np.append(x_train,x_train1)
    y_train = np.append(y_train,y_train1)
    x_test = np.append(x_test,x_test1)
    y_test = np.append(y_test,y_test1)

    x_train = x_train.reshape(-1,32,32,3)
    y_train = y_train.reshape(-1,1)
    x_test = x_test.reshape(-1,32,32,3)
    y_test = y_test.reshape(-1,1)

    np.save(f"x_train{i}",x_train)
    np.save(f"y_train{i}",y_train)
    np.save(f"x_test{i}",x_test)
    np.save(f"y_test{i}",y_test)