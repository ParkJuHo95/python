import pymysql


class DaoMem:

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = "select * from mem"
        self.curs.execute(sql)
        list = self.curs.fetchall()
        return list
    
    def select(self, m_id):
        sql = f"select * from mem where m_id = {m_id}"
        self.curs.execute(sql)
        vo = self.curs.fetchone()
        return vo
    
    def insert(self, m_id, m_name, moblie, email):
        sql = f"INSERT INTO mem values({m_id}, {m_name}, {moblie}, {email})"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self, m_id, m_name, mobile, email):
        sql = f"update mem set m_name = {m_name}, mobile = {mobile}, email = {email} where  m_id = {m_id}"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self, m_id):
        sql = f"delete from mem where m_id = {m_id}"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()    
