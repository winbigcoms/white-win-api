import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

db_id = os.getenv('mongo_id')
db_pw = os.getenv('mongo_pw')
uri = f"mongodb+srv://{db_id}:{db_pw}@bsl.11tjagq.mongodb.net/?retryWrites=true&w=majority&appName=bsl"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.bsl
collection_name = db["withyou"]