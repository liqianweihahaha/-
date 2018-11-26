import yaml
import os

conf_dir = os.path.join(os.path.dirname(__file__), '..', 'config')

def read_user(file_name, file_dir=conf_dir):
    file_path = os.path.join(file_dir, file_name)
    with open(file_path, 'r') as f:
        data = yaml.load(f)
        return data

def source_user(env):
    source_user_data = read_user('user.yaml')[env]['source_user']
    return source_user_data

def target_user( env):
    target_user_data = read_user('user.yaml')[env]['target_user']
    return target_user_data

if __name__ == '__main__':
    user = read_user('user.yaml')
    env = 'dev'
    print(user[env]['source_user'])