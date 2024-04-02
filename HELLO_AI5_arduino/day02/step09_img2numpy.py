import numpy as np
import os
import cv2
arr_eng = [
        "GA","NA","DA","RA","MA",
        "BA","SA","AA","JA","CA"
    ]
dir = "animal_en_s_size112/"

list = os.listdir(dir)

x_train = np.array([])
y_train = np.array([])


for i in list:
    files = os.listdir(f"{dir}{i}")
    for f in files:
        my_np = np.array([i])
        y_train = np.concatenate((y_train, my_np))
        img = cv2.imread(f"{dir}{i}/{f}")
        img = np.reshape(img,(112*112*3))
        x_train = np.concatenate((x_train,img))

x_train = np.reshape(x_train,(-1,112,112,3))

# print(myNp.shape)

np.save("x_train",x_train)
np.save("y_train",y_train)

print(x_train)
print(x_train.shape)
print(y_train)
print(y_train.shape)