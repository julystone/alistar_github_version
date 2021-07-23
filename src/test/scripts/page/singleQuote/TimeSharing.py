import allure

from src.test.scripts.framework.BasePage import BasePage
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.page.navigate.QuotePage import QuotePage
from src.test.scripts.page.setting.LoginPage import LoginPage


class TimeSharing(BasePage):
    # 顶部栏
    contract_name = ('id', 'esunny.test:id/es_kline_toolbar_title')
    draw_line_btn = {'x': 660 / 1080, 'y': 144 / 2201}
    fast_trade_btn = {'x': 780 / 1080, 'y': 144 / 2201}
    add_fav_btn = {'x': 900 / 1080, 'y': 144 / 2201}
    more_fun_btn = {'x': 1020 / 1080, 'y': 144 / 2201}
    quit_quote_btn = {'x': 60 / 1080, 'y': 144 / 2201}

    # TODO swipe to other page
    # TODO makeAPage
    # TODO goToFastTrade
    # TODO goToDrawTrade
    # TODO addFavorite

    @staticmethod
    @allure.step("调用底部栏接口，进入行情页面")
    def makeAPage():
        QuotePage.goToOneQuote_common()
        return TimeSharing()

    def clickDrawLineBtn(self):
        Driver.click(self.draw_line_btn)
        LoginPage.login_common()
        return self

    def long_press_quote(self):
        print("long_press")
        size = Driver.getWindowSize()
        print(size)
        Driver.long_press(y=size["height"] * 0.5, x=size["width"] * 0.5)
        return self

    def swipe_up_quote(self):
        print('swipe up')
        Driver.swipe('U')
        return self

    def swipe_left_quote(self):
        print('swipe left')
        Driver.swipe('L')
        return self


if __name__ == '__main__':
    Driver.driverInit(1)
    page = TimeSharing.makeAPage()
    (page.clickDrawLineBtn()
     .swipe_up_quote())
    input("点击继续")
