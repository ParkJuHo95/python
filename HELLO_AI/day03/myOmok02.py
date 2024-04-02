import sys

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from qtawesome import icon
from PyQt5.Qt import QIcon,  QPushButton, QMessageBox


# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("myOmok02.ui")[0]

# 프로그램 메인을 담당하는 Class 선언
class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.back = QIcon("0.png")
        self.white = QIcon("1.png")
        self.black = QIcon("2.png")
        self.color = False
        self.flag_ing = True 
        # self.arr = [[0,0,0,0,0, 0,0,0,0,0],
        #             [0,0,0,0,0, 0,0,0,0,0],
        #             [0,0,0,0,0, 0,0,0,0,0],
        #             [0,0,0,0,0, 0,0,0,0,0],
        #             [0,0,0,0,0, 0,0,0,0,0],
        #
        #             [0,0,0,0,0, 0,0,0,0,0],
        #             [0,0,0,0,0, 0,0,0,0,0],
        #             [0,0,0,0,0, 0,0,0,0,0],
        #             [0,0,0,0,0, 0,0,0,0,0],
        #             [0,0,0,0,0, 0,0,0,0,0]]
        self.arr = [[ 0 for i in range(10)] for j in range(10)]
        self.btns = [[ QPushButton for i in range(10)] for j in range(10)]
        self.setupUi(self)
        self.pb.clicked.connect(self.reset)
        
                
        for i in range(10):
            for j in range(10):
                    btn = QPushButton("",self)
                    # btn.setIcon(self.back)
                    btn.setIconSize(QtCore.QSize(40,40))
                    btn.setGeometry(QtCore.QRect(40*j,40*i,40,40))
                    btn.clicked.connect(self.myclick)
                    btn.setToolTip("{},{}".format(i,j))
                    self.btns[i][j] = btn
                    
        self.render()
        self.show()
        
        

    def myclick(self):
        if self.flag_ing != True:
            return
        
        sender = self.sender()
        point = self.find_index_2d(sender)
        x = point[0]
        y = point[1]
        stone = 0
        if self.arr[x][y] != 0:
            return
        
        if self.color == True:
            self.arr[x][y] = 1
            stone = 1
        else :
            self.arr[x][y] = 2
            stone = 2
        
        winner = "";
        if self.color == False:
            winner = "흑"
        else :
            winner = "백 "
            
        self.color = not self.color
        
        up = self.getUP(x, y, stone)
        dw = self.getDW(x, y, stone)
        ri = self.getRI(x, y, stone)
        le = self.getLE(x, y, stone)
        ul = self.getUL(x, y, stone)
        ur = self.getUR(x, y, stone)
        dl = self.getDL(x, y, stone)
        dr = self.getDR(x, y, stone)
        
        self.render()
        
        d1 = up + dw + 1
        d2 = ri + le + 1
        d3 = ul + dr + 1
        d4 = ur + dl + 1
        print(f"d1 = {d1}")
        print(f"d2 = {d2}")
        print(f"d3 = {d3}")
        print(f"d4 = {d4}")
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            print('승자 : '+ winner)
            self.flag_ing = not self.flag_ing
            
    
    def render(self):
        for i, row in enumerate(self.arr):
            for j, value in enumerate(row):
                if value == 0:
                    self.btns[i][j].setIcon(self.back)
                elif value == 1:
                    self.btns[i][j].setIcon(self.white)
                else:
                    self.btns[i][j].setIcon(self.black)
           
                   
    def find_index_2d(self,target_value):
        for i in range(len(self.btns)):
            for j in range(len(self.btns[i])):
                if self.btns[i][j] == target_value:
                    return [i, j]
        return None        
    
    def reset(self):
        for i, row in enumerate(self.arr):
            for j, values in enumerate(row):
                self.arr[i][j] = 0
                self.render()
        self.color = False
                
                
    def getUP(self, x, y, stone):
        count = 0
        flag = True
        while flag:
            x-=1
            try :
                if stone == self.arr[x][y]:
                    count += 1
                else :
                    return count
            except :
                flag = False
        return count
    
    def getDW(self, x, y, stone):
        count = 0
        flag = True
        while flag:
            x+=1
            try :
                if stone == self.arr[x][y]:
                    count += 1
                else :
                    return count
            except :
                flag = False
        return count    
            
    def getRI(self, x, y, stone):
        count = 0
        flag = True
        while flag:
            y+=1
            try :
                if stone == self.arr[x][y]:
                    count += 1
                else :
                    return count
            except :
                flag = False
        return count
    
    def getLE(self, x, y, stone):
        count = 0
        flag = True
        while flag:
            y-=1
            try :
                if stone == self.arr[x][y]:
                    count += 1
                else :
                    return count
            except :
                flag = False
        return count        
                
    def getUL(self, x, y, stone):
        count = 0
        flag = True
        while flag:
            x-=1
            y-=1
            try :
                if stone == self.arr[x][y]:
                    count += 1
                else :
                    return count
            except :
                flag = False
        return count
                
    def getUR(self, x, y, stone):
        count = 0
        flag = True
        while flag:
            x-=1
            y+=1
            try :
                if stone == self.arr[x][y]:
                    count += 1
                else :
                    return count
            except :
                flag = False
        return count
                
    def getDL(self, x, y, stone):
        count = 0
        flag = True
        while flag:
            x+=1
            y-=1
            try :
                if stone == self.arr[x][y]:
                    count += 1
                else :
                    return count
            except :
                flag = False
        return count
                
    def getDR(self, x, y, stone):
        count = 0
        flag = True
        while flag:
            x+=1
            y+=1
            try :
                if stone == self.arr[x][y]:
                    count += 1
                else :
                    return count
            except :
                flag = False
        return count        
        
                
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_() 