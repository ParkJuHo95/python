import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import json
from day13_3D.daobus import DaoBus


# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("my_daejeon_qt.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.driver = webdriver.Chrome()
        self.show()
        self.pb.clicked.connect(self.pbFunction)
        self.driver.get("http://traffic.daejeon.go.kr/bus/busInfo")
        self.dbp = DaoBus()
        
    def pbFunction(self):
        span = self.driver.find_elements(By.CSS_SELECTOR,'span[class="st_name"]')
        bus_name = self.driver.find_element(By.CSS_SELECTOR,'details[class="bus_info"]')
        first = bus_name.find_element(By.TAG_NAME,'mark').text
        last = bus_name.find_element(By.TAG_NAME,'strong').text
        bus_num = first+last
        for idx,s in enumerate(span):
            bus_id = s.text
            myparent = s.find_element(By.XPATH,'..')
            sp2 = myparent.find_element(By.CSS_SELECTOR,'span[class="st_id"]')
            bus_name = sp2.text
            ip = myparent.find_element(By.CSS_SELECTOR,'input')
            txt = ip.get_attribute("value")
            myjson = json.loads(txt);
            lat = myjson['gpsLati']
            lng = myjson['gpsLong']
            cnt = self.dbp.insert(bus_num,idx, bus_id, bus_name,lat,lng)
            print(bus_num,idx, bus_id, bus_name,lat,lng)
            
            
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 