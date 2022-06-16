"""
author :admin
Date : 2021/07/08
Description :
"""
import os

import yaml

from config import BASE_DIR


class DataUtils:

    @staticmethod
    def get_yaml_data(file_name):
        file_path = BASE_DIR + os.sep + 'data' + os.sep + file_name
        # print(file_path)
        with open(file_path, 'r', encoding='UTF-8') as f:
            return yaml.safe_load(f)

    @staticmethod
    def set_data(data, filename):
        file_path = BASE_DIR + os.sep + 'data' + os.sep + filename
        with open(file_path, 'w', encoding='UTF-8') as f:
            yaml.dump(data, f, allow_unicode=True, encoding='UTF-8')

    @staticmethod
    def get_login_data(type):
        data = DataUtils.get_yaml_data('t01_login_data.yaml')
        if type == "account":
            data1 = data.get('test_account_login').values()
            data2 = [tuple(x.values()) for x in data1]
            return data2


if __name__ == '__main__':
    print(DataUtils.get_login_data('account'))
