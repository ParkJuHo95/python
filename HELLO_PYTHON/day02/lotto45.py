from random import random

arr = list(range(1, 45 + 1))
a = input("게임 수를 입력하세요")
for i in range(int(a)):
    for i in range(100):
        rnd = int(random() * 45)
        temp = arr[0]
        arr[0] = arr[rnd]
        arr[rnd] = temp

    # lotto = []
    # for i in range(0,6) :
    #     lotto.append(arr[i])
    #

    lotto1 = arr[0:6]

    lotto1.sort()
    # print(lotto)
    print(lotto1)

    #####################################
# arr = [
#     1,2,3,4,5,6,7,8,9,10,
#     11,12,13,14,15,16,17,18,19,20,
#     21,22,23,24,25,26,27,28,29,30,
#     31,32,33,34,35,36,37,38,39,40,
#     41,42,43,44,45
# ]

