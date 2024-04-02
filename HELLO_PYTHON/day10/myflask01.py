from flask import Flask, redirect
from flask.json import jsonify
from flask.globals import request
from day10.daoemp import DaoEmp

app = Flask(__name__)


@app.route('/')
def index():
    return redirect("static/ajax.html")
    # return '<script>location.href="static/ajax.html"</script>'
    
@app.route('/ajax', methods=['POST'])
def ajax():
    # param = dict(request.form)
    param = request.get_json()
    print(param)
    print(param['menu'])
    return jsonify(msg = 'ajax')

@app.route('/ajax_list', methods=['POST'])
def ajax_list():
    de = DaoEmp()
    emps = de.selectList()
    return jsonify(emps = emps)

@app.route('/ajax_one', methods=['POST'])
def ajax_one():
    data = request.get_json()
    e_id = data['e_id']
    # e_id = request.form['e_id']
    de = DaoEmp()
    emp = de.select(e_id)
    return jsonify(emp = emp)


@app.route('/ajax_add', methods=['POST'])
def ajax_add():
    data = request.get_json()
    de = DaoEmp()
    print(data)
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    
    if de.select(e_id) != None :
        cnt = -20
    else :
        cnt = de.insert(e_id, e_name, gen, addr)
    # return jsonify(cnt = cnt);
    return jsonify(cnt = cnt)
    
    
    
@app.route('/ajax_mod', methods=['POST'])
def ajax_mod():
    data = request.get_json()
    de = DaoEmp()
    e_id = data['e_id']
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    cnt = de.update(e_id, e_name, gen, addr)
    print(cnt)
    return jsonify(cnt = cnt)
    
    
@app.route('/ajax_del', methods=['POST'])
def ajax_del():
    data = request
    e_id = data['e_id']
    de = DaoEmp()
    cnt = de.delete(e_id)
    return jsonify(cnt = cnt)
    
if __name__ == '__main__':
  app.run(debug=True)
  
