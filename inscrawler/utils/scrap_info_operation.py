import pymysql
from inscrawler.settings import SCRAP_MYSQL_HOST, SCRAP_MYSQL_USER, SCRAP_MYSQL_PWD, SCRAP_MYSQL_DB


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


def get_previous_post_ids(this_dataset, title_id):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "SELECT post_id from scrapinfo.post_info where title_id = '%(title_id)s' and dataset_id != '%(dataset_id)s' order by create_time desc " \
               % {
                   'dataset_id': this_dataset,
                   'title_id': title_id,
               }
    cursor.execute(sentence)
    result = list(cursor.fetchall())
    close_mysql(cursor, conn)
    return result


def get_post_ids(title_id):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "SELECT post_id from scrapinfo.post_info where title_id = '%(title_id)s'" \
               % {
                   'title_id': title_id,
               }
    cursor.execute(sentence)
    result = list(cursor.fetchall())
    close_mysql(cursor, conn)
    return result


def insert_mapping_record(post_id, dataset_id, title_id, category):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "INSERT INTO scrapinfo.post_info(id, post_id, dataset_id, title_id, category, create_time) " \
               "VALUES (UUID(), '%(post_id)s', '%(dataset_id)s', '%(title_id)s', '%(category)s', now())" % {
                   'post_id': post_id, 'dataset_id': dataset_id, 'title_id': title_id,
                   'category': category
               }
    effect_row = cursor.execute(sentence)
    print('Insert ' + str(effect_row) + ' rows')
    close_mysql(cursor, conn)


def insert_pic_record(pic_ins_id, dataset_id, category, pic_url, delete_url, origin_url):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "INSERT INTO scrapinfo.ins_pic_info(id, pic_wp_id, pic_ins_id, dataset_id, category, pic_url, delete_url, origin_pic_url,create_time)  " \
               "VALUES (UUID(), null, '%(pic_ins_id)s', '%(dataset_id)s', '%(category)s', '%(pic_url)s', '%(delete_url)s', '%(origin_pic_url)s', now())" % {
                   'pic_ins_id': pic_ins_id, 'dataset_id': dataset_id,
                   'category': category, 'pic_url': pic_url,
                   'delete_url': delete_url, 'origin_pic_url': origin_url
               }
    effect_row = cursor.execute(sentence)
    print('Insert ' + str(effect_row) + ' rows')
    close_mysql(cursor, conn)


def check_pic_info(pic_ins_id):
    conn = mysql_con()
    cursor = conn.cursor()
    sentence = "SELECT * from scrapinfo.ins_pic_info where pic_ins_id = '%(pic_ins_id)s'" \
               % {
                   'pic_ins_id': pic_ins_id,
               }
    cursor.execute(sentence)
    result = list(cursor.fetchall())
    close_mysql(cursor, conn)
    return result
