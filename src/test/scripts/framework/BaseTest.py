# -*- coding: utf-8 -*-
# @File   :   Base_Test.py.py
# @Author :   julystone
# @Date   :   2020/11/30 9:38
# @Email  :   july401@qq.com
from src.test.scripts.framework.Asserter import Asserter


class BaseTest:
    def recover_steps(self):
        pass

    def start_steps(self):
        pass

    def setup(self):
        try:
            self.start_steps()
        except AttributeError:
            self.recover_steps()
