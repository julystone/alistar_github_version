# -*- coding: utf-8 -*-
# @File   :   util.py
# @Author :   julystone
# @Date   :   2020/8/4 14:39
# @Email  :   july401@qq.com

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from common.BasePage import Page

from common import ConfigUtil


class LoginPage(Page):
    # 用户名输入框
    menu_button = (MobileBy.ID, 'esunny.test:id/rv_favorite_list')  # 完美
    # text1 = (MobileBy.XPATH, '//*[@resource-id="esunny.test:id/fag_nav"]//*[@text="行情"]')  # 找到了，但是好慢好慢   11
    # text2 = (MobileBy.XPATH, '//*[@resource-id="esunny.test:id/fag_nav"]//*[contains(@text,"行情")]')  # 找到了，但是好慢好慢   11
    # text3 = (MobileBy.XPATH, '//*[@text="行情"]')  # 找到了，但是好慢好慢    11
    text3 = ('part-text', '行情')  # 找到了，但是好慢好慢    11
    # text4 = (MobileBy.XPATH, '//*[contains(@text,"行情")]')  # 找到了，但是好慢好慢    12
    # text1 = (MobileBy.ID, "esunny.test:id/fag_nav")
    text2 = (MobileBy.LINK_TEXT, "esunny.test:id/fag_nav")
    # 密码输入框
    pass_input = (MobileBy.XPATH, '//div[@class="signInWrap"]//input[@placeholder="密码"]')
    # 登录按钮
    login_btn = (MobileBy.XPATH, '//div[@class="pass-login"]//button')

    def gotoPage(self):
        res = self._find_element(self.menu_button)
        print(res)


if __name__ == '__main__':
    test_phone_config = ConfigUtil.ConfigData(1)
    Desired_Caps = dict(test_phone_config["test_phone"])
    print(Desired_Caps)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', Desired_Caps)
    log = LoginPage(driver)
    try:
        log.gotoPage()
    except Exception as e:
        print(e)
    log.driver.quit()
