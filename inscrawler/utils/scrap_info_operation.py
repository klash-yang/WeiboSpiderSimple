import pymysql
from sina.settings import SCRAP_MYSQL_HOST, SCRAP_MYSQL_USER, SCRAP_MYSQL_PWD, SCRAP_MYSQL_DB


def mysql_con():
    conn = pymysql.connect(host=SCRAP_MYSQL_HOST, port=3306, user=SCRAP_MYSQL_USER, passwd=SCRAP_MYSQL_PWD,
                           db=SCRAP_MYSQL_DB,
                           charset='utf8')  # 将这里换为你的数据库地址
    return conn


def close_mysql(cursor, conn):
    conn.commit()
    cursor.close()
    conn.close()


def insert_dataset(dataset_id, category, project):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "insert into scrapinfo.dataset_info(id, dataset_id, category, project, create_time) " \
               "VALUES (uuid(), '%(dataset_id)s', '%(category)s', '%(project)s', now())" \
               % {
                   'dataset_id': dataset_id,
                   'category': category,
                   'project': project
               }
    effect_row = cursor.execute(sentence)
    print('Insert ' + str(effect_row) + ' rows')
    close_mysql(cursor, conn)


def get_latest_dataset_id(category, project):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "SELECT dataset_id from scrapinfo.dataset_info " \
               "where category = '%(category)s' and project = '%(project)s' order by create_time desc limit 1" \
               % {
                   'category': category,
                   'project': project
               }
    cursor.execute(sentence)
    result = cursor.fetchone()
    close_mysql(cursor, conn)
    return str(result[0])


def get_second_latest_dataset_id(category, project):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "SELECT dataset_id from scrapinfo.dataset_info order by create_time desc limit 2"
    cursor.execute(sentence)
    result = cursor.fetchall()
    close_mysql(cursor, conn)
    if result.__len__() == 0:
        return None
    else:
        return str(result[0])


def get_previous_post_ids(this_dataset, weibo_url):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "SELECT post_id from scrapinfo.post_info where weibo_url = '%(weibo_url)s' and dataset_id != '%(dataset_id)s' order by create_time desc " \
               % {
                   'dataset_id': this_dataset,
                   'weibo_url': weibo_url,
               }
    cursor.execute(sentence)
    result = list(cursor.fetchall())
    close_mysql(cursor, conn)
    return result


def get_post_ids(weibo_url):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "SELECT post_id from scrapinfo.post_info where weibo_url = '%(weibo_url)s'" \
               % {
                   'weibo_url': weibo_url,
               }
    cursor.execute(sentence)
    result = list(cursor.fetchall())
    close_mysql(cursor, conn)
    return result


def insert_mapping_record(post_id, dataset_id, weibo_url, category):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "INSERT INTO scrapinfo.post_info(id, post_id, dataset_id, weibo_url, category, create_time) " \
               "VALUES (UUID(), '%(post_id)s', '%(dataset_id)s', '%(weibo_url)s', '%(category)s', now())" % {
                   'post_id': post_id, 'dataset_id': dataset_id, 'weibo_url': weibo_url,
                   'category': category
               }
    effect_row = cursor.execute(sentence)
    print('Insert ' + str(effect_row) + ' rows')
    close_mysql(cursor, conn)


def insert_pic_record(pic_wp_id, pic_ins_id, dataset_id, category):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "INSERT INTO scrapinfo.post_info(id, pic_wp_id, pic_ins_id, dataset_id, category, create_time)  " \
               "VALUES (UUID(), '%(pic_wp_id)s', '%(pic_ins_id)s', '%(dataset_id)s', '%(category)s', now())" % {
                   'pic_wp_id': pic_wp_id, 'pic_ins_id': pic_ins_id, 'dataset_id': dataset_id,
                   'category': category
               }
    effect_row = cursor.execute(sentence)
    print('Insert ' + str(effect_row) + ' rows')
    close_mysql(cursor, conn)

# print(get_second_latest_dataset_id())
# print(get_latest_dataset_id())
