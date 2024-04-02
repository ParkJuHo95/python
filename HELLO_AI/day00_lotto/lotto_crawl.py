import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from flask import json
from day15_crawl.dao_bus_path import DaoBusPath
import numpy as np


form_class = uic.loadUiType("lotto.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.driver = webdriver.Chrome()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.cnt = 1
        self.lotto = []
        self.show()
        self.driver.get("https://www.dhlottery.co.kr/gameResult.do?method=statOddEven&sortOrder=DESC&startPage=1&endPage=10&currentPage=1")
        
    def myclick(self) :
        for i in range(1,110):
            games = self.driver.find_elements(By.CLASS_NAME ,"ta_left")
            arr = []
            for idx,game in enumerate(games):
                balls = game.find_elements(By.CSS_SELECTOR, 'span')
                for ball in balls:
                    arr.append(ball.text)
                if (idx+1)%2 == 0:
                    arr.sort()
                    my_arr = arr.copy()
                    self.lotto.append(my_arr)
                    arr.clear()
            self.cnt += 1
            self.driver.get(f"https://www.dhlottery.co.kr/gameResult.do?method=statOddEven&sortOrder=DESC&startPage=1&endPage=10&currentPage={self.cnt}")
        self.arr2numpy()    
        
    def arr2numpy(self):
        my_num = np.array(self.lotto)
        np.save("lotto",my_num)
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()