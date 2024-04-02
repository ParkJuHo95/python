import pymysql
 
conn = pymysql.connect(host='127.0.0.1',port=3305, user='root', password='python',
                       db='python', charset='utf8')
 
 
#파이썬의 cursor는 자바의 statement와 비슷(자바의 커서와는 다르다)
# curs = conn.cursor(pymysql.cursors.DictCursor)  #딕셔너리(json형태)로 가져오는 법 
curs = conn.cursor()
#""" a """ 따음표 3개로 묶어놓으면 띄워쓰기해도 자동으로 인식해준다
sql = "INSERT INTO emp VALUES(%s, %s, %s, %s)"
curs.execute(sql,(4,'4','4','4'))
conn.commit()

curs.close()
conn.close()