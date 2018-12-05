import requests
import time
import hmac
import hashlib
import json


# 获取某具体时间的时间戳
def get_timeslot(time_date):
    return int(time.mktime(time.strptime(str(time_date), '%Y-%m-%d')))

# 返回当前时间戳的后3分钟，用于测试删除作品业务标志位
def timestamp_3minutes():
    return int(time.time()+180)

# 生成删除作品业务标志位的秘钥
def generate_signature(timestamp, user_id, work_id):
    key = '9DMC9R0xXSbJ5tgzpA6UrXYA43hZRVJQ'
    msg = "business=%s&timestamp=%s&user_id=%s&work_id=%s" % ('CONTEST', timestamp, user_id, work_id)
    signature = hmac.new(key.encode('utf-8'), msg.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    return signature

# 判断两个值是否相等
def eval_equal(source, target):
    return source == target

# 测试国家数字教育资源接入：获取ticket
# www.codemao.cn?ticket={ticket}即可登录对应账号
def get_eduyun_ticket(account='test_account', password='123456'):
    host = 'http://system.eduyun.cn/bmp-web'
    user = {
        'account': account,
        'password': password
    }
    res = requests.post(host+'/debugTool/createTicket', data=user)
    ticket = ''
    if res.status_code == 200 and 'application/json' in res.headers['Content-Type']:
        # 注意返回的res.json()['data']['data']，格式为str，需要转为dict
        ticket = json.loads(res.json()['data']['data'])['data']['ticket']
    else:
        print('获取国家数字教育资源账号的ticket失败，状态码：%s' % res.status_code)
    return ticket

if __name__ == '__main__':
    # timestamp = int(time.time()+180)
    # print(generate_signature(timestamp, 1000002450, 2675933))
    print(get_eduyun_ticket())