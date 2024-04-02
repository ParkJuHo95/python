import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from random import random
from PyQt5.Qt import QPlainTextEdit

form_class = uic.loadUiType("myqt08_1.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.pbFunction)
        self.com = 0;
        self.setCom()
        
    def setCom(self):
        self.com = int(random()*99)+1
        print("com : " ,self.com)
    
    def pbFunction(self):
        mine = self.le.text()
        imine = int(mine)
        str_new = ""
        if self.com > imine :
            str_new = mine + " UP\n"
        elif self.com < imine :
            str_new = mine + " DOWN\n"
        else :
            str_new = mine + " Answer\n"
            QMessageBox.about(self,'UPDOWN',mine + '정답입니다')
             
             
        str_old = self.pte.toPlainText()
        self.le.setText("")
        self.pte.setPlainText(str_old + str_new)
        
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
