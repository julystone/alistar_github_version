"""
封装的读取配置文件的类，一般读取config.ini。如需多套环境切换，可自行实例化更改
"""
import configparser

from src.test.scripts.framework.OsPathUtil import CONF_DIR

config_path = CONF_DIR


class ConfigData(configparser.ConfigParser):
    def __init__(self, choice=0):
        super().__init__()
        self.optionxform = str
        if choice == 0:
            path = config_path + 'config.ini'
        else:
            path = config_path + f'config{choice}.ini'
            # self.read(config_path + f'/config{choice}.ini')
        # print(path)
        self.read(path, encoding='utf-8')


my_config = ConfigData()

if __name__ == '__main__':
    my_config = ConfigData(1)
    print(dict(my_config['test_phone']))
    # print(my_config["test_phone"])
