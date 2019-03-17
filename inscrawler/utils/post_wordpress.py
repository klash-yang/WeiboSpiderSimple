import inscrawler.utils.wordpress_operation as wordpress_operation
import inscrawler.utils.scrap_info_operation as scrap_info_operation
import inscrawler.utils.mongodb_operation as mongodb_operation


def transfer_to_mysql():
    # 假如需要异地开发，就把dataset_id换成需要的 '270dd05e-48b7-11e9-b4c9-4c3275997092'
    # latest_dataset_id = scrap_info_operation.get_latest_dataset_id('edcee3000', 'Instagram')
    latest_dataset_id = '270dd05e-48b7-11e9-b4c9-4c3275997092'
    db = mongodb_operation.get_mongo_db()
    records = db['ins'].find({"dataset_id": latest_dataset_id}).sort("dateTime", -1)
    for record in records:
        ins_id = record['ins_id']
        pic_loacation = record['pic_loacation']
        author = record['author']
        pic_wp_id = wordpress_operation.post_picture(dataset_id=latest_dataset_id, pic_loacation=pic_loacation, pic_ins_id=ins_id, category=author)
        sentence = "select * from scrapinfo.ins_pic_info where dataset_id = '%(latest_dataset_id)s'" \
                   % {
                       'latest_dataset_id': latest_dataset_id

                   }
        # content_list = ['<!-- wp:paragraph -->\n',
        #                 '<!-- wp:image {"id":424} -->\n',
        #                 '<figure class="wp-block-image"><img src="https://www.onedaycp.com/wp-content/uploads/2019/03/picture-819x1024.jpg" alt="" class="wp-image-424"/></figure>\n\n']

        content_list = ['<!-- wp:paragraph -->\n',
                        '<!-- wp:image {"id":%{pic_wp_id}s} -->\n' % {pic_wp_id},
                        '<figure class="wp-block-image"><img src="https://www.onedaycp.com/wp-content/uploads/2019/03/picture-819x1024.jpg" alt="" class="wp-image-424"/></figure>\n\n']

        blogger_id = tweet['']
        blogger_info = list(db['Information'].find({"dataset_id": latest_dataset_id, "blogger_id": blogger_id}))[0]
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
        categories = []  # 孙笑川
        # categories.insert(1, blogger_info['nick_name'])
        print(blogger_info['nick_name'])
        categories.append(blogger_info['nick_name'])
        # categories = mat(categories)
        previous_post_ids = scrap_info_operation.get_post_ids(weibo_url=tweet_url)
        wordpress_operation.delete_wordpress(post_id_list=previous_post_ids)
        post_id = wordpress_operation.post_wordpress(title, content, 'publish', 'open', post_tags, categories)
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
