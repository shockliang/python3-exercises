import pymongo
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client.mydb
users = db.users

users.create_index([("username", pymongo.ASCENDING)])
