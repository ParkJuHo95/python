from flask import Flask, redirect
from flask.json import jsonify
from flask.globals import request
from day11.daomem import DaoMem

app = Flask(__name__)


@app.route('/')
def index():
    return redirect("static/mem.html")

@app.route('/mem_list', methods=['POST'])
def ajax_list():
    de = DaoMem()
    emps = de.selectList()
    return jsonify(emps = emps)

@app.route('/mem_one', methods=['POST'])
def ajax_one():
    data = request.get_json()
    m_id = data['m_id']
    de = DaoMem()
    mem = de.select(m_id)
    return jsonify(mem = mem)


@app.route('/mem_add', methods=['POST'])
def ajax_add():
    data = request.get_json()
    de = DaoMem()
    m_id = data['m_id']
    m_name = data['m_name']
    mobile = data['mobile']
    email = data['email']
    
    if de.select(m_id) != None :
        cnt = -20
    else :
        cnt = de.insert(m_id, m_name, mobile, email)
    return jsonify(cnt = cnt)
    
    
    
@app.route('/mem_mod', methods=['POST'])
def ajax_mod():
    data = request.get_json()
    de = DaoMem()
    m_id = data['m_id']
    m_name = data['m_name']
    mobile = data['mobile']
    email = data['email']
    cnt = de.update(m_id, m_name, mobile, email)
    print(cnt)
    return jsonify(cnt = cnt)
    
    
@app.route('/mem_del', methods=['POST'])
def ajax_del():
    data = request.get_json()
    m_id = data['m_id']
    de = DaoMem()
    cnt = de.delete(m_id)
    return jsonify(cnt = cnt)
    
if __name__ == '__main__':
  app.run(debug=True)
  
