import numpy as np
import math
from random import random
from selenium.webdriver.common import by

nums = np.load("lotto.npy")

# print(np.unique(nums,return_counts=True))

unique, counts = np.unique(nums, return_counts=True)
# print(np.asarray((unique, counts)).T)
arr  = np.asarray((unique, counts)).T
sorted_indices = np.argsort(arr[:, 1].astype(int))[::-1]

# 정렬된 인덱스를 사용하여 배열을 재정렬
sorted_arr = arr[sorted_indices]

# 정렬된 배열 출력
print(sorted_arr)