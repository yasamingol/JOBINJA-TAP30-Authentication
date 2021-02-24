from flask import Flask, request
from datetime import date, datetime, time
import jwt
import asyncio

# server requests
app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        accountUserName = request.json.get('username')
        accountPassWord = request.json.get('password')
        return generateJWT(accountUserName, accountPassWord)


# token
def generateJWT(username,password):
    user = {
        "username": username,
        "password": password
    }
    jwt_valid_seconds = 180
    expiryTime = round(datetime.now().timestamp()) + jwt_valid_seconds
    payload = {"some": "payload", "aud": user,"exp":expiryTime}
    token = jwt.encode(payload, "secret")
    return token


def checkIfTokenIsExpired(token):
    decodedToken = jwt.decode(token,verify=False)
    currentTime = round(datetime.now().timestamp())
    tokenExp = decodedToken.get('exp')
    return currentTime>tokenExp

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")
