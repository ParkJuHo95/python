#홀(1)/짝(0)을 선택하시오
from random import random
a = int(input("홀(1)짝(0)을 선택하시오 >"))
b = int(random()*2)

if (a==b) :
    print('승리')
else :
    print('패배')
    
print(f"컴퓨터:{b} 나:{a}")



my = input("홀/짝을 선택하시오 >")
if my== "짝" :
    c = 0
else :
    c = 1
if (c==b) :
    print('승리')
else :
    print('패배')
    
print(f"컴퓨터:{b} 나:{c}")