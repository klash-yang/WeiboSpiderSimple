import sina.operation.wordpress_post as wordpress_post
import sina.operation.scrap_info_operation as scrap_info_operation
import sina.operation.mongodb_operation as mongodb_operation
import uuid


def transfer_to_mysql():
    latest_dataset_id = scrap_info_operation.get_latest_dataset_id()
    db = mongodb_operation.get_mongo_db()
    tweets = db['Tweets'].find({"dataset_id": latest_dataset_id})
    for tweet in tweets:
        tweet_url = tweet['weibo_url']
        blogger_id = tweet['blogger_id']
        blogger_info = list(db['Information'].find({"dataset_id": latest_dataset_id, "blogger_id": blogger_id}))
        print(blogger_info)
        comments = db['Comments'].find({"dataset_id": latest_dataset_id, "weibo_url": tweet_url})
        title = tweet['content']
        content_list = ['<!-- wp:paragraph -->\n', '<p>评论:</p>\n', '<!-- /wp:paragraph -->\n\n']
        for comment in comments:
            content_list.append('<!-- wp:paragraph -->\n')
            content_list.append('<p>%(nick_name)s: %(content)s</p>\n' % {'nick_name': comment['nick_name'],
                                                                         'content': comment['content']})
            content_list.append('<!-- /wp:paragraph -->\n\n')
        content = ''.join(content_list)
        print(content)
        post_tags = []
        categories = [] # 孙笑川
        # categories.insert(1, blogger_info['nick_name'])

        categories.append(blogger_info['nick_name'])
        post_id = wordpress_post.post_wordpress(title, content, 'publish', 'open', post_tags, blogger_info['nick_name'])
        scrap_info_operation.insert_mapping_record(post_id, latest_dataset_id, tweet_url, blogger_info['nick_name'])

        # 假如之前存在多个此微博的postid,则全部删除了然后再插入新的

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
