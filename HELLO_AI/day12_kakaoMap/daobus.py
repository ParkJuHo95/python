import pymysql


class DaoBus:

    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = "select * from bus_path"
        self.curs.execute(sql)
        list = self.curs.fetchall()
        return list
    
    def insert(self, bp_name, bp_seq, sta_id, st_name, lat, lng):
        sql = f"INSERT INTO bus_path values('{bp_name}', '{bp_seq}', '{sta_id}', '{st_name}', '{lat}', '{lng}')"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def pointList(self):
        sql = f"select lat, lng from bus_path"
        self.curs.execute(sql)
        list = self.curs.fetchall()
        return list

    def busLine(self,bus_name):
        sql = f"select lat, lng from bus_path where bp_name = '{bus_name}'"
        self.curs.execute(sql)
        list = self.curs.fetchall()
        return list

    def busByPoint(self, lat, lng):
        sql = f"select bp_name from bus_path where lat = {lat} and lng = {lng}"
        self.curs.execute(sql)
        list = self.curs.fetchall()
        points = []
        for bus_name in list:
            points.append(self.busLine(bus_name))
        return points

    def __del__(self):
        self.curs.close()
        self.conn.close()    


if __name__ == '__main__':
    de = DaoBus()
    list = de.selectList()
    print(list)
