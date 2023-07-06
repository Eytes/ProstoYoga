from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')  # cluster
db = client.prostoyoga  # create database

# create collections
users = db['users']
practices = db['practices']
schedule = db['schedule']
