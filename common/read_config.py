import yaml
import os

conf_dir = os.path.join(os.path.dirname(__file__), '..', 'config', 'user')

def read_user(file_name, file_dir=conf_dir):
    file_path = os.path.join(file_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        return data

def source_user(env):
    file_name = str(env)+'_user.yaml'
    source_user_data = read_user(file_name)['source_user']
    return source_user_data

def target_user( env):
    file_name = str(env)+'_user.yaml'
    target_user_data = read_user(file_name)['target_user']
    return target_user_data

if __name__ == '__main__':
    user = read_user('user.yaml')
    env = 'dev'
    print(user[env]['source_user'])