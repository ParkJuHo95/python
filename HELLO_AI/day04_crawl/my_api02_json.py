import os
import sys
import urllib.request
import json

client_id = "IOYV_ttrcCuuBMLbv0ta"
client_secret = "WLjFpA8DVT"
encText = urllib.parse.quote("아이유")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
response_body = response.read()
txt = response_body.decode('utf-8')
json_txt = json.loads(txt)
for i in json_txt["items"]:
    print(i['title'])
    print(i['link'])
