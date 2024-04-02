#가위 바위 보
from random import random
import numpy as np
from keras.models import load_model


model = load_model('gawi.h5')
my = input("가위/바위/보를 선택하세요(잘못입력하면 보) > ")

com = ""

pred_rf = None

if my == "가위" :
    pred_rf = model.predict(np.array([[1,0,0]]))
elif my == "바위" :
    pred_rf = model.predict(np.array([[0,1,0]]))
else : 
    pred_rf = model.predict(np.array([[0,0,1]]))

myidx = np.argmax(pred_rf)

if myidx == 0 :
    com = "가위"
elif myidx == 1 :
    com = "바위"
else :
    com = "보"
    
if com == "가위" and my == "가위" : result = "비김"
if com == "가위" and my == "바위" : result = "이김"
if com == "가위" and my == "보" : result = "짐"

if com == "바위" and my == "가위" : result = "짐"
if com == "바위" and my == "바위" : result = "비김"
if com == "바위" and my == "보" : result = "이김"

if com == "보" and my == "가위" : result = "이김"
if com == "보" and my == "바위" : result = "짐"
if com == "보" and my == "보" : result = "비김"
    
print(f"나:{my}")
print(f"컴퓨터:{com}")
print(f"결과:{result}")
    