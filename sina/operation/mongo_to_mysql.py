import pymongo
import pymysql
from sina.settings import SCRAP_MYSQL_HOST, SCRAP_MYSQL_USER, SCRAP_MYSQL_PWD, SCRAP_MYSQL_DB,LOCAL_MONGO_HOST, LOCAL_MONGO_PORT, DB_NAME

class MongoToMysql:

    def mysql_con(self):
        conn = pymysql.connect(host=SCRAP_MYSQL_HOST, port=3306, user=SCRAP_MYSQL_USER, passwd=SCRAP_MYSQL_PWD,
                               db=SCRAP_MYSQL_DB,
                               charset='utf8')  # 将这里换为你的数据库地址
        return conn

    def close_mysql(self, cursor, conn):
        conn.commit()
        cursor.close()
        conn.close()

    def get_latest_dataset_id(self):    # 获取最新的Dataset ID
        conn = self.mysql_con()
        cursor = conn.cursor()
        sentence = "SELECT dataset_id from scrapinfo.scrap_info order by create_time desc limit 1"
        cursor.execute(sentence)
        result = cursor.fetchone()
        self.close_mysql(cursor, conn)
        return str(result[0])

    def get_mongo_db(self):
        client = pymongo.MongoClient(LOCAL_MONGO_HOST, LOCAL_MONGO_PORT)
        db = client[DB_NAME]
        return db

    def transfer_to_mysql(self, table_name):
        db = self.get_mongo_db()
        table = db[table_name]
        items = table.find()
        for item in items:
            print(item)


a = MongoToMysql()
a.transfer_to_mysql('Tweets')



# client = pymongo.MongoClient(host='localhost', port=27017)
# mydb = client['Sina']
# mycol = mydb['Tweets']
# my_query = {"dataset_id": "9ce8aa50-3849-11e9-b056-e0d55eb10729"}
# # my_query = {"1748526937_GxfZpelkd}
# result = mycol.find()
# for item in result:
#     print(item)
