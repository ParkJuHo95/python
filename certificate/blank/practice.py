import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("practice.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.
        self.show()
        self.btn1.clicked.connect(self.btn1Function)
    #
    # def pbFunction(self):
    #     self.lbl.setText("Good Evening")
    def btn1Function(self):
        self.progressBar.st
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 