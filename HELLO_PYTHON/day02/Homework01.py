#가위 바위 보
from random import random

my = input("가위/바위/보를 선택하세요(잘못입력하면 보) > ")
myNum = 0;
comNum = int(random()*3)

com = ""

if comNum == 0 :
    com = "가위"
elif comNum == 1 :
    com = "바위"
else :
    com = "보"


if my == "가위" :
    myNum = 0
elif my == "바위" :
    myNum = 1
else : 
    myNum = 2
    

if myNum-comNum == -2 or myNum-comNum == 1:
    print("승리")
elif myNum-comNum == 0 :
    print("비김")
else :
    print("패배")
    
print(f"나:{my}")
print(f"컴퓨터:{com}")
    