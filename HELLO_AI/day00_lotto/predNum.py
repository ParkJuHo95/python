import numpy as np
import math
from random import random

oldNums = np.load("lotto.npy")
print(oldNums)
newNums = []
arr = []
for k in range(5):
    for idx in range(6):
        sum = 0
        for i in oldNums:
            sum += int(i[idx])
        result = sum/len(oldNums)
        if k == 0:
            result = round(result)
        elif k == 1:
            result = math.ceil(result)
        elif k == 2:
            result = math.floor(result)
        elif k == 3:
            result = (round(result+(random()*45+1))) %45
        else :
            result = (round(result)*2)%45
        arr.append(result)
    my_arr = arr.copy()
    arr.clear()
    my_arr.sort()
    newNums.append(my_arr)

print(newNums)