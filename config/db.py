import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

db_id = os.getenv('mongo_id')
db_pw = os.getenv('mongo_pw')
user_collection = os.getenv('mongo_user_collection')
promise_collection = os.getenv('mongo_promise_collection')
event_collection = os.getenv('mongo_event_collection')

uri = f"mongodb+srv://{db_id}:{db_pw}@bsl.11tjagq.mongodb.net/?retryWrites=true&w=majority&appName=bsl"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.bsl

promise_collection_name = db[promise_collection]
user_collection_name = db[user_collection]
event_collection_name = db[event_collection]