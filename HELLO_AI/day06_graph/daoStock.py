import pymysql
import numpy as np


class DaoStock:

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selectArr(self,s_name):
        sql = f"""select * from stock 
                where 
                s_name = '{s_name}'
            """
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        
        arr = []
        for s in list:
            arr.append(s['price'])
        return arr
    
        # first = arr[0]
        # percent = []
        # for i in arr:
        #     percent.append((i-first)/i * 100 )
        # return percent
        
    def selectArrN(self,s_name):
        sql = f"""select * from stock 
                where 
                s_name = '{s_name}'
            """
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        
        arr = []
        for s in list:
            arr.append(s['price'])
        arr_np = np.array(arr)
        return arr_np
    
    def selectSNames(self):
        sql = f"""select  s_name from stock group by s_name
            """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        names = []
        for i in list:
            names.append(i['s_name'])
        return names
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    ds = DaoStock();
    arr = ds.selectSNames()
    print(arr)
    