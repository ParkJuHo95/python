import requests
import time
from bs4 import BeautifulSoup as bs
from day04_crawl.daoStock import DaoStock
import datetime

print('1')
time.sleep(2)
dao  = DaoStock()
print('2')
time.sleep(2)
cnt = 0
dataCnt = 0
url = "https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry"

now = datetime.datetime.now()
ymd = now.strftime("%Y%m%d_%H%M")
print('3')
time.sleep(2)
res = requests.get(url)

soup = bs(res.text,"html.parser")

names = soup.select(".st_name")
for idx,n in enumerate(names):
    s_name = n.text.strip()
    s_code = n.select("a")[0]['href'].split("/")[3]
    price = n.parent.select(".price")[0].text.replace(",","")
    dao.insert(s_name, price, s_code, ymd)

    