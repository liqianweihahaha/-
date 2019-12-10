import os
from common import read_config
from common.util import *
from common.op_mysql import OpMysql
from common.op_redis import OpRedis

# 读取 .env 配置
TEST_ENV = os.environ['environment']
# 获取测试域名hosts
TIGER_API_HOST = os.environ['tiger_api_host']
PLATFORM_TIGER_API_HOST = os.environ['platform_tiger_api_host']
INTERNAL_ACCOUNT_API_HOST = os.environ['internal_account_api_host']
INTERNAL_ACCOUNT_SERVICE_HOST = os.environ['internal_account_service_host']
EZBUY_API_HOST = os.environ['ezbuy_api_host']
TRANSACTION_ADMIN_API_HOST = os.environ['transaction_admin_api_host']
ORDER_SERVICE_HOST = os.environ['order_service_host']
PRODUCT_SERVICE_HOST = os.environ['product_service_host']
AUHTORITY_API_HOST = os.environ['authority_api_host']

# 获取config配置文件：源用户信息
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
source_user_login_token_account_v2 = login_token_account_v2(TIGER_API_HOST, source_user_username(), source_user_password())
def source_user_login_token():
    return source_user_login_token_account_v2

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
    #login_token= login_token_internal_account(INTERNAL_ACCOUNT_API_HOST, internal_source_user_email(), internal_source_user_password())
    login_token = generate_internal_account_token(INTERNAL_ACCOUNT_SERVICE_HOST, internal_source_user_id())
    return login_token

# 判断是否是dev或者test环境
def is_dev_or_test():
    return True if TEST_ENV not in ('staging', 'production') else False

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

# 读取order配置信息
order_config = read_config.order(TEST_ENV)

def order_customerId_config():
    return order_config.get('customerId')

def order_placedBy_config():
    return order_config.get('placedBy')

def order_customerPhoneNumber_config():
    return order_config.get('customerPhoneNumber')

# #获取时间戳开始时间
# def get_start_time():
#     return int(time.time())-86400*2
#
# #获取当前时间戳结束时间
# def get_end_time():
#     return int(time.time())

