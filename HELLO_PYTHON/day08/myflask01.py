from flask import Flask
from flask import request
from flask import render_template
from day08.daoemp import DaoEmp

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/')
@app.route('/emp_list')
def emp():
    # conn = pymysql.connect(host='127.0.0.1',port=3305, user='root', password='python', db='python', charset='utf8')
    # curs = conn.cursor(pymysql.cursors.DictCursor)  #딕셔너리(json형태)로 가져오는 법 
    # sql = "select * from emp"
    # curs.execute(sql)
    # emplist = curs.fetchall()
    de = DaoEmp()
    emps = de.selectList()
    return render_template('./emp_list.html', list = emps )

@app.route('/emp_detail')
def emp_detail():
    de = DaoEmp()
    e_id = request.args['e_id']
    vo = de.select(e_id)
    return render_template('./emp_detail.html', vo = vo )

@app.route('/emp_mod')
def emp_update():
    de = DaoEmp()
    e_id = request.args['e_id']
    vo = de.select(e_id)
    return render_template('./emp_mod.html', vo = vo )

@app.route('/emp_mod_act')
def emp_update_act():
    de = DaoEmp()
    e_id = request.args['e_id']
    e_name = request.args['e_name']
    gen = request.args['gen']
    addr = request.args['addr']
    cnt = de.update(e_id, e_name, gen, addr)
    print(addr)
    return render_template('./emp_mod_act.html', cnt = cnt )
    
@app.route('/emp_delete')
def emp_delete():
    de = DaoEmp()
    e_id = request.args['e_id']
    cnt = de.delete(e_id)
    return render_template('./emp_delete_act.html', cnt = cnt)

@app.route('/emp_add')
def emp_add():
    return render_template('./emp_add.html')

@app.route('/emp_add_act')
def emp_add_act():
    de = DaoEmp()
    e_id = request.args['e_id']
    e_name = request.args['e_name']
    gen = request.args['gen']
    addr = request.args['addr']
    
    if de.select(e_id) != None:
        cnt = 20
    else :
        cnt = de.insert(e_id, e_name, gen, addr)
    return render_template('./emp_add_act.html', cnt = cnt)
    
if __name__ == '__main__':
    app.run(debug=True)
  
  
