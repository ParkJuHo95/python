import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from random import random
from PyQt5.Qt import QPushButton

form_class = uic.loadUiType("myqt09_1.ui")[0]


class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb0.clicked.connect(self.pbFunction)
        self.pb1.clicked.connect(self.pbFunction)
        self.pb2.clicked.connect(self.pbFunction)
        self.pb3.clicked.connect(self.pbFunction)
        self.pb4.clicked.connect(self.pbFunction)
        self.pb5.clicked.connect(self.pbFunction)
        self.pb6.clicked.connect(self.pbFunction)
        self.pb7.clicked.connect(self.pbFunction)
        self.pb8.clicked.connect(self.pbFunction)
        self.pb9.clicked.connect(self.pbFunction)
        self.pb_call.clicked.connect(self.calling)

    def pbFunction(self):
        str_new = self.sender().text()
        str_old = self.le.text()
        
        self.le.setText(str_old+str_new)
        
    def calling(self):
        str_tel = self.le.text()
        QMessageBox.about(self,'Calling','Calling...\n'+str_tel)
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
