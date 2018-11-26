import requests
import time
import os

from common import read_config

env = 'dev'

if env == 'dev':
    tiger_api_host = 'https://backend-dev.codemao.cn'
    platform_tiger_api_host = 'http://dev-external.platform.codemao.cn'
elif env == 'staging':
    tiger_api_host = 'https://backend-test.codemao.cn'
    platform_tiger_api_host = 'http://staging-internal.platform.codemao.cn'
elif env == 'production':
    tiger_api_host = 'https://api.codemao.cn'
    platform_tiger_api_host = 'http://internal.platform.codemao.cn'

source_user = read_config.source_user(env)
source_user_id = source_user.get('id')
source_user_username = source_user.get('username')
source_user_password = source_user.get('password')
# 用户拥有的精灵，不拥有的精灵
source_user_owned_sprite_id = source_user.get('sprite').get('owned')
source_user_unown_sprite_id = source_user.get('sprite').get('unown')
target_user = read_config.target_user(env)
target_user_id = target_user.get('id')



# 个人信息
# user_username = 'mxq111'
# user_password = 'm1234567'
# user_wrong_password = '123'
# user_id = 1000002450
# user_id_str = "1000002450"
# ide_published_work_id = 2675933
# ide_unpublish_work_id = 2675934
# ide_deleted_temporarily_work_id = 2675935
# ide_deleted_permanently_work_id = 2675938
# wood_work_id = 2676059

# user_username = 'sandy123456'
# user_password = 'm1234567'
# user_wrong_password = '123'
# user_id = 956856
# user_id_str = "956856"
# ide_published_work_id = 2675933
# ide_unpublish_work_id = 2675934
# ide_deleted_temporarily_work_id = 2675935
# ide_deleted_permanently_work_id = 2675938
# wood_work_id = 2676059




# 另一人信息
other_user_id = 1000002872
other_user_username = 'mxq121'
other_published_work_id = 2675915
other_published_unfork_work_id = 2676251
other_unpublish_work_id = 2676253
other_deleted_temporarily_work_id = 2676255
other_deleted_permanently_work_id = 2676257




# 异常信息：不存在、格式错误
unexist_user_id = 100
unexist_user_username = 'a00000'
unexist_work_id = 100
unexist_sprite_id = 100
wrong_type_user_id = 'aaa'
wrong_type_work_id = 'aaa'
wrong_type_user_ids = 'aaa'
wrong_type_fields= '{}'
wrong_type_work_ids = '{}'
wrong_type_fields_element = ''
wrong_type_sprite_id = 'aaa'
unsupport_fields_element = 'aaa'



start_time = int(time.mktime(time.strptime('2018-11-22', '%Y-%m-%d')))
end_time = int(time.mktime(time.strptime('2018-11-23', '%Y-%m-%d')))

# pid信息
pc_pid = 'UvOFXx2tfv'
web_pid = '65edCTyg'
ide_work_type = 1

content_type = 'application/json'


# 获取登录token
def login_token(identity, password, pid='UvOFXx2tfv'):
    data = {
        "identity": identity,
        "password": password,
        "pid": pid
    }
    params = {'Content-Type': 'application/json'}  
    res = requests.post(tiger_api_host+'/tiger/accounts/login', json=data, params=params)
    if res.status_code == 200 and 'application/json' in res.headers['Content-Type']:
        token = res.json()['token']
        bearer_token = 'Bearer '+ token
        return bearer_token


user_login_token = login_token(source_user_username, source_user_password)


def get_value(content, key):
    if isinstance(content, dict):
        return content.get(key)


# 获取用户的某ide作品的详细信息
def work_info(work_id, work_type_id=1):
    # 获取用户某作品信息
    res = requests.get(tiger_api_host+'/tiger/work/list?type='+str(work_type_id), headers={'Authorization': user_login_token})
    if res.status_code == 200:
        for i in res.text:
            print(i)
            if i['id'] == work_id:
                work_info = {
                    "id": i["id"],
                    "name": i["name"],
                    "type": i["type"],
                    "is_old": i["is_old"],
                    "preview": i["preview"],
                    "status": i["status"],
                    "publish_time": i["publish_time"]
                }
                return work_info

def eval_content(content):
    return eval(content)


