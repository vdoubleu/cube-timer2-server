from pymongo import MongoClient
import os
from dotenv import load_dotenv

def connect():
    load_dotenv()
    user = os.getenv("DBUSER")
    pw = os.getenv("PW")

    uri = "mongodb+srv://" + user + ":" + pw + "@cluster0.gnkvv.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(uri)

    db = client.test
    times_coll = db.times_collection

    return times_coll
