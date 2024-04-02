import cx_Oracle as cx

class DaoMenu:

    def __init__(self):
        self.conn = cx.connect("PYTHON/python@localhost:1521/XE")
        self.curs = self.conn.cursor()
    
    def getLabels(self):
        sql = """
        select
            m_id,
            m_name
        from menu
        order by m_id
        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        myjson = []
        for e in list:
            myjson.append({'m_id':e[0],'m_name':e[1]})
        return myjson
    
    def selectList(self):
        sql = """
        select
            m_id,
            m_name,
            DECODE(use_yn, 'y', 'O', 'n', 'X', '없음') use_yn
        from menu
        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        myjson = []
        for e in list:
            myjson.append({'m_id':e[0],'m_name':e[1],'use_yn':e[2]})
        return myjson
    
    def getCnt(self):
        sql = """
            select count(*)
            from menu
        """
        self.curs.execute(sql)
        cnt = self.curs.fetchone()
        return cnt[0];
    def __del__(self):
        self.curs.close()
        self.conn.close()    
    

if __name__ == '__main__':
    de = DaoMenu()
    cnt = de.getLabels()
    print(cnt)
