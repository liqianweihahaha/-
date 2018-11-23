import requests
import time


tiger_api_host = 'https://backend-dev.codemao.cn'
platform_tiger_api_host = 'http://dev-external.platform.codemao.cn'

# 个人信息
user_username = 'mxq111'
user_password = 'm1234567'
user_wrong_password = '123'
user_id = 1000002450
user_id_str = "1000002450"
ide_published_work_id = 2675933
ide_unpublish_work_id = 2675934
ide_deleted_temporarily_work_id = 2675935
ide_deleted_permanently_work_id = 2675938
wood_work_id = 2676059
# 用户拥有的精灵，不拥有的精灵
user_owned_sprite_id = 50
user_unown_sprite_id = 1

# 另一人信息
other_published_work_id = 2675915
other_user_id = 1000002872

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


user_login_token = login_token(user_username, user_password)
