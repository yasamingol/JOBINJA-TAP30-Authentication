from flask import Flask, request
from Server.Controller.JWTFunctions import *
from bson.json_util import dumps


import json
# server requests
app = Flask(__name__)


@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        accountUserName = request.json.get('username')
        accountPassWord = request.json.get('password')
        tokenX = asyncio.run(generateJWT(accountUserName,accountPassWord))
        asyncio.run(saveLogin(accountUserName,tokenX,str(round(datetime.now().timestamp()))))
        return tokenX

@app.route('/validateToken',methods=['POST'])
def validateUserLoginTokenAPI():
    if request.method == 'POST':
        token = request.json.get("token")
        validationResult = asyncio.run(validateLoginToken(token))
        return json.dumps(validationResult, separators=(',', ':'))



@app.route('/saveAccount',methods=['POST'])
def saveAccountRequest():
    if request.method == 'POST':
        accountUsername = request.json.get('username')
        accountPassWord = request.json.get('password')
        asyncio.run(saveAccount(accountUsername,accountPassWord))
        return "account created succesfully"



@app.route('/getAccountsFullDBTable',methods=['POST'])
def getAccountsFullDBTableRequest():
    if request.method == 'POST':
        return dumps(list(asyncio.run(getAccountsFullDBTable())),separators=(',', ':'))


@app.route('/getFullAccountById', methods=['POST'])
def getFullAccountByIdRequest():
    if request.method == 'POST':
        accountId = str(request.json.get('id'))
        account = asyncio.run(getFullAccountById(accountId))
        return account.username+"/"+account.password

@app.route('/getAccountUsernameUsingAccountId', methods=['POST'])
def getAccountUsernameUsingAccountIdRequest():
    if request.method == 'POST':
        accountId = str(request.json.get('id'))
        return asyncio.run(getAccountUsernameUsingAccountId(accountId))

@app.route('/getAccountPasswordUsingAccountId', methods=['POST'])
def getAccountPasswordUsingAccountIdRequest():
    if request.method == 'POST':
        accountId = str(request.json.get('id'))
        return asyncio.run(getAccountPasswordUsingAccountId(accountId))

@app.route('/getAccountIDUsingAccountUsername', methods=['POST'])
def getAccountIDUsingAccountUsernameRequest():
    if request.method == 'POST':
        username = request.json.get('username')
        return str(asyncio.run(getAccountIDUsingAccountUsername(username)))

@app.route('/getNumberOfRowsOfAccountsTable', methods=['POST'])
def getNumberOfRowsOfAccountsTableRequest():
    if request.method == 'POST':
        return str(asyncio.run(getNumberOfRowsOfAccountsTable()))



if __name__ == '__main__':
    asyncio.run(app.run(host="127.0.0.1", port="5001"))

