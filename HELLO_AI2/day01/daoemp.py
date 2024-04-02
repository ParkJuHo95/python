import cx_Oracle as cx

class DaoEmp:

    def __init__(self):
        self.conn = cx.connect("PYTHON/python@localhost:1521/XE")
        self.curs = self.conn.cursor()
        
    def selectList(self):
        sql = """
        select
            e_id,
            e_name,
            DECODE(gen, 'M', '남자', 'F', '여자', '기타') gen,
            addr
        from emp
        """
        self.curs.execute(sql)
        list = self.curs.fetchall()
        myjson = []
        for e in list:
            myjson.append({'e_id':e[0],'e_name':e[1],'gen':e[2],'addr':e[3]})
        return myjson
    
    def select(self, e_id):
        sql = f"select * from emp where e_id = {e_id}"
        self.curs.execute(sql)
        # list = self.curs.fetchall()
        # return list[0]
        vo = self.curs.fetchone()
        return vo
    
    def __del__(self):
        self.curs.close()
        self.conn.close()    
    
    

if __name__ == '__main__':
    de = DaoEmp()
    cnt = de.selectList()
    print(cnt)
