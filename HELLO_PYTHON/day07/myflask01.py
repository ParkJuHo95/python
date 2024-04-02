from flask import Flask
from flask import request
from flask import render_template
from day06_3 import mysql_select

app = Flask(__name__)


@app.route('/')
def index():
   return 'Hello ddd'

@app.route('/param')
def param():
   # return 'PARAM : ' + request.args.get('name','없음')   return 'PARAM : ' + request.args['name']

@app.route('/post', methods=['POST'])
def post():
    # first = request.form.get('menu','없음')
    # second = request.form.get('second','없음')
    # third = request.form.get('third','없음')
    # return 'POST : '+ first + second + third
    menu = request.form['menu']
    return 'POST : ' + menu

@app.route('/post')
def get():   return 'post인척하는 get'

@app.route('/forw')
def forw():
    a = "홍길동"
    b = ["전우치", "일지매"]
    c = [
        {'e_id':1, 'e_name':1, 'gen':1, 'addr':1},
        {'e_id':2, 'e_name':2, 'gen':2, 'addr':2},
        {'e_id':3, 'e_name':3, 'gen':3, 'addr':3}
    ]
    d = mysql_select
    return render_template('./forw.html', name=a, names=b, c=c,
                           d=d)


@app.route('/emp')
def emp():
    d = mysql_select.rows
    return render_template('./emp.html', d=d)


@app.route('/emp_detail')
def emp_detail():
    vo = request.args['e']
    return render_template('./emp_detail.html', vo=vo)

    
if __name__ == '__main__':
  app.run(debug=True)
  
