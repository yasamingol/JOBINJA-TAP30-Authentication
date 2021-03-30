from pymongo import MongoClient
from mongoengine import *
import asyncio

db = (connect('Accounts',
              host='mongodb+srv://yasamingol:2431380@cluster0.rrxyk.mongodb.net/Accounts?retryWrites=true&w=majority'))


class Account(Document):
    _id = StringField(required=True)
    username = StringField(required=True)
    password = StringField(required=True)
    meta = {'collection': 'accounts'}



async def getNumberOfRowsOfAccountsTable():
    numberOfAccounts = Account.objects().count()
    return numberOfAccounts



async def saveAccount(username, password):
    id = await getNumberOfRowsOfAccountsTable()
    account = Account(username=username, password=password, _id=str(id+1)).save()
    print("account saved to DB successfully")
    return account._id


async def getAccountsFullDBTable():
    return Account.objects()


async def getFullAccountById(accountId):
    account = Account.objects(_id=accountId)[0]
    return account


async def getAccountUsernameUsingAccountId(accountID):
    account = Account.objects(_id=accountID)[0]
    return account.username

async def getAccountPasswordUsingAccountId(accountID):
    account = Account.objects(_id=accountID)[0]
    return account.password

async def getAccountIDUsingAccountUsername(accountUsername) :
    account = Account.objects(username=accountUsername)[0]
    return account._id



