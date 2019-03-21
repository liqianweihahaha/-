import yaml
import os

conf_dir = os.path.join(os.path.dirname(__file__), '..', 'config')

# 读取用户配置
def read_user(file_name, file_dir=conf_dir):
    file_path = os.path.join(file_dir, 'user', file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        return data

def source_user(env):
    file_name = str(env)+'_user.yaml'
    source_user_data = read_user(file_name)['source_user']
    return source_user_data

def target_user(env):
    file_name = str(env)+'_user.yaml'
    target_user_data = read_user(file_name)['target_user']
    return target_user_data

# 读取数据库配置
def read_db(file_name, file_dir=conf_dir):
    file_path = os.path.join(file_dir, 'db', file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        return data

def read_config_mysql(env):
    file_name = str(env)+'_db.yaml'
    mysql_data = read_db(file_name)['mysql']
    return mysql_data


if __name__ == '__main__':
    user = read_user('user.yaml')
    env = 'dev'
    print(user[env]['source_user'])