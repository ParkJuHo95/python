import cx_Oracle as cx
import numpy as np
from keras.utils import np_utils
from day01.daomenu import DaoMenu
class DaoDiet:

    def __init__(self):
        self.conn = cx.connect("PYTHON/python@localhost:1521/XE")
        self.curs = self.conn.cursor()
        
    def selectList(self):
        sql = """
        SELECT DIET.*,EMP.E_NAME, MENU.M_NAME
        FROM DIET JOIN EMP ON ( DIET.E_ID = EMP.E_ID)
        JOIN MENU ON (DIET.M_ID = MENU.M_ID)
        ORDER BY YMD DESC, E_NAME
        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        myjson = []
        for e in list:
            myjson.append({'e_id':e[0],'m_id':e[1],'ymd':e[2],'e_name':e[3],'m_name':e[4]})
        return myjson
    
    def getPred(self,e_id,labels):
        sql = f"""
            SELECT M_ID
            FROM DIET
            WHERE e_id = '{e_id}'
            ORDER BY YMD DESC 
        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        a = np_utils.to_categorical(list[1],labels)
        b = np_utils.to_categorical(list[0],labels)
        x_test = np.append(a,b)
        return x_test.astype(int)
    
    def getArray(self,e_id,labels):
        sql = f"""
            SELECT M_ID
            FROM DIET
            WHERE E_ID = '{e_id}'
            ORDER BY YMD DESC
        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        xt = []
        yt = []
        for i in range(len(list)-2):
            arr = []
            daybeforeyester = list[i+2][0]
            arr.append(daybeforeyester)
            yester = list[i+1][0]
            arr.append(yester)
            xt.append(arr)
            yt.append(list[i][0])
        
        x_train = []
        for i in xt:
            a = np_utils.to_categorical(i[0],labels)
            b = np_utils.to_categorical(i[1],labels)
            c = np.append(a,b)
            x_train.append(c)
        
        x_train = np.array(x_train).astype(int)
        y_train = []
        
        for i in yt:
            y_train.append(i)
            
        y_train = np.array(y_train).astype(int)
        return x_train,y_train,list
    
    def __del__(self):
        self.curs.close()
        self.conn.close()    

if __name__ == '__main__':
    de = DaoDiet()
    dm = DaoMenu()
    cnt = dm.getCnt()
    xt = de.getArray("S001", cnt)
    print(xt)
