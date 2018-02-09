import pymongo
from pymongo import MongoClient

# client = MongoClient("localhost", 27017)
client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
users = db.users
user1 = {"username": "Shock", "password": "mypassword",
         "favorite_number": 5, "hobbies": ["program", "gunpla", "games"]}
# user_id = users.insert_one(user1).inserted_id
user_collection = [{"username":"Rich", "password":"12345"},
                   {"username":"Nick", "password":"45678"},
                   {"username":"Mama", "password":"91234"}]

inserted = users.insert_many(user_collection)
print(inserted.inserted_ids)