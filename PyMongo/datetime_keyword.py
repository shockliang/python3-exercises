import pymongo
import datetime
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
users = db.users

current_date = datetime.datetime.now()
old_date = datetime.datetime(2009, 8, 14)

uid = users.insert({"username": "Liang", "date": current_date})
print(users.find({"date": {"$gt": old_date}}).count())  # greater than
print(users.find({"date": {"$gte": old_date}}).count())  # greater than equal
print(users.find({"date": {"$lt": old_date}}).count())  # less than
print(users.find({"date": {"$exists": True}}).count())
print(users.find({"username": {"$ne": "shock"}}).count()) # not equal
