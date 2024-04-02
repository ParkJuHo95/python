import os
import shutil

dir = "gana/"
arr_eng = [
        "GA","NA","DA","RA","MA",
        "BA","SA","AA","JA","CA"
    ]

files= os.listdir(dir)
for file in files:
    spell = ""
    if file[0:1] == "가":
        spell = arr_eng[0]
    elif file[0:1] == "나":
        spell = arr_eng[1]
    elif file[0:1] == "다":
        spell = arr_eng[2]
    elif file[0:1] == "라":
        spell = arr_eng[3]
    elif file[0:1] == "마":
        spell = arr_eng[4]
    elif file[0:1] == "바":
        spell = arr_eng[5]
    elif file[0:1] == "사":
        spell = arr_eng[6]
    elif file[0:1] == "아":
        spell = arr_eng[7]
    elif file[0:1] == "자":
        spell = arr_eng[8]
    else :
        spell = arr_eng[9]
    file_name = file.replace(file[0:1], spell)
    # print(file_name)
    # os.rename(dir+file,dir+file_name)
    destination = "gana_en/"+file_name
    shutil.copyfile("gana/"+file, destination)