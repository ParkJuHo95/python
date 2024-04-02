import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("myqt04.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.pbFunction)

    def pbFunction(self):
        dan = self.te.toPlainText()
        intdan = int(dan)
        str1 = ""
        for i in range(1,9+1):
             # str1 += dan + " * " + str(i) + " = " + str(intdan*i)+"\n"
             str1 += f"{dan}*{i}={intdan*i}\n"
        self.pte.setPlainText(str1)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 