import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from keras.models import load_model
import numpy as np

form_class = uic.loadUiType("menu_qt.ui")[0]

class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.model = load_model('menu.h5')
        self.show()
        self.pb.clicked.connect(self.pbFunction)
    
    def pbFunction(self):
        myName = self.le_mine.text()
        com = ""
        if myName == "짜장" :
            pred_rf = self.model.predict(np.array([[1,0,0,0,0]]))
        elif myName == "삼겹살" :
            pred_rf = self.model.predict(np.array([[0,1,0,0,0]]))
        elif myName == "전복죽" :
            pred_rf = self.model.predict(np.array([[0,0,1,0,0]]))
        elif myName == "킹크랩" :
            pred_rf = self.model.predict(np.array([[0,0,0,1,0]]))
        else : 
            pred_rf = self.model.predict(np.array([[0,0,0,0,1]]))
        
        myidx = np.argmax(pred_rf)
        
        if myidx == 0 :
            com = "짜장"
        elif myidx == 1 :
            com = "삼겹살"
        elif myidx == 2 :
            com = "전복죽"
        elif myidx == 3 :
            com = "킹크랩"
        else :
            com = "라면"
        self.le_com.setText(com)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
