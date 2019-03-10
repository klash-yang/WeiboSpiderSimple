import pymongo
from inscrawler.settings import LOCAL_MONGO_HOST, LOCAL_MONGO_PORT, DB_NAME


def get_mongo_db():
    client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)
    db = client[DB_NAME]
    return db
