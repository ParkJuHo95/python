import sys

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from qtawesome import icon
from PyQt5.Qt import QIcon, QWhatsThisClickedEvent


# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myOmok01.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.white = QIcon("1.png")
        self.black = QIcon("2.png")
        
        self.setupUi(self)
        
        self.pb.clicked.connect(self.pbFunction)
        self.lbl.mousePressEvent = self.lblFunction
        
        self.show()

    def pbFunction(self):
        # self.pb.setStyleSheet("background-image : url(1.png);") 
        self.pb.setIcon(QtGui.QIcon("1.png"))
        
    def lblFunction(self):
        self.lbl.setPixmap(QtGui.QPixmap("1.png"))
    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 