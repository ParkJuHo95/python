import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt07.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.pbFunction)

    def pbFunction(self):
        first = self.sb_first.value()
        last = self.sb_last.value()
        str1 = ""
        for i in range(last-first+1):
            for j in range(first+i):
                str1 += "*"
            str1 +="\n"
        
        self.te.setText(str1)
            
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
