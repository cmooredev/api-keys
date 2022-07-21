from dotenv import load_dotenv
import os
import stripe
import pymongo
import secrets
import json
from datetime import datetime

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
stripe.api_key = os.getenv('STRIPE_API_KEY')

def generator(id, plan):
    credits = 0
    print(plan)
    if str(plan) == 'Intro':
        credits = 75000
    elif str(plan) == 'Basic':
        credits = 200000
    elif str(plan) == 'Pro':
        credits = 450000
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
            "credits": credits,
        }
    result = col.update_one(server_key ,{"$set":specs}, True)
    return key
