import pymysql


class CreateDataset:

    def __init__(self, dataset_id):
        self.dataset_id = dataset_id

    def mysql_con(self):
        conn = pymysql.connect(host='132.232.113.103', port=3306, user='scrapinfo', passwd='KEBjhAPk2bZtaAG3',
                               db='scrapinfo',
                               charset='utf8')  # 将这里换为你的数据库地址
        return conn

    def sentence(self):
        sql = "INSERT INTO scrapinfo.scrap_info(id, dataset_id, create_time) VALUES (UUID(), '%s', now())" % (str(self.dataset_id))
        return sql

    def close_mysql(self, cursor, conn):
        conn.commit()
        cursor.close()
        conn.close()

    def execute(self):
        conn = self.mysql_con()
        cursor = conn.cursor()
        c = self.sentence()
        effect_row = cursor.execute(c)
        print('Insert ' + str(effect_row) + ' rows')
        self.close_mysql(cursor, conn)

# a = CreateDataset("99999")
# a.execute()

