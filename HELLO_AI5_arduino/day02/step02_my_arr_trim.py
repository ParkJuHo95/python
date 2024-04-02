import numpy as np
import array

arr = [ 0,0,0,0,0,0,5,6,7,8,5,4,0,0,0,0,0]

# myNp = np.array(arr)
# myNp = np.trim_zeros(myNp)
# myNp = np.concatenate(([0],myNp,[0]))
# myNp = list(myNp)
# print(myNp)

fi = 0 
fe = len(arr) -1

while True:
    if arr[fi] > 2:
        break
    else :
        fi += 1
    
print(fi)

while True:
    if arr[fe] > 2:
        break
    else :
        fe -= 1

print(fe)

arrCut = arr[fi-1:fe+2]
print(arrCut)

