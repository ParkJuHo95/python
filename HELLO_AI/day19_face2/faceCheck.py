import os
import cv2
arr = []

file_list = os.listdir("./pre01/1조/07")
file_list_png = [file for file in file_list if file.endswith(".png")]
for idx,i in enumerate(file_list_png):
    image = cv2.imread(f"pre01/1조/07/{i}")
    # img = cv2.imread('iu.png')
    print(image)
    # print(f"/pre01/1조/07/{i}")