import time
from datetime import datetime

from appium.webdriver.common.mobileby import MobileBy as By

from src.test.scripts.framework import Asserter
from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.page.common.LoginPage import LoginPage
from src.test.scripts.page.interface.Keyboard import Keyboard
from src.test.scripts.page.interface.RightToolBar import RightToolBar
import allure

from src.test.scripts.page.singleQuote.TimeSharing import TimeSharing

"""
封装快买快卖
"""


class FastTrade(Page):
    quit_btn = {'x': 60 / 1080, 'y': 144 / 2201}

    # 底部栏
    lots_select = {'x': 90 / 1080, 'y': 2171 / 2201}
    price_select = {'x': 270 / 1080, 'y': 2171 / 2201}
    buy_button = {'x': 480 / 1080, 'y': 2171 / 2201}
    sell_button = {'x': 720 / 1080, 'y': 2171 / 2201}
    cover_button = {'x': 960 / 1080, 'y': 2171 / 2201}

    @staticmethod
    @allure.step("进入快买快卖界面")
    def makeAPage(driver):
        ts = TimeSharing.makeAPage(driver)
        Driver.click(driver, ts.fast_trade_btn)
        if Driver.check_element_exist(driver, ('text', '交易登录')):
            LoginPage.login_common(driver)
        Asserter.shouldElemExist(driver, FastTrade.buy_button)
        return FastTrade(driver)

    @allure.step("设置手数")
    def setLots(self, lots=1):
        print(f"设置手数 {lots}")
        my_log.info(f"设置手数 {lots}")
        Driver.click(self.driver, self.lots_select)
        Keyboard.lots_input(self.driver, lots)
        return self

    @allure.step("设置价格")
    def setPrice(self, price='对手价'):
        print(f"设置价格 {price}")
        my_log.info(f"设置价格 {price}")
        Driver.click(self.driver, self.price_select)
        Keyboard.price_input(self.driver, price)
        return self

    @allure.step("点击 买")
    def clickBuy(self):
        print("点击 买")
        my_log.info("点击 买")
        Driver.click(self.driver, self.buy_button)
        return self

    @allure.step("点击 卖")
    def clickSell(self):
        print("点击 卖")
        my_log.info("点击 卖")
        Driver.click(self.driver, self.sell_button)
        return self

    Err:
    @allure.step("检查账号密码是否已经保存")
    def checkAccountSaved(self):
        print("检查账号密码是否已经保存")
        if Driver.get_text(self.driver, self.login_pwd) is None:
            print("账密未保存")
            return False
        print("账密已记住")
        return True


if __name__ == '__main__':
    dd = Driver.driverFactory(0)

    input("点击继续")
    dd.quit()