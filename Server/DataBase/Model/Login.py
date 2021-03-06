from pymongo import MongoClient
from mongoengine import *
import asyncio

db = (connect('Accounts',
              host='mongodb+srv://yasamingol:2431380@cluster0.rrxyk.mongodb.net/Accounts?retryWrites=true&w=majority'))


class Login(Document):
    _id = StringField(required=True)
    username = StringField(required=True)
    loginToken = StringField(required=True)
    loginTime = StringField(required=True)
    meta = {'collection': 'logins'}


async def saveLogin(username, loginToken, loginTime):
    id = await getNumberOfRowsOfLoginsTable()
    Login(username=username, loginToken=loginToken, loginTime=loginTime, _id=str(id + 1)).save()
    print("account logged in successfully")


async def getNumberOfRowsOfLoginsTable():
    numberOfLogins = Login.objects().count()
    return numberOfLogins


async def getLoginsFullDBTable():
    return Login.objects


async def getLoginIdUsingToken(token):
    login = Login.objects(loginToken=token)[0]
    return login._id

async def getAccountIdUsingToken(token):
    login = Login.objects(loginToken = token)[0]
    return login.username

async def getLastLoginTokenId(username):
    result = Login.objects(username=username).order_by("loginTime")
    return result

async def checkIfTokenExists(token):
    result = Login.objects(loginToken= token)
    return result


# asyncio.run(saveLogin("yasamingol","token","60"))
print(asyncio.run(getLastLoginTokenId("token")))

