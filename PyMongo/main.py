import pymongo
from pymongo import MongoClient

# client = MongoClient("localhost", 27017)
client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
users = db.users
user1 = {"username": "Shock", "password": "mypassword",
         "favorite_number": 5, "hobbies": ["program", "gunpla", "games"]}
user_id = users.insert_one(user1).inserted_id
print(user_id)
