import numpy as np
from keras.utils import np_utils
from google.protobuf.text_format import ParseInteger
from myRecom.myRecommend import myRecommend
age = [
    {'label':'0','value':'20'},
    {'label':'1','value':'30'},
    {'label':'2','value':'40'},
    {'label':'3','value':'50'},
    {'label':'4','value':'60'}
]

team = [
    {'label':'0','value':'교육팀'},
    {'label':'1','value':'인사팀'},
    {'label':'2','value':'회계팀'},
    {'label':'3','value':'시설관리팀'},
    {'label':'4','value':'구매팀'},
    {'label':'5','value':'법무팀'},
    {'label':'6','value':'제품기획팀'},
    {'label':'7','value':'제품마케팅팀'},
    {'label':'8','value':'영업1팀'},
    {'label':'9','value':'영업2팀'}
]



de = myRecommend()
# result = de.selectEMP_CER_List()
result= de.selectDetails('2021-00020','dreaminfosystem')
print(result)
my = f"{result[0]}"
myTeam = f"{result[1]}"
myage = f"{my[:-1]}{0}"
yLabel = ParseInteger(result[2])
yt = np.array([], int)
yt = np.append(yt,yLabel)
print(myage)
ageLength = len(age)
ageLabel = '' 
teamLength = len(team)
teamLabel = ''
for i in age:
    if i['value']==myage:
        ageLabel=i['label']

for i in team:
    if i['value']==myTeam:
        teamLabel = i['label']


x1 = np_utils.to_categorical(ageLabel,ageLength, int)
x2 = np_utils.to_categorical(teamLabel,teamLength, int)
xt = np.append(x1,x2)
# print(xt,yt)
