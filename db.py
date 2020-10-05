from flask import Flask
from flask_pymongo import pymongo


CONNECTION_STRING = "mongodb+srv://bts530:memeschool@player-cluster.cgxr1.mongodb.net/Tasks?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('Users')
user_collection = pymongo.collection.Collection(db,'user_info')
