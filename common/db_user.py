# from op_mysql import *
# from debugtalk import env

# mysql_conf = config_mysql(env)
# opmysql = OpMysql(host=mysql_conf['host'], user=mysql_conf['user'], password=mysql_conf['password'], database='account')

# # 用户基本信息
# def user_info(user_id):
#     data = opmysql.select_one('SELECT * FROM user WHERE id=%s', (user_id,))
#     user_data = {
#         "id": data(0),
#         "bcmid": data(1),
#         "nickname": data(2),
#         "fullname": data(3),
#         "avatar_url": data(4),
#         "birthday": data(5),
#         "sex": data(6),
#         "qq": data(7),
#         "description": data(8),
#         "product_id": data(9),
#         "remark": data(10)
#     }
#     return data_extension

# # 用户扩展信息
# def user_extension_info(user_id):
#     data = opmysql.select_one('SELECT * FROM user_extension WHERE user_id=%s', (user_id,))
#     data_extension = {
#         "id": data(0),
#         "user_id": data(1),
#         "gold": data(2),
#         "masonry": data(3),
#         "age": data(4),
#         "preview_work_id": data(5),
#         "doing": data(6),
#         "grade": data(7),
#         "mlz_name": data(8),
#         "familiar_sprite": data(9)
#     }
#     return data_extension