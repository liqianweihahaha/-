import os
from common import read_config
from common.util import *
from common.environment import *
from common.db_user import *
from common.op_mysql import OpMysql
from common.op_redis import OpRedis

# 读取 .env 配置
TEST_ENV = os.environ['environment']
# 因为会发送验证码，所以最好是用自己的手机号测试
TEST_PHONE_NUMBER = os.environ['test_phone_number']

# 获取测试域名hosts
TIGER_API_HOST = get_hosts(TEST_ENV).get('tiger_api_host')
PLATFORM_TIGER_API_HOST = get_hosts(TEST_ENV).get('platform_tiger_api_host')
INTERNAL_ACCOUNT_API_HOST = get_hosts(TEST_ENV).get('internal_account_api_host')
TRANSACTION_ADMIN_API_HOST = get_hosts(TEST_ENV).get('transaction_admin_api_host')

def test_phone_number():
    return TEST_PHONE_NUMBER

def tiger_api_host(): 
    return TIGER_API_HOST

def platform_tiger_api_host(): 
    return PLATFORM_TIGER_API_HOST

def internal_account_api_host():
    return INTERNAL_ACCOUNT_API_HOST

def transaction_admin_api_host():  
    return TRANSACTION_ADMIN_API_HOST

# 获取配置文件：源用户信息
source_user = read_config.source_user(TEST_ENV)
target_user = read_config.target_user(TEST_ENV)

def source_user_id():
    return source_user.get('id')

def source_user_username():
    return source_user.get('username')

def source_user_email():
    return source_user.get('email')

def source_user_password():
    return source_user.get('password')

# 用户拥有的精灵，不拥有的精灵
def source_user_owned_sprite_id():
    return source_user.get('sprite').get('owned')

def source_user_unown_sprite_id():
    return source_user.get('sprite').get('unown')

# Kitten作品
def source_user_ide_published_work_id():
    return source_user.get('work').get('ide').get('published_work_id')

def source_user_ide_unpublish_work_id():
    return source_user.get('work').get('ide').get('unpublish_work_id')

def source_user_ide_deleted_temporarily_work_id():
    return source_user.get('work').get('ide').get('deleted_temporarily_work_id')

def source_user_ide_deleted_permanently_work_id():
    return source_user.get('work').get('ide').get('deleted_permanently_work_id')

def source_user_ide_work_url():
    return source_user.get('work').get('ide').get('work_url')

def source_user_ide_preview_url():
    return source_user.get('work').get('ide').get('preview_url')

def source_user_ide_bcmc_url():
    return source_user.get('work').get('ide').get('bcmc_url')

# box1.0作品
def source_user_boxv1_work_url():
    return source_user.get('work').get('boxv1').get('work_url')

def source_user_boxv1_preview_url():
    return source_user.get('work').get('boxv1').get('preview_url')

# box2.0作品
def source_user_boxv2_published_work_id():
    return source_user.get('work').get('boxv2').get('published_work_id')

def source_user_boxv2_unpublish_work_id():
    return source_user.get('work').get('boxv2').get('unpublish_work_id')

def source_user_boxv2_work_url():
    return source_user.get('work').get('boxv2').get('work_url')

def source_user_boxv2_preview_url():
    return source_user.get('work').get('boxv2').get('preview_url')

def source_user_boxv2_bcmc_url():
    return source_user.get('work').get('boxv2').get('bcmc_url')
# wood
def source_user_wood_work_id():
    return source_user.get('work').get('wood').get('work_id')
# nemo
def source_user_nemo_work_id():
    return source_user.get('work').get('nemo').get('work_id')

def source_user_nemo_work_url():
    return source_user.get('work').get('nemo').get('work_url')

def source_user_nemo_preview_url():
    return source_user.get('work').get('nemo').get('preview_url')

# 获取原用户登录token，避免测试用例中多次调用登录态都初始化函数，这里先定义变量
source_user_login_token_v2 = login_token_v2(TIGER_API_HOST, source_user_username(), source_user_password())
def source_user_login_token():
    return source_user_login_token_v2

# 目标用户信息
def target_user_id():
    return target_user.get('id')

def target_user_username():
    return target_user.get('username')

def target_user_password():
    return target_user.get('password')

# Kitten作品
def target_user_ide_published_work_id():
    return target_user.get('work').get('ide').get('published_work_id')

def target_user_ide_published_unfork_work_id():
    return target_user.get('work').get('ide').get('published_unfork_work_id')

def target_user_ide_unpublish_work_id():
    return target_user.get('work').get('ide').get('unpublish_work_id')

def target_user_ide_deleted_temporarily_work_id():
    return target_user.get('work').get('ide').get('deleted_temporarily_work_id')

def target_user_ide_deleted_permanently_work_id():
    return target_user.get('work').get('ide').get('deleted_permanently_work_id')

# box2.0
def target_user_boxv2_published_work_id():
    return target_user.get('work').get('boxv2').get('published_work_id')

# nemo作品
def target_user_nemo_work_id():
    return target_user.get('work').get('nemo').get('work_id')

# 获取内部账号配置数据
internal_source_user = read_config.internal_source_user(TEST_ENV)

def internal_source_user_email():
    return internal_source_user.get('email')

def internal_source_user_password():
    return internal_source_user.get('password')

# 获取内部账号系统token
def source_user_login_token_internal_account():
    login_token= login_token_internal_account(INTERNAL_ACCOUNT_API_HOST, internal_source_user_email(), internal_source_user_password())
    return login_token

# 读取account库mysql配置
mysql_config_account = read_config.read_config_mysql(TEST_ENV, 'account')
opmysql_account = OpMysql(host=mysql_config_account['host'], user=mysql_config_account['user'], password=mysql_config_account['password'], database=mysql_config_account['database'])
# 读取redis配置
redis_config = read_config.read_config_redis(TEST_ENV)
op_redis = OpRedis(host=redis_config['host'], port=redis_config['port'], password=redis_config['password'], db=1)

# 清除数据库basic_auth表的phone_number字段
def clear_phone_number(phone_number):
    global opmysql_account
    opmysql_account.clear_basic_auth(column_name='phone_number', column_value=phone_number)

# 清除数据库basic_auth表的username字段
def clear_username(username):
    global opmysql_account
    opmysql_account.clear_basic_auth(column_name='username', column_value=username)

# 获取账号3.0的redis中存储的验证码
def get_captcha_account_v3(catpcha_type, phone_number):
    global op_redis
    captcha = op_redis.get_captcha_account('v3', catpcha_type, phone_number)
    return captcha

# 获取账号2.0的redi中存储的验证码
def get_captcha_account_v2(catpcha_type, phone_number):
    captcha = op_redis.get_captcha_account('v2', catpcha_type, phone_number)
    return captcha

# 获取发送图形验证码的ticket
def get_captcha_ticket():
    return get_captcha_ticket_account_v3(TIGER_API_HOST)

# 判断是否是dev或者test环境
def is_dev_or_test():
    return is_dev_or_test_env(TEST_ENV)

# 判断是dev环境（因为账号2.0只有dev关闭了极验）
def is_dev():
    return is_dev_env(TEST_ENV)

# 因为test中None会被解析为字符串，所以这里增加此函数
def is_none(source):
    return True if source == None else False
