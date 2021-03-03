import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://yasamingol:2431380@cluster0.rrxyk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",connect=False)
db = cluster["test"]
collection = db["test"]

post = {"_id": 0, "name": "tim", "score": 5}

collection.insert_one(post)
