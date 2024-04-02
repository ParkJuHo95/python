import cx_Oracle as cx
# conn = cx.connect("PYTHON","python","localhost:1521/XE") #DB연동
conn = cx.connect("PYTHON/python@localhost:1521/XE") #DB연동
 
curs = conn.cursor()
 
e_id = 4  
e_name = 4
gen = 4 
addr = 4

sql = f"""
INSERT INTO EMP 
(
    e_id,
    e_name,
    gen,
    addr
)
 VALUES ('{e_id}','{e_name}','{gen}','{addr}')"""
# curs.execute(sql)
curs.execute(sql)
conn.commit()
print(curs.rowcount)
curs.close()
conn.close()