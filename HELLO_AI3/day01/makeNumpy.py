import numpy as np
import os
import cv2
arr_eng = [
        "GA","NA","DA","RA","MA",
        "BA","SA","AA","JA","CA"
    ]

files = os.listdir("gana_resize/")

x_train = np.array([])
y_train = np.array([])


for f in files:
    label = f[0:2]
    myclass = -1
    if label == "GA" : myclass = 0
    if label == "NA" : myclass = 1
    if label == "DA" : myclass = 2
    if label == "RA" : myclass = 3
    if label == "MA" : myclass = 4
    if label == "BA" : myclass = 5
    if label == "SA" : myclass = 6
    if label == "AA" : myclass = 7
    if label == "JA" : myclass = 8
    if label == "CA" : myclass = 9
    
    my_np = np.array([myclass])
    y_train = np.concatenate((y_train, my_np))

    img = cv2.imread(f"gana_resize/{f}")
    # print(img.shape)
    img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    img = cv2.resize(img,(56,56))
    img = np.reshape(img,(56*56))
    x_train = np.concatenate((x_train,img))

x_train = np.reshape(x_train,(-1,56,56))

# print(myNp.shape)

np.save("x_train",x_train)
np.save("y_train",y_train)

print(x_train)
print(x_train.shape)
print(y_train)
print(y_train.shape)