import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt08.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.pbFunction)
        self.com = int(random()*100)+1
        

    def pbFunction(self):
        mine = self.le.text()
        myNum = int(mine)
        answer = ""
        if self.com > myNum:
            answer = mine + " UP"
        elif self.com < myNum:
            answer = mine + " DOWN"
        else :
            answer = mine + " 정답!"
            self.com = int(random()*100)+1
            
        self.pte.appendPlainText(answer)
        self.le.setText("")
            
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
