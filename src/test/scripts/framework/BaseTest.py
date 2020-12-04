# -*- coding: utf-8 -*-
# @File   :   Base_Test.py.py
# @Author :   julystone
# @Date   :   2020/11/30 9:38
# @Email  :   july401@qq.com
import unittest

from src.test.scripts.framework.Driver import Driver


class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver = Driver.prepareForAndroidAppium(0)

    def tearDown(self):
        self.driver.quit()
