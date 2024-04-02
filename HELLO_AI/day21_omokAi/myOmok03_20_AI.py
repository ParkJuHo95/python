import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon,  QPushButton, QMessageBox
import numpy as np
from tensorflow.keras.models import load_model

form_class = uic.loadUiType("myOmok03_20_AI.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.model = load_model('20201213_202430.h5')
        self.back = QIcon("0.png")
        self.white = QIcon("1.png")
        self.black = QIcon("2.png")
        self.color = False
        self.flag_ing = True 
        # self.gibo = [
        #         {'i':0,'j':0},
        #         {'i':1,'j':0},
        #         {'i':2,'j':0},
        #         {'i':3,'j':0},
        #         {'i':4,'j':0}
        #     ]
        self.userFirst = True
        self.width = 20
        self.height = 20
        self.arr2D = [[ 0 for i in range(self.width)] for j in range(self.height)]
        # self.arr2D = [
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0, 0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0]
        # ]
        self.pb2D = []
        self.setupUi(self)
        self.pb.clicked.connect(self.reset)
        for i in range(self.width):
            line = []
            for j in range(self.height):
                    btn = QPushButton("",self)
                    btn.setIconSize(QtCore.QSize(40,40))
                    btn.setGeometry(QtCore.QRect(40*j,40*i,40,40))
                    btn.clicked.connect(self.myclick)
                    btn.setToolTip("{},{}".format(i,j))
                    line.append(btn)
            self.pb2D.append(line)
                    
        self.render()
        self.show()
        
    def myclick(self):
        if self.flag_ing != True:
            return
        # if self.userFirst == False:
        #     self.comclick(self.gibo_cnt)
        #     self.userFirst = True
             
        sender = self.sender()
        str_ij = sender.toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = 0
        
        if self.color == True:
            self.arr2D[i][j] = 1
            stone = 1
        if self.color == False:
            self.arr2D[i][j] = 2
            stone = 2
            
        up = self.getUP(i, j, stone)
        dw = self.getDW(i, j, stone)
        ri = self.getRI(i, j, stone)
        le = self.getLE(i, j, stone)
        ul = self.getUL(i, j, stone)
        ur = self.getUR(i, j, stone)
        dl = self.getDL(i, j, stone)
        dr = self.getDR(i, j, stone)
        
        self.render()
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ul + dr + 1
        d4 = ur + dl + 1

        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            if self.color == False:
                QMessageBox.about(self,"오목","흑돌승리")
            if self.color == True:
                QMessageBox.about(self,"오목","백돌승리")
            
            
            self.flag_ing = not self.flag_ing
            self.color = False
            
        self.color = not self.color
        self.comclick()
        
    def comclick(self):
        if self.flag_ing != True:
            return
        
        
        myarr = []
        for i in range(20):
            for j in range(20):
                if self.arr2D[i][j] == 2:
                    myarr.append(-1)
                else :
                    myarr.append(self.arr2D[i][j])
                    
                    
        input = np.array(myarr)
        input = np.reshape(input,(-1,20,20,1))

        output = self.model.predict(input).squeeze()
        output = output.reshape((self.height, self.width))
        output_y, output_x = np.unravel_index(np.argmax(output), output.shape)

        i = output_y
        j = output_x

        # self.arr2D[i][j] = 2
        
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = 0
        
        if self.color == True:
            self.arr2D[i][j] = 1
            stone = 1
        if self.color == False:
            self.arr2D[i][j] = 2
            stone = 2
            
        up = self.getUP(i, j, stone)
        dw = self.getDW(i, j, stone)
        ri = self.getRI(i, j, stone)
        le = self.getLE(i, j, stone)
        ul = self.getUL(i, j, stone)
        ur = self.getUR(i, j, stone)
        dl = self.getDL(i, j, stone)
        dr = self.getDR(i, j, stone)
        
        self.render()
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ul + dr + 1
        d4 = ur + dl + 1

        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            if self.color == False:
                QMessageBox.about(self,"오목","흑돌승리")
            if self.color == True:
                QMessageBox.about(self,"오목","백돌승리")
            
            
            self.flag_ing = not self.flag_ing
            self.color = False
            
        self.color = not self.color
        
            
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(self.back)
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(self.white)
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(self.black)
           
    def reset(self):
        for i in range(len(self.arr2D)):
            for j in range(len(self.arr2D[i])):
                self.arr2D[i][j] = 0
        self.render()
        self.flag_ing = True
        self.color = False
        self.gibo_cnt = 0
     
     
                
                
    def getUP(self, i, j, stone):
        count = 0
        try :
            while True:
                i -= 1
                
                if i < 0 or j < 0:
                    return count
                
                if self.arr2D[i][j]==stone:
                    count += 1
                else :
                    return count
        except :
            return count
        
    def getDW(self, i, j, stone):
        count = 0
        try :
            while True:
                i += 1
                
                if i < 0 or j < 0:
                    return count
                
                if self.arr2D[i][j]==stone:
                    count += 1
                else :
                    return count
        except :
            return count

    def getLE(self, i, j, stone):
        count = 0
        try :
            while True:
                j -= 1
                
                if i < 0 or j < 0:
                    return count
                
                if self.arr2D[i][j]==stone:
                    count += 1
                else :
                    return count
        except :
            return count
        
    def getRI(self, i, j, stone):
        count = 0
        try :
            while True:
                j += 1
                
                if i < 0 or j < 0:
                    return count
                
                if self.arr2D[i][j]==stone:
                    count += 1
                else :
                    return count
        except :
            return count

    def getDR(self, i, j, stone):
        count = 0
        try :
            while True:
                j += 1
                i += 1
                
                if i < 0 or j < 0:
                    return count
                
                if self.arr2D[i][j]==stone:
                    count += 1
                else :
                    return count
        except :
            return count

    def getDL(self, i, j, stone):
        count = 0
        try :
            while True:
                i += 1
                j -= 1
                
                if i < 0 or j < 0:
                    return count
                
                if self.arr2D[i][j]==stone:
                    count += 1
                else :
                    return count
        except :
            return count

    def getUR(self, i, j, stone):
        count = 0
        try :
            while True:
                i -= 1
                j += 1
                
                if i < 0 or j < 0:
                    return count
                
                if self.arr2D[i][j]==stone:
                    count += 1
                else :
                    return count
        except :
            return count
   
    def getUL(self, i, j, stone):
        count = 0
        try :
            while True:
                i -= 1
                j -= 1
                
                if i < 0 or j < 0:
                    return count
                
                if self.arr2D[i][j]==stone:
                    count += 1
                else :
                    return count
        except :
            return count
        
    def whoIsFirst(self):
        pass
        
                
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 