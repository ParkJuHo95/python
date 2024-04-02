import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from keras.models import load_model
import numpy as np

form_class = uic.loadUiType("gawi_ai_qt.ui")[0]

class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.model = load_model('gawi.h5')
        self.show()
        self.pb.clicked.connect(self.pbFunction)

    def pbFunction(self):
        my = self.le_mine.text()
        pred_rf = None
        if my == "가위" :
            pred_rf = self.model.predict(np.array([[1,0,0]]))
        elif my == "바위" :
            pred_rf = self.model.predict(np.array([[0,1,0]]))
        else : 
            pred_rf = self.model.predict(np.array([[0,0,1]]))

        myidx = np.argmax(pred_rf)

        com = ""
        if myidx == 0 :
            com = "가위"
        elif myidx == 1 :
            com = "바위"
        else :
            com = "보"
            
        self.le_com.setText(com)
        
        result = ""
        
        if com == "가위" and my == "가위" : result = "비김"
        if com == "가위" and my == "바위" : result = "이김"
        if com == "가위" and my == "보" : result = "짐"
        
        if com == "바위" and my == "가위" : result = "짐"
        if com == "바위" and my == "바위" : result = "비김"
        if com == "바위" and my == "보" : result = "이김"
        
        if com == "보" and my == "가위" : result = "이김"
        if com == "보" and my == "바위" : result = "짐"
        if com == "보" and my == "보" : result = "비김"
        
        self.le_result.setText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
