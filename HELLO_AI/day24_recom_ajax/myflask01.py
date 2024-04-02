from flask import Flask, redirect
from flask.json import jsonify
from flask.globals import request
from flask_cors.extension import CORS
from keras.models import load_model
import numpy as np
app = Flask(__name__)
CORS(app)

model = load_model('menu.h5')
labels = [
            {'name':'짜장','label':0,'arr':[1,0,0,0,0]},
            {'name':'삼겹살','label':1,'arr':[0,1,0,0,0]},
            {'name':'전복죽','label':2,'arr':[0,0,1,0,0]},
            {'name':'킹크랩','label':3,'arr':[0,0,0,1,0]},
            {'name':'라면','label':4,'arr':[0,0,0,0,1]}
        ]

def getIdxByName(myName):
    for idx,l in enumerate(labels):
        if l['name'] == myName:
            return idx;
    return -1;

@app.route('/')
def index():
    return redirect("static/ajax.html")
    
@app.route('/menuRecomend', methods=['POST'])
def ajax():
    data = request.get_json()
    print(data.yester)
    return jsonify({data:data})
   
@app.route('/ajax', methods=['POST'])
def fetch():
    data = request.get_json()
    myName=data['menu']
    idx = getIdxByName(myName);
    com = ""
    if idx == -1:
        com = "데이터 로드 실패"
    else :
        pred_rf = model.predict(np.array([labels[idx]['arr']]))
        myidx = np.argmax(pred_rf)
        com = labels[myidx]['name']
    return jsonify(menu = com)
   
 
if __name__ == '__main__':
    app.run(debug=True)
  
