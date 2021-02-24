from flask import Flask, request
from datetime import date, datetime, time
import jwt
from Server.DataBase.loginDataBase import *
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




async def checkTokenValidation(token) :
     tokenId = await getLoginIdUsingToken(token)
     isExpired = await checkIfTokenIsExpired(token,tokenId)
     isLatestLogin = await checkIfTokenIsForTheLatestLogin(token,tokenId)
    if isExpired:
        isValid = True,
        message = "token has expired!"
        return isValid,message


    if tokenId===undefined:
        isValid = True,
        message = "token is undefined!"
        return isValid,message

    elif !isLatestLogin:
        isValid = True
        message = "this is not your latest login! updated version of token is required."
        return isValid,message

    else :
        isValid =  True
        message =  "token is valid."
        return isValid,message




async def checkIfTokenIsForTheLatestLogin(token,tokenId):
    accountId = await getAccountIdUsingToken(token)
    latestTokenId = await getLastLoginTokenId(accountId)
    if latestTokenId==tokenId:
        return True
    else :
        return False


async def validateUserLoginToken(token):
    validation = await checkTokenValidation(token)
    if (validation.isValid) :
        isValid: True
        message: validation.message
        return isValid,message

    else :
        isValid: False
        message: validation.message
        return  isValid,message





if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000")
