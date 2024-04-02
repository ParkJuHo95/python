import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
import numpy as np
from keras.models import load_model


form_class = uic.loadUiType("holl_ai_qt.ui")[0]

class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.model = load_model('holl.h5')
        self.show()
        self.pb.clicked.connect(self.pbFunction)

    def pbFunction(self):
        pred_rf = None
        mine = self.le_mine.text()
        
        if mine=="홀":
            pred_rf = self.model.predict(np.array([[1,0]]))
        else:
            pred_rf = self.model.predict(np.array([[0,1]]))
            
        myidx = np.argmax(pred_rf)
        
        if myidx == 1:
            com="짝"
        if myidx == 0:
            com="홀"
        self.le_com.setText(com)
        
        result = ""
        if com == mine:
            result = "승리"
        else :
            result = "패배"
        self.le_result.setText(result)
            
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
