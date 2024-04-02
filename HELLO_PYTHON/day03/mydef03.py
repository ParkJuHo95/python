from random import random
def getHollJjak():
    ranNum = random()*2
    if(ranNum > 1) : 
        return "짝"
    else : 
        return "홀"

com = getHollJjak()
print("com :",com)


