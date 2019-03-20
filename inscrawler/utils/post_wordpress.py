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
        pic_loacation = record['pic_location']
        author = record['author']
        pic_bed_url = wordpress_operation.post_picture(dataset_id=latest_dataset_id, pic_loacation=pic_loacation,
                                                       pic_ins_id=ins_id, category=author)



        content_list = ['< !-- wp:image -->\n',
                        '< figure class ="wp-block-image" > < img src="%{pic_bed_url}s}" alt="" / > < / figure >\n' % {
                            pic_bed_url},
                        '< !-- / wp: image -->\n\n']

        blogger_id = records['_id']
        print(blogger_id)
        comments = record['commentMessage']
        title = record['title']
        content_list.append(['<!-- wp:paragraph -->\n', '<p>评论:</p>\n', '<!-- /wp:paragraph -->\n\n'])
        for comment in comments:
            content_list.append('<!-- wp:paragraph -->\n')
            content_list.append('<p>%(content)s</p>\n' % {'content': comment})
            content_list.append('<!-- /wp:paragraph -->\n\n')
        content = ''.join(content_list)
        print(content)
        post_tags = []
        categories = []  # 孙笑川
        print(author)
        categories.append(author)
        # categories = mat(categories)
        previous_post_ids = scrap_info_operation.get_previous_post_ids(this_dataset=latest_dataset_id, title_id=ins_id)
        wordpress_operation.delete_wordpress(post_id_list=previous_post_ids)
        post_id = wordpress_operation.post_wordpress(title, content, 'publish', 'open', post_tags, categories)
        scrap_info_operation.insert_mapping_record(post_id=post_id, dataset_id=latest_dataset_id, title_id=ins_id,
                                                   category=author)
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
