from flask import Flask, request
from Server.Controller.JWTFunctions import *
# server requests
app = Flask(__name__)


@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        accountUserName = request.json.get('username')
        accountPassWord = request.json.get('password')
        tokenX = asyncio.run(generateJWT(accountUserName,accountPassWord))
        return tokenX


if __name__ == '__main__':
    asyncio.run(app.run(host="127.0.0.1", port="5000"))

