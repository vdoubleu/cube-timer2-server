from pymongo import MongoClient
import os

def connect():
    user = os.getenv("DBUSER")
    pw = os.getenv("DBPW")

    #uri = "mongodb+srv://" + user + ":" + pw + "@cluster0.gnkvv.mongodb.net/test?retryWrites=true&w=majority"
    uri = "mongodb+srv://vdoubleu:passwordVW12345@cluster0.gnkvv.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(uri)

    db = client.test
    times_coll = db.times_collection

    return times_coll
