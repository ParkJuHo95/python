from flask import request
from flask import render_template
from flask import Flask
from flask.json import jsonify
import requests
app = Flask(__name__, static_folder='static')


@app.route('/')
def main():
    return render_template('main.html')

@app.route('/kakaopay/paymethod.ajax', methods=['POST'])
def payMethod():
    if request.method == 'POST':
        URL = "https://kapi.kakao.com/v1/payment/ready"
        headers = {
            'Authorization' : "KakaoAK6c6d88b9e510d1de9393c7b1610daada",
            'Content-type' : 'application/x-www-form-urlencoded;charset=utf-8'
        }
        params = {
            "cid" : "TC0ONETIME",
            "partner_order_id" : "partner_order_id",
            "partner_user_id" : "partner_user_id",
            "item_name" : "초코파이",
            "quantity" : 1,
            "total_amount" : 2200,
            "vat_amount" : 200,
            "tax_free_amount" : 0,
            "approval_url" : "https://localhost:5000/kakao.com/success",
            "fail_url" : "https://localhost:5000/kakao.com/fail",
            "cancel_url" : "https://localhost:5000/kakao.com/cancel"
        }
        
        res = requests.post(URL, headers = headers, params=params)
        app.tib = res.json()['tid']
        return jsonify({"next_url" : res.json()['next_redirect_pc_url']})
    
    return render_template('main.html')

    
if __name__ == '__main__':
    app.run(debug=True)
  
