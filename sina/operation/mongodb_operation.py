import pymongo
from sina.settings import LOCAL_MONGO_HOST, LOCAL_MONGO_PORT, DB_NAME


def get_mongo_db():
    client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)
    db = client[DB_NAME]
    return db


def delete_twitter_rec(weibo_url, dataset_id=None):
    db = get_mongo_db()

    if dataset_id is None:
        delete_num = db['Tweets'].delete_many({"weibo_url": weibo_url})
    else:
        delete_num = db['Tweets'].delete_many({"dataset_id": dataset_id, "weibo_url": weibo_url})

    print('Delete %s tweets' % delete_num)


def delete_previous_twitter_rec(weibo_url, current_dataset_id):
    db = get_mongo_db()

    delete_num = db['Tweets'].delete_many({"dataset_id": {"$ne": current_dataset_id}, "weibo_url": weibo_url})
    print('Delete %s tweets' % delete_num)


def delete_comment_under_twitter(weibo_url, dataset_id=None):
    db = get_mongo_db()

    if dataset_id is None:
        delete_num = db['Comments'].delete_many({"weibo_url": weibo_url})
    else:
        delete_num = db['Comments'].delete_many({"dataset_id": dataset_id, "weibo_url": weibo_url})

    print('Delete %s comments' % delete_num)


def delete_previous_comment_under_twitter(weibo_url, current_dataset_id):
    db = get_mongo_db()

    delete_num = db['Comments'].delete_many({"dataset_id": {"$ne": current_dataset_id}, "weibo_url": weibo_url})
    print('Delete %s comments' % delete_num)


def delete_user_info(blogger_id, dataset_id=None):
    db = get_mongo_db()

    if dataset_id is None:
        delete_num = db['Information'].delete_many({"blogger_id": blogger_id})
    else:
        delete_num = db['Information'].delete_many({"dataset_id": dataset_id, "blogger_id": blogger_id})

    print('Delete %s user info' % delete_num)


def delete_previous_user_info(blogger_id, current_dataset_id):
    db = get_mongo_db()

    delete_num = db['Information'].delete_many({"dataset_id": {"$ne": current_dataset_id}, "blogger_id": blogger_id})
    print('Delete %s user info' % delete_num)


# delete_previous_user_info()