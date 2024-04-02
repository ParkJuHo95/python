import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random

form_class = uic.loadUiType("myqt05.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.pbFunction)

    def pbFunction(self):
        arr = list(range(1, 45 + 1))
        
        for i in range(100):
            rnd = int(random() * 45)
            temp = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = temp
            
        lotto = arr[0:6]
        lotto.sort()
        self.sp1.setValue(lotto[0])
        self.sp2.setValue(lotto[1])
        self.sp3.setValue(lotto[2])
        self.sp4.setValue(lotto[3])
        self.sp5.setValue(lotto[4])
        self.sp6.setValue(lotto[5])
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
