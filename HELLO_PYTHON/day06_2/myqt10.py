import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QLabel

form_class = uic.loadUiType("myqt10.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.lbl2D = [10][10]
        for i in range(10):
            for j in range(10):
                self.lbl = QLabel
                # self.lbl.setFixedWidth(40)
                # self.lbl.setFixedHeight(40)
                self.lbl.setBaseSize(40, 40)
                self.lbl.set
                self.lbl2D[i][j] = self.lbl
            
        
        
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass()
    app.exec_() 
