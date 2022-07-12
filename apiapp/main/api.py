from dotenv import load_dotenv
import os
import pymongo
import secrets
import datetime

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

def generator(id):
    mongodb_client = pymongo.MongoClient(MONGO_URI)
    db = mongodb_client["translatordb"]
    col = db["api_keys"]
    key = secrets.token_hex(16)
    server_id = int(id)
    server_key = {"server_id" : server_id}
    specs = {
            "server_id" : server_id,
            "key": key,
            "registration_date": datetime.now(),
        }
    result = col.update_one(server_key ,{"$set":specs}, True)
    return key
