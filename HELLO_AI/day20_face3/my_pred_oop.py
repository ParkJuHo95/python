from keras.utils import np_utils
from keras.datasets import cifar10
import numpy as np
import tensorflow as tf
import cv2

class AiFace:
    def __init__(self):     #파이썬에서 생성자
        self.arr = [
            {'lbl':0,'f':'00','n':'박주호'},
            {'lbl':1,'f':'01','n':'박지원'},
            {'lbl':2,'f':'02','n':'이미소'},
            {'lbl':3,'f':'03','n':'하예종'}
        ]
        self.model = tf.keras.models.load_model('face.h5')
        
    def getNameByImage(self,img):
        img = cv2.resize(img,(32,32))
        img = np.reshape(img,(-1,32,32,3))/255
        pred = self.model.predict(img)
        myidx = np.argmax(pred)
        return self.arr[myidx]['n']

if __name__ == '__main__':
    img = cv2.imread("132.png")
    af = AiFace()
    name = af.getNameByImage(img)
    print(name)
