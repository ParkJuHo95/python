#up and down 게임
from random import random

#1~100 컴
#기회 10번


ranNum = int(random()*100)+1

count = 0;
for i in range(0,10):
    a = int(input("숫자를 맞춰보세요 > "))
    count += 1
    if a > ranNum :
        print("down")
    elif a < ranNum :
        print("up")
    else :
        print("정답입니다")
        break
    
if count>=10 :
    print("기회 끝")
