import sys

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPushButton


# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myOmok01_1.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.back = QIcon("0.png")
        self.white = QIcon("1.png")
        self.black = QIcon("2.png")
        
        self.setupUi(self)
        
        self.pb.clicked.connect(self.pbFunction)
        self.lbl.mousePressEvent = self.lblFunction
        
        self.show()

    def pbFunction(self):
        self.pb.setIcon(QtGui.QIcon("1.png"))
        
    def backgroundSetting(self):
        btn = QPushButton("Button 1", self)
        btn.resize(btn.sizeHint()) # btn의 크기 조정
        btn.setToolTip("Button Application <br><b>made by Koo</b>") # btn 위에 커서를 놓을 경우 Tip을 보여줌
        btn.move(10, 10) # btn의 위치를 조정
        
        self.resize(400, 500) # App 인스턴스의 크기를 조정
        self.show() # App을 띄움
    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 