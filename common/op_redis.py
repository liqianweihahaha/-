# python连接redis
import redis

class OpRedis(object):
    # dev环境，默认连接redis实例下面的第一个数据库
    def __init__(self, host='dev.codemao.cn', port=7000, db=0):
        # decode_responses=True,写入键值对中的value为str类型，不加这个参数写入的则为字节类型
        pool = redis.ConnectionPool(host=host, port=port, db=db, decode_responses=True)
        self.r = redis.Redis(connection_pool=pool)
 
    # 获取登录、注册等验证码
    def get_captcha(self, captcha_type, phone_number):
        r_key = 'platform:account:captcha:'+str(captcha_type)+':'+str(phone_number)
        h_key = 'captcha'
        captcha_value = self.r.hget(r_key, h_key)
        if captcha_value != None:
            return captcha_value
        else:  
            print('手机号：%s, 对应的验证码redis中不存在')
            return ''   

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