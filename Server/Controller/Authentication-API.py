from flask import Flask, request
from datetime import date, datetime, time
from Server.Controller.JWTFunctions import *


import json
# server requests
app = Flask(__name__)


@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        accountUserName = request.json.get('username')
        accountPassWord = request.json.get('password')
        tokenX = asyncio.run(generateJWT(accountUserName,accountPassWord))
        asyncio.run(saveLogin(accountUserName,tokenX,round(datetime.now().timestamp())))
        return tokenX

@app.route('/validateToken',methods=['POST'])
def validateUserLoginTokenAPI():
    if request.method == 'POST':
        token = request.json.get("token")
        validationResult = asyncio.run(validateLoginToken(token))
        valid = validationResult[0]
        message = validationResult[1]
        if valid==False:
            return "False:"+message
        else:
            return "True:"+message




if __name__ == '__main__':
    asyncio.run(app.run(host="127.0.0.1", port="5001"))

