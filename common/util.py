import requests
import time
import hmac
import hashlib


def get_value(content, key):
    if isinstance(content, dict):
        return content.get(key)

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


if __name__ == '__main__':
    timestamp = int(time.time()+180)
    print(generate_signature(timestamp, 1000002450, 2675933))