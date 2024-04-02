from flask import Flask,redirect
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return redirect("static/examples/_ex04.html")

if __name__ == '__main__':
    app.run(debug=True)
  
