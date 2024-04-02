import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from keras.models import load_model
import numpy as np

form_class = uic.loadUiType("menu_qt2.ui")[0]

class MainClass(QMainWindow, form_class):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.model = load_model('menu.h5')
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
        myName = self.le.text()
        idx = self.getIdxByName(myName);
        com = ""
        if idx == -1:
            com = "데이터 로드 실패"
        else :
            pred_rf = self.model.predict(np.array([self.labels[idx]['arr']]))
            myidx = np.argmax(pred_rf)
            com = self.labels[myidx]['name']
        # if myName == "짜장" :
        #     pred_rf = self.model.predict(np.array([[1,0,0,0,0]]))
        # elif myName == "삼겹살" :
        #     pred_rf = self.model.predict(np.array([[0,1,0,0,0]]))
        # elif myName == "전복죽" :
        #     pred_rf = self.model.predict(np.array([[0,0,1,0,0]]))
        # elif myName == "킹크랩" :
        #     pred_rf = self.model.predict(np.array([[0,0,0,1,0]]))
        # else : 
        #     pred_rf = self.model.predict(np.array([[0,0,0,0,1]]))

        # myidx = np.argmax(pred_rf)

        
        # if myidx == 0 :
        #     com = "짜장"
        # elif myidx == 1 :
        #     com = "삼겹살"
        # elif myidx == 2 :
        #     com = "전복죽"
        # elif myidx == 3 :
        #     com = "킹크랩"
        # else :
        #     com = "라면"
        self.le_recom.setText(com)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 
