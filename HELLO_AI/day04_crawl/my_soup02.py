import requests
from bs4 import BeautifulSoup as bs

url = "http://localhost:8888/HELLO_WEB_EMP/emp_list"
res = requests.get(url)

soup = bs(res.text, "html.parser")
trs = soup.select('tr')

for idx,tr in enumerate(trs):
    if idx == 0:
        continue
    tds = tr.select('td')
    for idx,td in enumerate(tds):
        if idx%2 != 0:
            print(td.text)
