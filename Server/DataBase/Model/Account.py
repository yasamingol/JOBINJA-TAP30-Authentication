from mongothon import Schema, create_model
from past.types import basestring
from pymongo import MongoClient
import asyncio

cluster = MongoClient(
    "mongodb+srv://yasamingol:2431380@cluster0.rrxyk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
    connect=False)
db = cluster["Accounts"]
collectionAccount = db['accounts']


account_schema = Schema({
    "_id": {"type": int, "required": True},
    "username": {"type": basestring, "required": True},
    "password": {"type": basestring, "required": True}
})

Account = create_model(account_schema, collectionAccount)
result = asyncio.run(Account.find_by_id({"_id": 0}))


# Functions
async def saveAccount(id, username, password):
    account = Account({
        "_id": id,
        "username": username,
        "password": password
    })
    account.save()
    print("account has been saved")
