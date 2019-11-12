import os
from common import read_config
from common.util import *
from common.environment import *
from common.op_mysql import OpMysql
from common.op_redis import OpRedis

# 读取 .env 配置
TEST_ENV = os.environ['environment']

# 获取测试域名hosts
TIGER_API_HOST = get_hosts(TEST_ENV).get('tiger_api_host')
PLATFORM_TIGER_API_HOST = get_hosts(TEST_ENV).get('platform_tiger_api_host')
INTERNAL_ACCOUNT_API_HOST = get_hosts(TEST_ENV).get('internal_account_api_host')
INTERNAL_ACCOUNT_SERVICE_HOST = get_hosts(TEST_ENV).get('internal_account_service_host')
EZBUY_API_HOST = get_hosts(TEST_ENV).get('ezbuy_api_host')
TRANSACTION_ADMIN_API_HOST = get_hosts(TEST_ENV).get('transaction_admin_api_host')
ORDER_SERVICE_HOST = get_hosts(TEST_ENV).get('order_service_host')
PRODUCT_SERVICE_HOST = get_hosts(TEST_ENV).get('product_service_host')
AUHTORITY_API_HOST = get_hosts(TEST_ENV).get('authority_api_host')

def tiger_api_host():
    return TIGER_API_HOST

def platform_tiger_api_host():
    return PLATFORM_TIGER_API_HOST

def internal_account_api_host():
    return INTERNAL_ACCOUNT_API_HOST

def internal_account_service_host():
    return INTERNAL_ACCOUNT_SERVICE_HOST

def ezbuy_api_host():
    return EZBUY_API_HOST

def transaction_admin_api_host():
    return TRANSACTION_ADMIN_API_HOST

def order_service_host():
    return ORDER_SERVICE_HOST

def product_service_host():
    return PRODUCT_SERVICE_HOST

def authority_api_host():
    return AUHTORITY_API_HOST

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

# 获取内部账号配置数据
internal_source_user = read_config.internal_source_user(TEST_ENV)

def internal_source_user_email():
    return internal_source_user.get('email')

def internal_source_user_password():
    return internal_source_user.get('password')

def internal_source_user_id():
    return internal_source_user.get('id')

def internal_source_user_department_id():
    return internal_source_user.get('department_id')

def internal_source_user_fish_id():
    return internal_source_user.get('relation_fish_id')

# 获取内部账号系统token
def internal_source_user_login_token():
    login_token= login_token_internal_account(INTERNAL_ACCOUNT_API_HOST, internal_source_user_email(), internal_source_user_password())
    return login_token

# 判断是否是dev或者test环境
def is_dev_or_test():
    return is_dev_or_test_env(TEST_ENV)

# 判断是否是正式环境
def is_production():
    return True if TEST_ENV == 'production' else False

# 因为test中None会被解析为字符串，所以这里增加此函数
def is_none(source):
    return True if source == None else False

# 读取sku配置信息
sku_config = read_config.sku(TEST_ENV)

def sku_number_config():
    return sku_config.get('number')

def sku_price_config():
    return sku_config.get('price')

# 获取当前时间的秒级时间戳
def get_timeslot_now():
    return int(time.time())