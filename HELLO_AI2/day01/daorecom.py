import cx_Oracle as cx
import numpy as np
from keras.utils import np_utils
class DaoRecom:

    def __init__(self):
        self.conn = cx.connect("PYTHON/python@localhost:1521/XE")
        self.curs = self.conn.cursor()
        
    def insertRecom(self,e_id,m_id):
        sql = f"""
            INSERT INTO RECOM (
                e_id,
                ymd,
                m_id
            ) VALUES (
                '{e_id}',
                to_char(SYSDATE,'yyyymmdd'),
                {m_id}
            )
        """
        self.curs.execute(sql)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()

if __name__ == '__main__':
    de = DaoRecom()
    xt = de.insertRecom("S001", 2)
    print(xt)
