import requests
import os
from common import read_config
from common.util import *
from common.environment import *
from builtins import str

# 读取 .env 配置
env = os.environ['environment']

# 获取测试hosts
def tiger_api_host():
    return get_hosts(env).get('tiger_api_host')

def platform_tiger_api_host():
    return get_hosts(env).get('platform_tiger_api_host')

# 源用户信息
def source_user():
    return read_config.source_user(env)

def source_user_id():
    return source_user().get('id')

def source_user_username():
    return source_user().get('username')

def source_user_email():
    return source_user().get('email')

def source_user_password():
    return source_user().get('password')

# # Kitten作品
# source_user_ide_published_work_id = source_user.get('work').get('ide').get('published_work_id')
# source_user_ide_unpublish_work_id = source_user.get('work').get('ide').get('unpublish_work_id')
# source_user_ide_deleted_temporarily_work_id = source_user.get('work').get('ide').get('deleted_temporarily_work_id')
# source_user_ide_deleted_permanently_work_id = source_user.get('work').get('ide').get('deleted_permanently_work_id')
# source_user_ide_work_url = source_user.get('work').get('ide').get('work_url')
# source_user_ide_preview_url = source_user.get('work').get('ide').get('preview_url')
# source_user_ide_bcmc_url = source_user.get('work').get('ide').get('bcmc_url')
# # box1.0
# source_user_boxv1_work_url = source_user.get('work').get('boxv1').get('work_url')
# source_user_boxv1_preview_url = source_user.get('work').get('boxv1').get('preview_url')
# # box2.0
# source_user_boxv2_published_work_id = source_user.get('work').get('boxv2').get('published_work_id')
# source_user_boxv2_work_url = source_user.get('work').get('boxv2').get('work_url')
# source_user_boxv2_preview_url = source_user.get('work').get('boxv2').get('preview_url')
# source_user_boxv2_bcmc_url = source_user.get('work').get('boxv2').get('bcmc_url')
# # wood
# source_user_wood_work_id = source_user.get('work').get('wood').get('work_id')
# # nemo
# source_user_nemo_work_id = source_user.get('work').get('nemo').get('work_id')
# source_user_nemo_work_url = source_user.get('work').get('nemo').get('work_url')
# source_user_nemo_preview_url = source_user.get('work').get('nemo').get('preview_url')
# # 用户拥有的精灵，不拥有的精灵
# source_user_owned_sprite_id = source_user.get('sprite').get('owned')
# source_user_unown_sprite_id = source_user.get('sprite').get('unown')

# 目标用户信息
def target_user():
    return read_config.target_user(env)

def target_user_id():
    return target_user().get('id')

def target_user_username():
    return target_user().get('username')

def target_user_password():
    return target_user().get('password')
# Kitten作品
# target_user_ide_published_work_id = target_user.get('work').get('ide').get('published_work_id')
# target_user_ide_published_unfork_work_id = target_user.get('work').get('ide').get('published_unfork_work_id')
# target_user_ide_unpublish_work_id = target_user.get('work').get('ide').get('unpublish_work_id')
# target_user_ide_deleted_temporarily_work_id = target_user.get('work').get('ide').get('deleted_temporarily_work_id')
# target_user_ide_deleted_permanently_work_id = target_user.get('work').get('ide').get('deleted_permanently_work_id')
# # nemo作品
# target_user_nemo_work_id = target_user.get('work').get('nemo').get('work_id')

def content_type():
    return 'application/json'

# # 获取登录token
# def login_token(identity, password, pid='UvOFXx2tfv'):
#     data = {
#         "identity": identity,
#         "password": password,
#         "pid": pid
#     }
#     params = {'Content-Type': 'application/json'}  
#     res = requests.post(get_tiger_api_host()+'/tiger/accounts/login', json=data, params=params)
#     if res.status_code == 200 and 'application/json' in res.headers['Content-Type']:
#         token = res.json()['token']
#         bearer_token = 'Bearer '+ token
#         return bearer_token

# source_user_login_token = login_token(source_user_username, source_user_password)

# # 取消收藏作品
# def uncollection_work(work_id):
#     res = requests.delete(get_tiger_api_host()+'/api/work/collection/'+str(work_id), headers={'Authorization': source_user_login_token})
#     if res.status_code == 200:
#         if res.json()['code'] == 200:
#             return True
#         elif res.json()['code'] == 500:
#             print('用户未收藏此作品')
#             return False
#     else:
#         print('用户取消收藏作品失败，返回状态码：%s' % res.status_code)
#         return False

# # 收藏作品
# def collection_work(work_id):
#     res = requests.post(get_tiger_api_host()+'/api/work/collection/'+str(work_id), headers={'Authorization': source_user_login_token})
#     if res.status_code == 200:
#         if res.json()['code'] == 200:
#             return True
#         elif res.json()['code'] == 2001:
#             print('用户已收藏此作品')
#             return False
#     else:
#         print('用户收藏作品失败，返回状态码：%s' % res.status_code)
#         return False

# # 删除作品业务标志位
# def delete_work_business_relation(timestamp, user_id, work_id):
#     signature = business_relation_signature(timestamp, user_id, work_id)
#     res = requests.delete(get_tiger_api_host()+'/tiger/work/business/relation?business=CONTEST&timestamp=%s&user_id=%s&work_id=%s&signature=%s' % (timestamp, user_id, work_id, signature))
#     if res.status_code == 204:
#         return True
#     else:
#         print('删除作品业务标志位失败，状态码：%s，请求url: %s' % (res.status_code), res.url)
#         return False

# # 判断是否是dev或者test环境
# def is_dev():
#     stat = True if env in ('dev', 'test') else False
#     return stat