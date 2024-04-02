import numpy as np

arr = [5,4,3,2,1]
numarr = np.array(arr)
a = np.sort(numarr)[::-1]
arr[0] = 3
print(arr)
print(a)
print(a[0])
