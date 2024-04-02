from flask import Flask,redirect
from flask import request
from flask import render_template
import cv2

app = Flask(__name__)


@app.route('/')
@app.route('/ganada')
def ganada():
    li = []
    for i in range(ord("가"),ord("깋")+1):
        li.append(chr(i))
    return render_template('./ganada.html',a=li)
    

@app.route('/ganadaSem')
def ganadaSem():
    farr = ["Stylish","Gaegu","Dokdo","Sunflower","Nanum Gothic","Nanum Myeongjo","Nanum Pen Script","Black Han Sans"]
    char = request.args['char']
    w = request.args['w']
    ff = request.args['f']
    f = farr[int(ff)]
    return render_template('./ganadaSem.html',char=char, w=w,f=f)
    
@app.route('/static/examples/ganadara')
def Model3D():
    image = request.args['image']
    rx = request.args['rx']
    ry = request.args['ry']
    return render_template("ganadara.html",image = image, rx = rx, ry = ry)

#rx,ry >> 0.5로


if __name__ == '__main__':
  app.run(debug=True)
  
