# @File   :   R_r_os.py.py
# @Author :   July401
# @Date   :   2019/6/5
# @Email  :   july401@qq.com

import os


class OsRead:
    def readpath(self, filepattern, ifsymbol='True'):
        """
        基于根目录返回响应pattern的目录
        :param filepattern: --->    文件夹名称
        :param ifsymbol:    --->    是否返回值末尾要带反斜杠，默认为带
        :return:            --->    目标路径
        """
        dest_path = os.path.join(BASE_DIR, filepattern) + '/' if ifsymbol else os.path.join(BASE_DIR, filepattern)
        return dest_path


my_os = OsRead()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

CONF_DIR = my_os.readpath('config')

DATA_DIR = my_os.readpath('TestCases/data')

LOG_DIR = my_os.readpath('result/log')

REPORT_DIR = my_os.readpath('result/report')

SCREENSHOT_DIR = my_os.readpath('result/screenshot')

CASE_DIR = my_os.readpath('TestCases')

if __name__ == '__main__':
    print(LOG_DIR)
