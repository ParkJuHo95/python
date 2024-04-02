import requests
from bs4 import BeautifulSoup as bs
import datetime
from daoStock import DaoStock

dao  = DaoStock()
cnt = 0
dataCnt = 0
url = "https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry"

now = datetime.datetime.now()
ymd = now.strftime("%Y%m%d_%H%M")
res = requests.get(url)

soup = bs(res.text,"html.parser")

names = soup.select(".st_name")
for idx,n in enumerate(names):
    s_name = n.text.strip()
    s_code = n.select("a")[0]['href'].split("/")[3]
    price = n.parent.select(".price")[0].text.replace(",","")
    dao.insert(s_name, price, s_code, ymd)

    