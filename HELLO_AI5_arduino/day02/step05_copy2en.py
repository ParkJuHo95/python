import shutil
import os

list = os.listdir("animal/")

for idx,name in enumerate(list):
    tag = chr(idx+65)
    wavfiles = os.listdir(f"animal/{name}")
    ind = 0
    for k,wav in enumerate(wavfiles):
        if k%10 == 0 and k != 0:
            ind += 1
        shutil.copy(f"animal/{name}/{wav}", f"animal_en/{ind}/{tag}{wav}")