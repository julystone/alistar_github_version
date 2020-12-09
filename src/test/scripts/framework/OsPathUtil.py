# @File   :   R_r_os.py.py
# @Author :   July401
# @Date   :   2019\\6\\5
# @Email  :   july401@qq.com

import os
from utils.getRootPathUtil import getRootPath


class OsRead:
    @staticmethod
    def readPath(filepattern, ifsymbol=True):
        """
        基于根目录返回响应pattern的目录
        :param filepattern: --->    文件夹名称
        :param ifsymbol:    --->    是否返回值末尾要带反斜杠，默认为带
        :return:            --->    目标路径
        """
        dest_path = os.path.join(BASE_DIR, filepattern) + '\\' if ifsymbol else os.path.join(BASE_DIR, filepattern)
        return dest_path


BASE_DIR = getRootPath()

CONF_DIR = OsRead.readPath('config')

DATA_DIR = OsRead.readPath('task\\data')

LOG_DIR = OsRead.readPath('result\\log')

REPORT_DIR = OsRead.readPath('result\\report', ifsymbol=False)

SCREENSHOT_DIR = OsRead.readPath('result\\screenshot')

CASE_DIR = OsRead.readPath('src\\test\\scripts\\testcase')

if __name__ == '__main__':
    print(BASE_DIR)
    print(REPORT_DIR)
    print(SCREENSHOT_DIR)
