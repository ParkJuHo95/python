import cx_Oracle as cx
# conn = cx.connect("PYTHON","python","localhost:1521/XE") #DB연동
conn = cx.connect("PYTHON/python@localhost:1521/XE") #DB연동
 
curs = conn.cursor()
 
e_id = 4  
e_name = 6
gen = 6
addr = 6

sql = f"""
UPDATE EMP 
SET
    e_name = '{e_name}',
    gen = '{gen}',
    addr = '{addr}'
WHERE 
    E_ID = {e_id}
"""
# curs.execute(sql)
curs.execute(sql)
conn.commit()
print(curs.rowcount)
curs.close()
conn.close()