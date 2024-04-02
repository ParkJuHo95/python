import requests
from bs4 import BeautifulSoup as bs

url = "http://localhost:8888/MVVM_EMP/emp.html"
res = requests.get(url)
res.encoding='UTF-8'
soup = bs(res.text, "html.parser")
trs = soup.select('tr')

print(soup)

for idx,tr in enumerate(trs):
    if idx == 0:
        continue
    tds = tr.select('td')
    for idx,td in enumerate(tds):
        if idx%2 != 0:
            print(td.text)

