import allure
from appium.webdriver.common.mobileby import MobileBy as By

from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.page.navigate.QuotePage import QuotePage
from src.test.scripts.page.common.LoginPage import LoginPage


class TimeSharing(Page):
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
    def makeAPage(driver):
        QuotePage.goToOneQuote_common(driver)
        return TimeSharing(driver)


if __name__ == '__main__':
    pass
