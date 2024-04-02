import requests
from bs4 import BeautifulSoup as bs

url = "http://localhost:8888/HELLO_WEB_EMP/emp_list"
res = requests.get(url)

# print(res.text)

soup = bs(res.text, "html.parser")
trs = soup.find_all('tr')

for idx,tr in enumerate(trs):
    if idx == 0:
        continue
    tds = tr.find_all('td')
    for idx,td in enumerate(tds):
        if idx == 1:
            print("이름 : ",td.text)
        if idx == 3:
            print("위치 : ",td.text)

# print(tds[1].text,tds[3].text)
# for i in list:
#     if list.index(i)>0 :
#         for j in i.select('td'):
#             print(j)