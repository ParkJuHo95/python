import os
import cv2
import numpy as np

arr = [
    {'lbl':0,'f':'00','n':'박주호'},
    {'lbl':1,'f':'01','n':'박지원'},
    {'lbl':2,'f':'02','n':'이미소'},
    {'lbl':3,'f':'03','n':'하예종'}
]

# x_train = []
# y_train = []
x_train = np.array([])
y_train = np.array([])

for i in arr:
    file_list = os.listdir(f"./pre/{i['f']}")
    file_list_png = [file for file in file_list if file.endswith(".png")]
    for png in file_list_png:
        # x_train.append(cv2.imread(f"pre/{i['f']}/{png}"))
        x_train = np.append(x_train,cv2.imread(f"pre/{i['f']}/{png}"))
        y_train = np.append(y_train,i['lbl'])
        
# x_train = np.array(x_train)
# y_train = np.array(y_train)
x_train = np.reshape(x_train,(-1,32,32,3))
y_train = np.reshape(y_train,(-1,1))

print(x_train.shape)
print(y_train.shape)

print(x_train)
print(y_train)

np.save("x_train",x_train)
np.save("y_train",y_train)
