import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from keras.models import load_model
import numpy as np

form_class = uic.loadUiType("menu_recom02.ui")[0]

class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.model = load_model('menu2.h5')
        self.labels = [
            {'name':'짜장','label':0,'arr':[1,0,0,0,0]},
            {'name':'삼겹살','label':1,'arr':[0,1,0,0,0]},
            {'name':'전복죽','label':2,'arr':[0,0,1,0,0]},
            {'name':'킹크랩','label':3,'arr':[0,0,0,1,0]},
            {'name':'라면','label':4,'arr':[0,0,0,0,1]}
        ]
        self.show()
        self.pb.clicked.connect(self.pbFunction)
    
    def getIdxByName(self,myName):
        for idx,l in enumerate(self.labels):
            if l['name'] == myName:
                return idx;
        return -1;
    
    def pbFunction(self):
        yesterday = self.le.text()
        bday = self.le_2.text()
        idx1 = self.getIdxByName(bday);
        idx2 = self.getIdxByName(yesterday);
        com = ""
        if idx1 == -1 or idx2 == -1:
            com = "데이터 로드 실패"
        else :
            pred_rf = self.model.predict(np.array([[self.labels[idx2]['arr'],self.labels[idx1]['arr']]]))
            myidx = np.argmax(pred_rf)
            
            print([self.labels[idx2]['arr'],self.labels[idx1]['arr']])
            print(myidx)
            com = self.labels[myidx]['name']

        self.le_recom.setText(com)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
