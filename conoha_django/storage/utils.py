import json
from django.conf import settings


def load_settings(k, default=None):
    return getattr(settings, k, default)


def json_load(filepath, **kwargs):
    with open(filepath, **kwargs) as f:
        return json.load(f)


def load_credentials():
    access_file_path = load_settings('CONOHA_ACCESS_FILE_PATH', 'conoha.json')
    access_json = json_load(access_file_path)
    return access_json


def get_container_and_filename(name):
    splited_name = name.split('/')
    if len(splited_name) == 1:
        return name, ''
    return splited_name[0], '/'.join(splited_name[1:])


def is_container(name):
    container, filename = get_container_and_filename(name)
    return filename == ''
