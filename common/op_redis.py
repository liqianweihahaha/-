# python连接redis
import redis

class OpRedis(object):
    # dev环境，默认连接redis实例下面的第一个数据库
    def __init__(self, host, port, password, db):
        password = None if password == '' else password
        # decode_responses=True,写入键值对中的value为str类型，不加这个参数写入的则为字节类型
        pool = redis.ConnectionPool(host=host, port=port, password=password, db=db, decode_responses=True)
        self.r = redis.Redis(connection_pool=pool)

    # 获取账号3.0登录、注册等验证码，value为hash类型
    def get_captcha_account_v3(self, captcha_type, phone_number):
        r_key = 'platform:account:captcha:'+str(captcha_type)+':'+str(phone_number)
        h_key = 'captcha'
        captcha_value = self.r.hget(r_key, h_key)
        if captcha_value != None:
            return captcha_value
        else:
            # print('Redis中未获取到手机号：%s 对应的验证码' % phone_number)
            pass

    # 获取账号2.0登录、注册等验证码，value为string类型
    def get_captcha_account_v2(self, captcha_type, phone_number):
        key_name = 'tiger:account:captcha:'+str(captcha_type)+':'+str(phone_number)
        captcha_value = self.r.get(key_name)
        if captcha_value != None:
            return captcha_value
        else:
            # print('Redis中未获取到手机号：%s 对应的验证码' % phone_number)
            pass

    # 获取产品信息
    # return: List
    def get_product_info(self, pid):
        r_key = 'platform:account:product_info:'+str(pid)
        pid_info = self.r.hmget(r_key, ['id', 'name', 'description'])
        if pid_info[0] != None:
            return pid_info


if __name__ == '__main__':
    op_redis = OpRedis(host='dev.codemao.cn', port=7000, db=1)
    print(op_redis.get_product_info('-8ZfYfLG'))