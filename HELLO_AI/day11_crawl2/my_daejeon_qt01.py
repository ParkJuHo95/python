import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from flask import json


form_class = uic.loadUiType("my_daejeon_qt01.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.driver = webdriver.Firefox()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
        self.driver.get("http://traffic.daejeon.go.kr/bus/busInfo")
        
    def myclick(self) :
        #root > div.mapWrap > aside > div > article > div > ul > li:nth-child(1) > span.st_name
        spans = self.driver.find_elements(By.CSS_SELECTOR,"span[class='st_name']")
        
        for idx,s in enumerate(spans):
            # 부모 element를 찾기위한 코드
            myparent = s.find_element(By.XPATH, '..')            
            
            sp2 = myparent.find_elements(By.CSS_SELECTOR,"span[class='st_id']")
            
            # input 요소 찾기
            ip = myparent.find_elements(By.CSS_SELECTOR, "input")[0]
    
            # Hidden input 요소의 값을 가져오기
            txt = ip.get_attribute("value")
            
            # print(value)
            
            # JSON 형식의 문자열을 파이썬 객체로 변환
            myjson = json.loads(txt)
            
            lat = myjson['gpsLati']
            lng = myjson['gpsLong']
            
            print(lat,lng)
            
            bus_name = s.text
            bus_id = sp2[0].text
            
            print(f"{idx}, 정류장명 : {bus_name}, 정류장ID : {bus_id}, 위도 : {lat}, 경도 : {lng}")

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()