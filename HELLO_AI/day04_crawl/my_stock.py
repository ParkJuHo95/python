import requests
from bs4 import BeautifulSoup as bs
import time
from day04_crawl.daoStock import DaoStock
dao  = DaoStock()
cnt = 0
dataCnt = 0
while cnt<400:
    url = "https://stock.mk.co.kr/domestic/all_stocks?type=kospi&status=industry"
    res = requests.get(url)
    
    soup = bs(res.text,"html.parser")
    list = soup.select(".st_name")
    ymd = time.strftime('%Y%m%d_%H%M')
    for idx1,i in enumerate(list):
        row = i.parent
        st_name = row.select_one('.st_name')
        st_price = row.select_one('.st_price').text
        price = st_price.replace(",","")
        href = st_name.select_one('a').attrs['href']
        s_name = row.select_one('.st_name').text
        s_code = href.split("/")[3]
        
        dao.insert(s_name, price, s_code, ymd)
        dataCnt += 1
    cnt += 1
    print(f"입력 데이터 개수 : {dataCnt}")
    time.sleep(60)
    
    
