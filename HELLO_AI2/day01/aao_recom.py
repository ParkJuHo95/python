import tensorflow as tf
import numpy as np
from day01.daomenu import DaoMenu
from day01.daodiet import DaoDiet
from day01.daorecom import DaoRecom
from day01.daoemp import DaoEmp
import threading
from defusedxml.expatbuilder import parseString

class AaoRecom:
    def __init__(self):     #파이썬에서 생성자
        self.dm = DaoMenu()
        self.dd = DaoDiet()
        self.dr = DaoRecom()
        self.cnt = self.dm.getCnt()
        self.x_train = None;
        self.y_train = None;
        self.labels = self.dm.getLabels()
    
    def setXYtrain(self,e_id,cnt):
        x_train, y_train = self.dd.getArray(e_id,cnt)
        self.x_train = x_train
        self.y_train = y_train
    
    def pred(self,e_id):   #첫번째 인자부분에 self를 넣은것은 문법적인 부분
        self.setXYtrain(e_id,self.cnt)
        
        print(self.x_train)
        print(self.y_train)
        
        model = tf.keras.Sequential([
                        tf.keras.layers.Flatten(input_shape=(self.cnt*2,)),
                        tf.keras.layers.Dense(512, activation = tf.nn.relu),
                        tf.keras.layers.Dense(512, activation = tf.nn.relu),
                        tf.keras.layers.Dense(self.cnt, activation=tf.nn.softmax)
                    ])
        model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
        
        model.fit(self.x_train, self.y_train, epochs=10)
        model.save('menu.h5')
        pred = model.predict(self.x_train)
        for p in pred:
            myidx = np.argmax(p)
            print("myidx",myidx,p)
        #
        x_rf =self.dd.getPred(e_id, self.cnt)
        pred_rf = model.predict(x_rf)
        myidx = np.argmax(pred_rf)
        recom_menu = self.labels[myidx]['m_name']
        recom_m_id = self.labels[myidx]['m_id']
        self.dr.insertRecom(e_id, recom_m_id)
        print(recom_menu)
        
    def __del__(self):
        pass


if __name__ == '__main__':
    de = DaoEmp()
    ar = AaoRecom();
    list = de.selectList()
    for idx,e in enumerate(list):
        threading.Thread(target=ar.pred(e['e_id'])).start()
        




