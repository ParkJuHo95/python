import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt06.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.pbFunction)

    def pbFunction(self):
        mine = self.le_mine.text()
        rnd = random()
        com = ""
        if rnd > 0.5:
            com = "짝"
        else :
            com = "홀"
        self.le_com.setText(com)
        result = ""
        if com == mine:
            result = "승리"
        else :
            result = "패배"
        self.le_result.setText(result)
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
