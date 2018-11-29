import requests
import time


def get_value(content, key):
    if isinstance(content, dict):
        return content.get(key)

# 获取时间戳
def get_timeslot(time_date):
    return int(time.mktime(time.strptime(str(time_date), '%Y-%m-%d')))

def eval_content(content):
    return eval(content)