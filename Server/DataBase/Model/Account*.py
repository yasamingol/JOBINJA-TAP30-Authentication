from pymongo import MongoClient
from mongoengine import *
import asyncio


db = (connect('Accounts', host='mongodb+srv://yasamingol:2431380@cluster0.rrxyk.mongodb.net/Accounts?retryWrites=true&w=majority'))


class Account(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    meta = {'collection': 'accounts'}

async def saveAccount(username,password):
    Account(username=username, password=password).save()
    print("account saved to DB successfully")



