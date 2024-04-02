import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myseleniumqt01.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.driver = webdriver.Chrome()
        self.show()
        self.pb.clicked.connect(self.pbFunction)
        self.driver.get("https://map.kakao.com/")

    def pbFunction(self):
        stops = self.driver.find_elements(By.CSS_SELECTOR,'strong[class=busstop]')
        for idx,s in enumerate(stops):
            print(idx,s.text)
            
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 