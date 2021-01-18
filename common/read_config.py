# encoding: utf-8

import yaml
import os

conf_dir = os.path.join(os.path.dirname(__file__), '..', 'config')

# 读取C端用户配置
def read_user(env, file_dir=conf_dir):
    file_name = str(env) + '_user.yml'
    file_path = os.path.join(file_dir, 'user', file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        return data

def source_user(env):
    source_user_data = read_user(env)['source_user']
    return source_user_data

def target_user(env):
    target_user_data = read_user(env)['target_user']
    return target_user_data

# 读取内部账号配置
def read_internal_user(env, file_dir=conf_dir):
    file_name = str(env)+'_user.yml'
    file_path = os.path.join(file_dir, 'internal_user', file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        return data

def internal_source_user(env):
    source_user_data = read_internal_user(env)['source_user']
    return source_user_data

# 读取数据库配置
def read_db(env, file_dir=conf_dir):
    file_name = str(env) + '_db.yml'
    file_path = os.path.join(file_dir, 'db', file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        return data

def read_config_mysql(env, database_name):
    mysql_data = read_db(env)['mysql'][database_name]
    return mysql_data

def read_config_redis(env):
    redis_data = read_db(env)['redis']
    return redis_data

# 读取商品配置
def read_config_product(env, file_dir=conf_dir):
    file_name = str(env) + '_product.yml'
    file_path = os.path.join(file_dir, 'product', file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        return data

# 获取虚拟商品信息
def sku(env):
    sku_info = read_config_product(env)['sku']
    return sku_info

# 获取虚拟&实物商品信息
def sku_physical(env):
    sku_physical_info = read_config_product(env)['sku_physical']
    return sku_physical_info

# 获取订金商品配置信息
def sku_deposit(env):
    sku_info = read_config_product(env)['sku_deposit']
    return sku_info

#获取商品属性配置信息
def attribute(env):
    attribute_info = read_config_product(env)['attribute']
    return attribute_info

# 读取订单配置
def read_config_order(env, file_dir=conf_dir):
    file_name = str(env) + '_order.yml'
    file_path = os.path.join(file_dir, 'order', file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        return data

def order(env):
    orderList = read_config_order(env)['orderList']
    return orderList

# 读取fish账号配置
def read_config_fish_account(env, file_dir=conf_dir):
    file_name = str(env) + '_user.yml'
    file_path = os.path.join(file_dir, 'fish_account', file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        return data


if __name__ == '__main__':
    env = 'dev'
    user = read_user(env)
    print(user['source_user'])