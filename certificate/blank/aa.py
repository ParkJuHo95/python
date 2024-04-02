import os
import numpy as np

filename = []
ty = []

list = os.listdir("./dependency/")
for file in list:
    a = file[0:-4]
    b = a.split("-")
    cc = []
    for idx,k in enumerate(b):
        try: 
            if b[idx+1] != None:
                cc.append(k)
        except: 
            ty.append(k)
            
    filename.append(cc)
        
        
for idx,arr in enumerate(filename):
    if len(arr) != 1:
        stri = ""
        for kk,ar in enumerate(arr):
            if kk != 0:
                stri += f"-{ar}"
            else :
                stri += f"{ar}"
        filename[idx] = stri
    else :
        filename[idx]= arr[0]

for idx,a in enumerate(filename):
    print(filename[idx])

for idx,a in enumerate(ty):
    print(ty[idx])
    
