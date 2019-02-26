import pymongo
import pymysql
from sina.settings import SCRAP_MYSQL_HOST, SCRAP_MYSQL_USER, SCRAP_MYSQL_PWD, SCRAP_MYSQL_DB, LOCAL_MONGO_HOST, \
    LOCAL_MONGO_PORT, DB_NAME
import sina.operation.wordpress_post as wordpress_post


def mysql_con():
    conn = pymysql.connect(host=SCRAP_MYSQL_HOST, port=3306, user=SCRAP_MYSQL_USER, passwd=SCRAP_MYSQL_PWD,
                           db=SCRAP_MYSQL_DB,
                           charset='utf8')  # 将这里换为你的数据库地址
    return conn


def close_mysql(cursor, conn):
    conn.commit()
    cursor.close()
    conn.close()


def get_latest_dataset_id():  # 获取最新的Dataset ID
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "SELECT dataset_id from scrapinfo.scrap_info order by create_time desc limit 1"
    cursor.execute(sentence)
    result = cursor.fetchone()
    close_mysql(cursor, conn)
    return str(result[0])


def get_mongo_db():
    client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)
    db = client[DB_NAME]
    return db


def transfer_to_mysql():
    latest_dataset_id = get_latest_dataset_id()
    db = get_mongo_db()
    tweets = db['Tweets'].find({"dataset_id": latest_dataset_id})
    for tweet in tweets:
        tweet_url = tweet['weibo_url']
        blogger_id = tweet['blogger_id']
        blogger_info = db['Information'].find({"dataset_id": latest_dataset_id, "blogger_id": blogger_id})[0]
        comments = db['Comments'].find({"dataset_id": latest_dataset_id, "weibo_url": tweet_url})
        title = tweet['content']
        content_list = []
        content_list.append('<!-- wp:paragraph -->\n')
        content_list.append('<p>评论:</p>\n')
        content_list.append('<!-- /wp:paragraph -->\n\n')
        for comment in comments:
            content_list.append('<!-- wp:paragraph -->\n')
            content_list.append('<p>%(nick_name)s: %(content)s</p>\n' % {'nick_name': comment['nick_name'],
                                                                         'content': comment['content']})
            content_list.append('<!-- /wp:paragraph -->\n\n')

            # content_list.append(comment['content'])
            # content_list.append('\n')

        content = ''.join(content_list)
        print(content)
        post_tags = []
        categories = []  # 孙笑川
        categories.append(blogger_info['nick_name'])
        wordpress_post.post_wordpress(title, content, 'publish', post_tags, categories)

        # comments = db['CommentItem'].find(latest_dataset_id)


transfer_to_mysql()

# items = table.find()
# content = []
# content.append('yang')
# content.append('cheng')
# print(content)
# for item in items:
#     # print(item)
#     content.append(item)


# a = 'dasdasdasdasd'
# salt = crypt.mksalt(crypt.METHOD_SHA512)
# hash = crypt.crypt("helloworld", salt)
# print(hash)


# {"dataset_id": "6f3d77ba-3910-11e9-bfef-e0d55eb10729"}
# client = pymongo.MongoClient(host='localhost', port=27017)
# mydb = client['Sina']
# mycol = mydb['Tweets']
# my_query = {"dataset_id": "9ce8aa50-3849-11e9-b056-e0d55eb10729"}
# # my_query = {"1748526937_GxfZpelkd}
# result = mycol.find()
# for item in result:
#     print(item)
