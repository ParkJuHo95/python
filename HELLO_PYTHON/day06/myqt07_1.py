import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt07_1.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.pbFunction)

    def getStar(self, cnt):
        ret = ""
        for i in range(cnt):
            ret += "*"
        ret += "\n"
        return ret
    
    def getStar1(self,cnt):
        ret = ""
        ret += '*' * cnt + "\n"
        return ret

    def pbFunction(self):
        a = self.sb_first.value();
        b = self.sb_last.value();
        
        txt = ""
        for i in range(a, b+1):
            txt += self.getStar1(i)
        
        self.te.setText(txt)

        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
