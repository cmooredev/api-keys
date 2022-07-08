from dotenv import load_dotenv
import os
import pymongo
import secrets

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')

def generator():
    mongodb_client = pymongo.MongoClient(MONGO_URI)
    db = mongodb_client["translatordb"]
    col = db["api_keys"]
    key = secrets.token_hex(16)
    server_key = {"id" : id}
    specs = {
            "id" : id,
            "key": key,
        }
    result = col.update_one(server_key ,{"$set":specs}, True)
    return key
