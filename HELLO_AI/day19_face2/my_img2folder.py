import cv2
import os

file_list = os.listdir("./img")
file_list_mp4 = [file for file in file_list if file.endswith(".mp4")]
for idx,list in enumerate(file_list_mp4):
    video = cv2.VideoCapture(f'img/{list}')
    frame_count = 0
    idx = str(idx).zfill(2)
    os.mkdir(f"./pre01/{idx}")      #폴더가 있을경우 주석처리해주고 진행

    while(video.isOpened()) :
        ret, frame = video.read()
        if ret :
            frame_count += 1
            cv2.imwrite(f'pre01/{idx}/{frame_count}.png',frame)
        else :
            break