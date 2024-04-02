import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


form_class = uic.loadUiType("click.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.driver = webdriver.Firefox()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
        self.driver.get("https://namu.wiki/w/%EA%B5%AD%EA%B0%80%EA%B8%B0%EC%88%A0%EC%9E%90%EA%B2%A9#s-3")
        self.index = []
        self.innerIndex = []
        
    def myclick(self) :
        divs = self.driver.find_elements(By.CLASS_NAME,'JOWKtQdm')
        
        nowstart = False;
        
        for div in divs:
            trs = div.find_elements(By.TAG_NAME, 'tr')
            for idx,tr in enumerate(trs):
                if idx == 0:
                    td = tr.find_element(By.TAG_NAME,'td').text
                    if td == "2. 경영/회계/사무":
                        nowstart = True
                    if nowstart == True:
                        td = f"{td}"
                        if len(td) != 0:
                            print(td)
                            self.index.append(td)
                
                if idx == 1:
                    continue
                
                if nowstart == True and idx != 0 and idx != 1 :
                    tds = tr.find_elements(By.TAG_NAME,'td')
                    for td in tds:
                        td = f"{td.text}"
                        if len(td) != 0:
                            print(td)
                            self.innerIndex.append(td)
        
        print(self.index)
        print(self.innerIndex)
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()