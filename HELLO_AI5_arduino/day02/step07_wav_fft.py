import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os
import cv2
from day02.step02_arr_def import muteCut


# def cutMute(arr_n,height):
#     idx_f = 0
#     while True:
#         if arr_n[idx_f]<height:
#             pass
#         else:
#             break
#         idx_f+=1
#
#     idx_f-=500
#
#
#     idx_l = len(arr_n)-1
#     while True:
#         if arr_n[idx_l]<height:
#             pass
#         else:
#             break
#         idx_l-=1
#
#     idx_l+=500
#
#     return arr_n[idx_f:idx_l]




dir = "animal_en/"

list = os.listdir(dir)

for i in list:
    files = os.listdir(f"{dir}{i}")
    for f in files:
        wavFile = f"{dir}{i}/{f}"
        y,sr = librosa.load(wavFile)
        y_trim = muteCut(y,0.01)
        t = np.arange(0, len(y_trim))
        plt.specgram(y_trim)
        plt.savefig(f"animal_en_s/{i}/{f[0:3]}.jpg")
        plt.clf()






