import pymysql
from sina.settings import SCRAP_MYSQL_HOST, SCRAP_MYSQL_USER, SCRAP_MYSQL_PWD, SCRAP_MYSQL_DB


def mysql_con():
    conn = pymysql.connect(host=SCRAP_MYSQL_HOST, port=3306, user=SCRAP_MYSQL_USER, passwd=SCRAP_MYSQL_PWD,
                           db=SCRAP_MYSQL_DB,
                           charset='utf8')  # 将这里换为你的数据库地址
    return conn


def insert_sentence(dataset_id):
    sql = "INSERT INTO scrapinfo.scrap_info(id, dataset_id, create_time) VALUES (UUID(), '%s', now())" % (
        str(dataset_id))
    return sql


def close_mysql(cursor, conn):
    conn.commit()
    cursor.close()
    conn.close()


def insert_dataset(dataset_id):
    conn = mysql_con()
    cursor = conn.cursor()
    c = insert_sentence(dataset_id)
    effect_row = cursor.execute(c)
    print('Insert ' + str(effect_row) + ' rows')
    close_mysql(cursor, conn)


def get_latest_dataset_id():
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "SELECT dataset_id from scrapinfo.scrap_info order by create_time desc limit 1"
    cursor.execute(sentence)
    result = cursor.fetchone()
    close_mysql(cursor, conn)
    return str(result[0])


def get_second_latest_dataset_id():
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "SELECT dataset_id from scrapinfo.scrap_info order by create_time desc limit 2"
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
