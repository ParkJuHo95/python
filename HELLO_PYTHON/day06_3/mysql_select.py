import pymysql
 
conn = pymysql.connect(host='127.0.0.1',port=3305, user='root', password='python',
                       db='python', charset='utf8')
 
 
#파이썬의 cursor는 자바의 statement와 비슷(자바의 커서와는 다르다)
# curs = conn.cursor()  #딕셔너리(json형태)로 가져오는 법 
curs = conn.cursor(pymysql.cursors.DictCursor)  #딕셔너리(json형태)로 가져오는 법 
# curs = conn.cursor()
 
sql = "select * from emp"
curs.execute(sql)

rows = curs.fetchall()
print(rows[0])  #튜플형태로 줌
print(rows[0]['addr'])
print(rows[0].get('addr'))

curs.close()
conn.close()