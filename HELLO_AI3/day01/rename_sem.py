import os
import shutil

dir = "gana/"
arr_eng = [
        "GA","NA","DA","RA","MA",
        "BA","SA","AA","JA","CA"
    ]

files= os.listdir(dir)
for file in files:
    file_name = file.replace("가",arr_eng[0])
    file_name = file_name.replace("나",arr_eng[1])
    file_name = file_name.replace("다",arr_eng[2])
    file_name = file_name.replace("라",arr_eng[3])
    file_name = file_name.replace("마",arr_eng[4])
    file_name = file_name.replace("바",arr_eng[5])
    file_name = file_name.replace("사",arr_eng[6])
    file_name = file_name.replace("아",arr_eng[7])
    file_name = file_name.replace("자",arr_eng[8])
    file_name = file_name.replace("차",arr_eng[9])
    # print(file_name)
    # os.rename(dir+file,dir+file_name)
    # destination = "gana_en/"+file_name
    # shutil.copyfile("gana/"+file, destination)
    print(file,file_name)