from flask import request
from flask import render_template
from day01.daoemp import DaoEmp
from day01.daomenu import DaoMenu
from day01.daodiet import DaoDiet
from flask import Flask, render_template, url_for
from day01.aao_recom import AaoRecom
app = Flask(__name__, static_folder='static')
de = DaoEmp()
dd = DaoDiet()
dm = DaoMenu()
aa = AaoRecom()

@app.route('/')
def main():
    return render_template('main.html')
@app.route('/emp')
def emp():
    list = de.selectList()
    return render_template('emp.html',list=list)
@app.route('/diet')
def diet():
    list = dd.selectList()
    return render_template('diet.html',list=list)    
@app.route('/menu')
def menu():
    list = dm.selectList()
    return render_template('menu.html',list=list)    
@app.route('/recom')
def recom():
    aa.pred()
    return render_template('recom.html')
    
if __name__ == '__main__':
    app.run(debug=True)
  
