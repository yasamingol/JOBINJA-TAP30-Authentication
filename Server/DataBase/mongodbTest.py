import pymongo
from pymongo import MongoClient
import asyncio



cluster = MongoClient(
    "mongodb+srv://yasamingol:2431380@cluster0.rrxyk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    connect=False)
db = cluster["Accounts"]
collectionAccounts = db["accounts"]
collectionLogins = db["logins"]




# accounts db functions
async def getNumberOfRowsOfAccountsTable():
    numberOfAccounts = collectionAccounts.count_documents({})
    return numberOfAccounts


async def saveAccount(username, password):
    id = await getNumberOfRowsOfAccountsTable()
    post = {"_id": id, "username": username, "password": password}
    collectionAccounts.insert_one(post)
    print("account saved to DB successfully")


async def getAccountsFullDBTable() :
    result = collectionAccounts.find()
    return result

async def getFullAccountById(accountId):
    result = collectionAccounts.find_one({"_id": accountId})
    return result

async def getAccountUsernameUsingAccountId(accountID):
    result = collectionAccounts.find_one({"_id": accountID})["username"]
    return result


async def getAccountPasswordUsingAccountId(accountID):
    result = collectionAccounts.find_one({"_id": accountID})["password"]
    return result

async def getAccountIDUsingAccountUsername(accountUsername) :
    result = collectionAccounts.find_one({"username": accountUsername})["_id"]
    return result






# login db functions
async def saveLogin(username, loginToken, loginTime):
    id = await getNumberOfRowsOfAccountsTable()
    post = {"_id": id, "username": username, "loginToken": loginToken, "loginTime": loginTime}
    collectionLogins.insert_one(post)
    print("login saved to DB successfully")

async def getNumberOfRowsOfLoginsTable():
    result = collectionLogins.count_documents({})
    return result

async def getLoginsFullDBTable():
    result = collectionLogins.find()
    return result

async def getLoginIdUsingToken(token):
    result = collectionLogins.find_one({"loginToken": token})["_id"]
    return result

async def getAccountIdUsingToken(token):
    result = collectionLogins.find_one({"loginToken": token})["username"]
    return result

async def getLastLoginTokenId(username):
    result = collectionLogins.find_one({"username": username}, {"$query": {}, "$orderby": {"loginTime": -1}})
    return result

async def checkIfTokenExists(token):
    result = collectionLogins.find({"loginToken": token})
    return result




asyncio.run(saveLogin("yasamingol","1234","123"))


