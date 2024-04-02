import tensorflow as tf
import numpy as np
from keras.models import load_model


model = load_model('holl.h5')

mine = input("홀/짝을 선택하시오")

pred_rf = None
if mine=="홀":
    pred_rf = model.predict(np.array([[1,0]]))
else:
    pred_rf = model.predict(np.array([[0,1]]))

myidx = np.argmax(pred_rf)

if myidx == 1:
    com="짝"
if myidx == 0:
    com="홀"

if com == mine:
    result = "이김"
else :
    result = "짐"
    
print("나",mine)
print("컴",com)
print("결과",result)