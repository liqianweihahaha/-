import pymysql

class OpMysql(object):
    # 连接ali云数据库，使用云数据库外网地址
    def __init__(self, host, user, password, database):
        try:
            self.conn = pymysql.connect(host=host, user=user, password=password, database=database)
            self.cur = self.conn.cursor()
        except pymysql.Error as e:
            print('connect mysql error')

    def select_one(self, query, params=None):
        try:
            result = self.cur.execute(query, params)
            if result > 1:
                print('找到多条数据')
            elif result == 1:
                return self.cur.fetchone()
            else:
                # 查询到的结果为0
                print('找不到符合条件的数据')
        except BaseException as e:
            return '001'

    # 清除用户的手机号
    def clear_phone_number(self, phone_number):
        result = self.cur.execute('UPDATE basic_auth SET phone_number=%s WHERE phone_number=%s', (None, phone_number,))
        if self.cur.rowcount == 1:
            self.conn.commit()

    # 获取work_base表的作品信息，用于判断workclub生产MQ和workcore消费MQ是否成功
    # def get_work_from_work_base(self, work_id):
    #     result = self.cur.execute('SELECT * FROM work_base WHERE id=%s', (work_id,))
    #     if self.cur.rowcount == 1:
    #         return self.cur.fetchone()
    #     else：
    #         return False


if __name__ == '__main__':
    # 连接dev环境
    opmysql = OpMysql(host='rm-bp173j25673ah67z8ko.mysql.rds.aliyuncs.com', user='TestDep', password='4Ehp1ndpfnlN9D0qvg4SZuig', database='account')
    data = opmysql.select_one("SELECT * from basic_auth where user_id=%s", (1000002450, ))
    print(data)