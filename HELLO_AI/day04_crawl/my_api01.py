import os
import sys
import urllib.request
from bs4 import BeautifulSoup as bs

client_id = "IOYV_ttrcCuuBMLbv0ta"
client_secret = "WLjFpA8DVT"
encText = urllib.parse.quote("아이유")
url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

response_body = response.read()
txt = response_body.decode('utf-8')

soup = bs(txt,"xml")

items = soup.find_all("item")
# for idx,i in enumerate(items):
#     if idx == 0:
#         print(i.find('title').text)
#         print(i.find('link'))
        # for idx, j in enumerate(i):
for i in items:
    print(i.find('title').text)
    print(i.find('link').text)