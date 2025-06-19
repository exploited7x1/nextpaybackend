import requests
from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  


@app.route("/createInvoice", methods=["POST", "GET"])
def createInvoice():
    args = request.args
    print(args)
    amount = args.get('amount')
    name = args.get('name')
    url = "https://accept.paymob.com/v1/intention/"

    payload = json.dumps(
        {
            "amount": int(amount)*100,
            "currency": "EGP",
            "payment_methods": [
                5001401,
            ],
            "items": [
                {
                    "name": "Item name 1",
                    "amount": int(amount)*100,
                    "description": "Watch",
                    "quantity": 1,
                }
            ],
            "billing_data": {
                "apartment": "6",
                "first_name": name,
                "last_name": "nextPay",
                "street": "938, Al-Jadeed Bldg",
                "building": "939",
                "phone_number": "+96824480228",
                "country": "OMN",
                "email": "AmmarSadek@gmail.com",
                "floor": "1",
                "state": "Alkhuwair",
            },
            "customer": {
                "first_name": name,
                "last_name":"nextPay",
                "email": "AmmarSadek@gmail.com",
                "extras": {"re": "22"},
            },
            "extras": {"ee": 22},
        }
    )
    headers = {
        "Authorization": "Token egy_sk_test_5c337aad58356b787474eddcc12acd18d73259283845061fac8c2fd48b2e4734",
        "Content-Type": "application/json",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    clientSecret = response.json()['client_secret']
    return jsonify({'success':True,"redirect_link":f"https://accept.paymob.com/unifiedcheckout/?publicKey=egy_pk_test_UR18MctH0X93Imu1VlmogKX7jKPQ4rEI&clientSecret={clientSecret}"})


app.run(host=0.)
