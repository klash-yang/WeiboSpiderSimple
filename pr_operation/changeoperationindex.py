# import pymssql as pymssql
#
# server = "10.157.107.11:1801"  # 连接服务器地址
# user = "sa"  # 连接帐号
# password = "P@ss1234"  # 连接密码
# db_name = "PRSystemDev"
#
# conn = pymssql.connect(host=server, user=user, password=password, database=db_name, charset="utf8")
#
# cursor = conn.cursor()  # 获取光标
#
# sentence = "select ID, Code, PositionIndex from PermissionOld where PLevel = 2"
#
# cursor.execute(sentence)
# parents = cursor.fetchall()
#
# for parent in parents:
#     parent_id = parent[0]
#     print(parent_id)
#     sentence = "select ID, Code, PositionIndex from PermissionOld where PLevel = 3 and ParentID = '%s'" % (parent_id)
#     cursor.execute(sentence)
#     sons = cursor.fetchall()
#     for son in sons:
#         print(son)
#
#
#     # sentence = "select ID, Code, PositionIndex from PermissionOld where PLevel = 3 and ParentID =" + row[0]
#     # cursor.execute(sentence)
#     # for row in cursor:
#     #     print(row)
#
# conn.close()
