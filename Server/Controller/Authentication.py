from flask import Flask, request
from datetime import date, datetime
import jwt
import json

# server requests
app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        accountUserName = request.json.get('username')
        accountPassWord = request.json.get('password')
        # return createToken(accountUserName, accountPassWord)


# token
def createToken():
    user = {
        "username": "jafar",
        "password": "1234"
    }
    payload = {"some": "payload", "aud": user}
    encoded = jwt.encode(payload, "secret")
    return encoded


if __name__ == '__main__':
    # app.run(host="127.0.0.1", port="5000")
    print(createToken())
