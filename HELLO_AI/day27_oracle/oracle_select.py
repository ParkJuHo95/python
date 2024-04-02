import cx_Oracle as cx
# conn = cx.connect("PYTHON","python","localhost:1521/XE") #DB연동
conn = cx.connect("PYTHON/python@localhost:1521/XE") #DB연동



def makeDictFactory(cursor):
    columnNames = [d[0] for d in cursor.description]
    def createRow(*args):
        return dict(zip(columnNames, args))
    return createRow
 
 
curs = conn.cursor()
curs.rowfactory = makeDictFactory(curs)
 

 
sql = "select * from emp"
curs.execute(sql)

rows = curs.fetchall()
print(rows)

curs.close()
conn.close()