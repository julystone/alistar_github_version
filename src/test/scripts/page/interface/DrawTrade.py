import allure
from src.test.scripts.page.interface.ConfirmNtf import ConfirmNtf
from src.test.scripts.page.singleQuote.TimeSharing import TimeSharing

from src.test.scripts.framework.Driver import Driver
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.page.BasePage.BasePage import BasePage
from src.test.scripts.page.interface.TradeNtf import TradeNtf
from src.test.scripts.page.setting.LoginPage import LoginPage

"""
封装画线下单
"""


class DrawTrade(BasePage):
    quit_btn = {'x': 60 / 1080, 'y': 144 / 2201}

    # 底部栏
    buy_button = {'x': 90 / 1080, 'y': 2171 / 2201}
    sell_button = {'x': 270 / 1080, 'y': 2171 / 2201}
    cover_sell = {'x': 450 / 1080, 'y': 2171 / 2201}
    cover_buy = {'x': 630 / 1080, 'y': 2171 / 2201}
    lots_select = {'x': 810 / 1080, 'y': 2171 / 2201}
    confirm_button = {'x': 990 / 1080, 'y': 2171 / 2201}

    @staticmethod
    @allure.step("进入画线下单界面")
    def makeAPage():
        ts = TimeSharing.makeAPage() \
            .clickDrawLineBtn()
        if Driver.check_element_exist(('text', '交易登录')):
            LoginPage.makeAPage() \
                .login_common()
            ts.clickDrawLineBtn()
        # Asserter.shouldElemExist(DrawTrade.buy_button)
        return DrawTrade()

    @allure.step("设置手数")
    def setLots(self, lots=1):
        print(f"设置手数 {lots}")
        my_log.info(f"设置手数 {lots}")
        Driver.click(self.lots_select)
        Keyboard.lots_input(lots)
        return self

    @allure.step("点击 买")
    def clickBuy(self):
        print("点击 买")
        my_log.info("点击 买")
        Driver.click(self.buy_button)
        return self

    @allure.step("点击 卖")
    def clickSell(self):
        print("点击 卖")
        my_log.info("点击 卖")
        Driver.click(self.sell_button)
        return self

    @allure.step("点击 确定")
    def clickConfirm(self):
        print("点击 确定")
        my_log.info("点击 确定")
        Driver.click(self.confirm_button)
        return self

    @allure.step("检查交易")
    def checkAccountSaved(self):
        print("检查账号密码是否已经保存")
        if Driver.get_text(self.login_pwd) is None:
            print("账密未保存")
            return False
        print("账密已记住")
        return True


if __name__ == '__main__':
    Driver.driverInit(1)

    DrawTrade.makeAPage(). \
        clickBuy(). \
        setLots(3). \
        clickConfirm()

    ConfirmNtf.commonNtf()

    TradeNtf.acceptNtf()

    input("点击继续")
    Driver.quit()
