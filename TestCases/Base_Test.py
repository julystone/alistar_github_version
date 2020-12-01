# -*- coding: utf-8 -*-
# @File   :   Base_Test.py.py
# @Author :   julystone
# @Date   :   2020/11/30 9:38
# @Email  :   july401@qq.com
import unittest

from appium import webdriver

from common import R_r_config

test_config = R_r_config.ConfigData()

Desired_Caps = {}
Desired_Caps['platformName'] = test_config.get('test_phone', 'platformName')
Desired_Caps['platformVersion'] = test_config.get('test_phone', 'platformVersion')
Desired_Caps['appPackage'] = test_config.get('test_phone', 'appPackage')
Desired_Caps['appActivity'] = test_config.get('test_phone', 'appActivity')
Desired_Caps['noReset'] = test_config.get('test_phone', 'noReset')


class TestBase(unittest.TestCase):
    def setUp(self):
        self.desired_caps = Desired_Caps
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

