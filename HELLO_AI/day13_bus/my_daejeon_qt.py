import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


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

    def pbFunction(self):
        first = self.driver.find_element(By.CSS_SELECTOR,'div[class=rtList]')
        stops = first.find_elements(By.TAG_NAME,'li')
        
        for idx,s in enumerate(stops):
                sta_name = s.find_element(By.CLASS_NAME,'st_name').text
                sta_id = s.find_element(By.CLASS_NAME,'st_id').text
                print(idx,sta_name,sta_id)
            
            
            
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 