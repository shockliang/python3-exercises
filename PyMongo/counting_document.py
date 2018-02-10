import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
users = db.users
print("Total items:", users.find().count())

print("Favorite number equal to 5. count:", users.find(
    {"favorite_number": 5, "username": "Shock"}).count())
