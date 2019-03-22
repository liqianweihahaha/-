# python连接redis
import redis

class OpRedis(object):
    # dev环境，默认连接redis实例下面的第一个数据库
    def __init__(self, host='dev.codemao.cn', port=7000, db=0)
        pool = redis.ConnectionPool(host=host, port=port, db=db)
        self.r = redis.Redis(connection_pool=pool)
 
    # 获取登录、注册等验证码
    def get_captcha(self, captcha_ype, phone_number):
        hash_name = 'platform:account:captcha:'+str(captcha_ype)+':'+str(phone_number)
        key = 'captcha'
        captcha_value = self.r.hget(h_name, key)
        if captcha_value != None:
            return captcha_value.decode('utf-8')
        else:  
            print('手机号：%s, 对应的验证码redis中不存在')
            return ''   

    # 获取产品信息
    def get_product_info(self):
        # print(r.hmget('platform:account:product_info:-8ZfYfLG', ['id', 'name']))
        pass
            

if __name__ == '__main__':
    op_redis = OpRedis()
    print(op_redis)