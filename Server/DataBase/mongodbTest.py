import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://yasamingol:2431380@cluster0.rrxyk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",connect=False)
db = cluster["test"]
collection = db["test"]

post1 = {"_id": 1, "name": "tim", "score": 5}
post2 = {"_id": 2, "name": "yac", "score": 10}

# collection.insert_many([post1, post2])
# results = collection.find({"name": "yac"})
# results = collection.find_one({"_id": ""})
# results = collection.delete_one({})
# results = collections.update_one({"_id":1},{"$set":{"name":"jafar"}})
# for result in results:
#     print(result)
#     print(result["_id"])

post_count = collection.count_documents({})
print(post_count)
