import pprint

from pymongo import MongoClient

from config import uri


client = MongoClient(uri)
db = client.glasgow

duplicates = db.duplicate_mapreduce_coll.find({'value': {'$gt':1} })

for d in duplicates:
    dup_1 = db.scraped_tweets.find({'id_str': d['_id'] })[0]
    db.scraped_tweets.remove({"_id": dup_1._id})