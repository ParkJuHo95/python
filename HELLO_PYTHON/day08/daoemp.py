import pymysql


class DaoEmp:

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def selectList(self):
        sql = "select * from emp"
        self.curs.execute(sql)
        list = self.curs.fetchall()
        return list
    
    def select(self, e_id):
        sql = f"select * from emp where e_id = {e_id}"
        self.curs.execute(sql)
        # list = self.curs.fetchall()
        # return list[0]
        vo = self.curs.fetchone()
        return vo
    
    def insert(self, e_id, e_name, gen, addr):
        sql = f"INSERT INTO emp values({e_id}, {e_name}, {gen}, {addr})"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self, e_id, e_name, gen, addr):
        sql = f"update emp set e_name = {e_name}, gen = {gen}, addr = {addr} where  e_id = {e_id}"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self, e_id):
        sql = f"delete from emp where e_id = {e_id}"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()    


if __name__ == '__main__':
    de = DaoEmp()
    cnt = de.update('6', '7', '7', '7')
    print(cnt)
