import pymongo
from pymongo import MongoClient

# client = MongoClient("localhost", 27017)
client = MongoClient('mongodb://localhost:27017/')
db = client.pytests
