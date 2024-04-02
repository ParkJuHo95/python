from flask import Flask
from flask import request
from flask import render_template
from flask.json import jsonify
from day12_kakaoMap.daobus import DaoBus

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('bus_here.html')

@app.route('/bus')
def bus():
    return render_template('bus.html')

@app.route('/walk')
def walk():
    return render_template('walk_around.html')

@app.route('/bus_list')
def bus_list():
    dbp = DaoBus()
    list = dbp.pointList()
    return jsonify(list = list)

@app.route('/bus_load', methods=['POST'])
def bus_load():
    param = request.form['busName']
    print(param)
    # bus_name = param['busName']
    # print(bus_name)
    dbp = DaoBus()
    list = dbp.busLine(param)
    return jsonify(list = list)

@app.route('/bus_load_point', methods=['POST'])
def bus_load_id():
    lat = request.form['lat']
    lng = request.form['lng']
    dbp = DaoBus()
    list = dbp.busLine(busStop)
    return jsonify(list = list)
    
if __name__ == '__main__':
    app.run(debug=True)
  
