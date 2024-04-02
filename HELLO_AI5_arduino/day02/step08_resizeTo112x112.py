import cv2
import os

dir = "animal_en_s/"

list = os.listdir(dir)
x = 80
y = 55
w = 497
h = 373

for i in list:
    files = os.listdir(f"{dir}{i}")
    for f in files:
        wavFile = f"{dir}{i}/{f}"
        img = cv2.imread(wavFile)
        img = img[y:y+h,x:x+w]
        img = cv2.resize(img,(112,112),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(f"animal_en_s_size112/{i}/{f[0:3]}.jpg",img)
        


