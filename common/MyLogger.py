"""
封装的自定义的日志格式
"""

import logging
import time

from common.ConfigUtil import my_config
from common.R_r_os import LOG_DIR


class Mylog:
    def __new__(cls):
        log_path = LOG_DIR

        name = my_config.get('log', 'name')
        all_level = my_config.get('log', 'all_level')
        ls_level = my_config.get('log', 'ls_level')
        fs_level = my_config.get('log', 'fs_level')

        # format = my_config.get('log', 'format')
        format = '%(asctime)s | %(process)s | [%(filename)s-->line:%(lineno)d] | %(levelname)-5s: %(message)s'

        # log_name = my_config.get('log', 'logName')
        log_name = 'log_%Y_%m_%d_%H'

        my_log = logging.getLogger(name)
        my_log.setLevel(all_level)

        my_ls = logging.StreamHandler()
        my_ls.setLevel(ls_level)
        my_lf = logging.FileHandler(f"{log_path}{time.strftime(log_name, time.localtime())}.log",
                                    encoding='utf8')
        my_lf.setLevel(fs_level)

        my_format = logging.Formatter(format)

        my_ls.setFormatter(my_format)
        my_lf.setFormatter(my_format)

        my_log.addHandler(my_ls)
        my_log.addHandler(my_lf)

        return my_log


my_log = Mylog()
