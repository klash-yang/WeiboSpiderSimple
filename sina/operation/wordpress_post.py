import time

import pymysql


class WordpressPost:
    def __init__(self, tittle, content):
        self.tittle = tittle
        self.content = content

    def mysql_con(self):
        conn = pymysql.connect(host='132.232.113.103', port=3306, user='chouxiang', passwd='EYXHkjeKJD', db='chouxiang',
                               charset='utf8')  # 将这里换为你的数据库地址
        return conn

    def up(self):
        times = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        # 根据表名改
        sql = "INSERT INTO chouxiang.cx_posts(post_author,post_date,post_content,post_title,post_excerpt,post_status,comment_status,ping_status,post_name,to_ping,pinged,post_modified,post_content_filtered,post_parent,menu_order,post_type,comment_count) VALUES ('1','%s','%s','%s','','publish','open','open','%s','','','%s','','0','0','post','0')" % (
            str(times), str(self.content), str(self.tittle), str(self.tittle), str(times))
        return sql

    def update_guid(self, blog_id):
        guid = "https://www.onedaycp.com/?p=%s" % blog_id
        sql = "UPDATE chouxiang.cx_posts SET guid = '%s' WHERE ID = '%s'" % (guid, blog_id)
        return sql

    def cat(self, ids, cat):
        # 根据表名改
        sql = "INSERT INTO chouxiang.cx_term_relationships(object_id,term_taxonomy_id,term_order) VALUES (%s,%s,'0')" % (ids, cat)
        return sql

    def close_mysql(self, cursor, conn):
        conn.commit()
        cursor.close()
        conn.close()

    def execute(self):
        conn = self.mysql_con()
        cursor = conn.cursor()
        c = self.up()
        effect_row = cursor.execute(c)
        print('Insert ' + str(effect_row) + ' rows')
        new_id = cursor.lastrowid  # 这里是记录文章id以便设置文章的分类
        update_guid_sentence = self.update_guid(new_id)
        effect_row = cursor.execute(update_guid_sentence)
        print('Update ' + str(effect_row) + ' rows')
        d = self.cat(new_id, '1')
        effect_row = cursor.execute(d)
        print('Insert ' + str(effect_row) + ' rows')
        self.close_mysql(cursor, conn)


a = WordpressPost("孙狗", "孙狗司马")
a.execute()

# a = WordpressPost("孙笑川打奶奶", "孙笑川没得亲妈")  # 这里第一个参数是标题 第二个是文章内容
# conn = a.mysql_con()
# cursor = conn.cursor()
# c = a.up()
# effect_row = cursor.execute(c)
# new_id = cursor.lastrowid  # 这里是记录文章id以便设置文章的分类
# d = a.cat(new_id, '1')
# effect_row = cursor.execute(d)
# a.close_mysql(cursor, conn)
