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
    return str(result[1])


print(get_second_latest_dataset_id())

