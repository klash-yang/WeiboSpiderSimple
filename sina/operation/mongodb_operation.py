import pymongo
from sina.settings import LOCAL_MONGO_HOST, LOCAL_MONGO_PORT, DB_NAME


def get_mongo_db():
    client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)
    db = client[DB_NAME]
    return db


def delete_twitter_rec(dataset_id, weibo_url):
    db = get_mongo_db()
    delete_num = db['Tweets'].delete_many({"dataset_id": dataset_id, "weibo_url": weibo_url})
    print('Delete %s tweets' % delete_num)


def delete_comment_under_twitter(dataset_id, weibo_url):
    db = get_mongo_db()
    delete_num = db['Comments'].delete_many({"dataset_id": dataset_id, "weibo_url": weibo_url})
    print('Delete %s comments' % delete_num)
