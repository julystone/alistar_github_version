import time

from appium.webdriver.common.mobileby import MobileBy as By

from src.test.scripts.framework import Asserter
from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.page.common.LoginPage import LoginPage
from src.test.scripts.page.interface import RightToolBar
import allure

from src.test.scripts.page.interface.BottomToolBar import BottomToolBar
from src.test.scripts.page.interface.Keyboard import Keyboard


class TradePage(Page):
    # 顶部栏标题、点价、跳转K线
    title = (By.ID, 'esunny.test:id/toolbar_ll_title')
    dot_trade = (By.ID, 'esunny.test:id/toolbar_left_first')
    go_quote = (By.ID, 'esunny.test:id/toolbar_left_second')

    # 合约选择、手数、价格、买、卖
    contract_select = (By.ID, 'esunny.test:id/et_trade_contract')
    lots_select = (By.ID, 'esunny.test:id/et_trade_lots')
    price_select = (By.ID, 'esunny.test:id/et_trade_price')
    buy_button = (By.ID, 'esunny.test:id/tradeBtnPrimal_buy')
    sell_button = (By.ID, 'esunny.test:id/tradeBtnPrimal_sell')

    # 持仓、挂单、委托、成交页签
    tag_pos = (By.ID, 'esunny.test:id/textView_trade_position')
    tag_ask = (By.ID, 'esunny.test:id/textView_trade_parorder')
    tag_order = (By.ID, 'esunny.test:id/textView_trade_order')
    tag_match = (By.ID, 'esunny.test:id/textView_trade_match')

    # 委托列表
    order_list = (By.ID, 'esunny.test:id/recyclerview_trade_order')
    # 成交列表
    match_list = (By.ID, 'esunny.test:id/recyclerview_trade_match')

    @staticmethod
    @allure.step("进入交易界面")
    def makeAPage(driver):
        BottomToolBar.goToTradePage(driver)
        if Driver.check_element_exist(driver, ('text', '交易登录')):
            LoginPage.login_common(driver)
        Asserter.shouldElemExist(driver, TradePage.buy_button)
        return TradePage(driver)

    @allure.step("选择合约")
    def setContract(self, contract):
        print(f"选择{contract}合约")
        my_log.info(f"选择{contract}合约")
        Driver.click(self.driver, self.contract_select)
        locator = ('part-text', contract)
        Driver.click(self.driver, locator)
        return self

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

    @allure.step("检查委托列表")
    def checkMatchList(self):
        # 查看成交列表第一条是否有
        first_match = Driver.find_elements(self.driver, self.match_list)[0]
        first_order = Driver.find_elements(self.driver, self.order_list)[0]
        Asserter.shouldElemExist(first_order, first_match)


if __name__ == '__main__':
    dd = Driver.driverFactory(0)
    page = TradePage.makeAPage(dd)
    page.setContract("棉花105").\
        setLots(1).\
        setPrice('对手价').\
        clickBuy().\
        clickSell().\
        checkMatchList()
    input("点击继续")
    dd.quit()
