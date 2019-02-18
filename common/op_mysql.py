import pymysql

class OpMysql(object):
    # 连接ali云数据库，使用云数据库外网地址
    def __init__(self, host, user, password, database):
        try:
            self.conn = pymysql.connect(host=host, user=user, password=password, database,charset='utf-8')
            self.cur = self.conn.cursor()
        except pymysql.Error as e:
            print('err')



if __name__ == '__main__':
    opmysql = OpMysql()