from flask import Flask, request
from datetime import datetime
import jwt

app = Flask(__name__)

accountUserName = None
accountPassWord = None
loginToken = None


@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        accountUserName = request.json.get('username')
        accountPassWord = request.json.get('password')
        return accountPassWord+accountUserName


def createToken(username, password):
    try:
        user = {
            'username': username,
            'password': password,
            'time': datetime.now()
        }
        return jwt.encode(
            user,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e




if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")
