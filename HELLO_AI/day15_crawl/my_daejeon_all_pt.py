import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from flask import json
from day15_crawl.dao_bus_path import DaoBusPath


form_class = uic.loadUiType("my_daejeon_all_pt.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.driver = webdriver.Firefox()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.pb_all.clicked.connect(self.myBus_All)
        self.pb_macro.clicked.connect(self.macro)
        self.dbp = DaoBusPath()
        self.cnt = 0
        self.bp_names = []
        self.lis = []
        self.show()
        self.driver.get("http://traffic.daejeon.go.kr/bus/busInfo")
        
    def myclick(self) :
        spans = self.driver.find_elements(By.CSS_SELECTOR,"span[class='st_name']")
        for idx,s in enumerate(spans):
            myparent = s.find_element(By.XPATH, '..')            
            sp2 = myparent.find_elements(By.CSS_SELECTOR,"span[class='st_id']")
            ip = myparent.find_elements(By.CSS_SELECTOR, "input")[0]
            txt = ip.get_attribute("value")
            myjson = json.loads(txt)
            lat = myjson['gpsLati']
            lng = myjson['gpsLong']
            bus_name = s.text
            bus_id = sp2[0].text
            cnt = self.dbp.insert(self.bp_names[self.cnt], idx, bus_id, bus_name, lat, lng)
            print(f"{idx}, 정류장명 : {bus_name}, 정류장ID : {bus_id}, 위도 : {lat}, 경도 : {lng}")
        self.cnt +=1
        # self.driver.get("http://traffic.daejeon.go.kr/bus/busInfo")
        self.driver.back()

    def myBus_All(self):
        ul = self.driver.find_element(By.CSS_SELECTOR,"ul[class=route]")
        marks = ul.find_elements(By.TAG_NAME, "mark")
        strongs = ul.find_elements(By.TAG_NAME, "strong")
        self.bp_names.clear()
        for idx,mark in enumerate(marks):
            bp_name = f"{mark.text}{strongs[idx].text}"
            self.bp_names.append(bp_name)
            print(idx,bp_name)
        print(self.bp_names)
        
    def macro(self):
        self.myBus_All()
        
        for idx,bp_name in enumerate(self.bp_names):
            ul = self.driver.find_element(By.CLASS_NAME,"route")
            lis = ul.find_elements(By.TAG_NAME, "li")
            lis[self.cnt].click()
            time.sleep(2)
            self.myclick()
            time.sleep(2)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()