import yaml
import secrets


def secure_token():
    return secrets.token_hex(32)


def get_token():
    return load_file_yaml()['TOKEN']


def get_size():
    return load_file_yaml()['SIZE']


def load_file_yaml():
    with open('config.yaml') as file:
        return yaml.load(file,Loader=yaml.FullLoader)