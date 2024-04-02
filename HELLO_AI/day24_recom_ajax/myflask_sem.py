from flask import Flask,redirect,jsonify
from flask.globals import request
from flask.templating import render_template
from flask_cors.extension import CORS
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('menu.h5')
labels = [
    {'name':'짜장','label':0,'arr':[1,0,0,0,0]},
    {'name':'삼겹살','label':1,'arr':[0,1,0,0,0]},
    {'name':'전복죽','label':2,'arr':[0,0,1,0,0]},
    {'name':'킹크랩','label':3,'arr':[0,0,0,1,0]},
    {'name':'라면','label':4,'arr':[0,0,0,0,1]}
]

app = Flask(__name__)
CORS(app)

def getIdxByName(name):
    for idx,l in enumerate(labels):
        if name == l['name']:
            return idx
    return -1


@app.route('/')
def index():
    return redirect("static/ajax.html")
    # return '<script>location.href="static/ajax.html"</script>'
    
    
@app.route('/ajax',methods=['POST'])
def ajax():
    data = request.get_json()
    print(data['menu'])
    return jsonify(result = "success")

@app.route('/fetch',methods=['POST'])
def fetch():
    data = request.get_json()
    print(f"data : {data}")
    myname=data['menu']
    print(myname)
    idx = getIdxByName(myname)
    print("idx",idx)
    x_rf = np.array([
        labels[idx]['arr']
    ])   
    if idx == -1:
        com = "데이터 로드 실패"
    else :
        pred_rf = model.predict(np.array([labels[idx]['arr']]))
        myidx = np.argmax(pred_rf)
        com = labels[myidx]['name']
    # pred_rf = model.predict(x_rf)
    # myidx =np.argmax(pred_rf)
    # menu = labels[myidx]['name']
    return jsonify(menu = com)


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    