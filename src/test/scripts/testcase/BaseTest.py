# -*- coding: utf-8 -*-
# @File   :   Base_Test.py.py
# @Author :   julystone
# @Date   :   2020/11/30 9:38
# @Email  :   july401@qq.com
from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.page.BasePage import BasePage


class BaseTest:
    testPage: BasePage

    def init_steps(self):
        pass

    def recover_steps(self):
        pass

    def setup(self):
        try:
            self.init_steps()
        except (AttributeError, AssertionError):
            self.recover_steps()

    def teardown(self):
        pass

    @classmethod
    def init_steps_class(cls):
        pass

    @classmethod
    def setup_class(cls):
        cls.init_steps_class()

    def meta_switchTest(self, switch):
        # 数据备份
        before = self.testPage.getCurSwitchStatus(switch)

        # 切换
        self.testPage.changeOneSwitch(switch, not before)
        after = self.testPage.getCurSwitchStatus(switch)
        Asserter.BoolNotEqualBool(before, after)

        self.testPage.changeOneSwitch(switch, before)

    def meta_checkTest(self, check):
        # 数据备份
        before = self.testPage.getCurCheckStatus(check)

        # 切换
        self.testPage.changeOneCheck(check, not before)
        after = self.testPage.getCurCheckStatus(check)
        Asserter.BoolNotEqualBool(before, after)

        self.testPage.changeOneCheck(check, before)
