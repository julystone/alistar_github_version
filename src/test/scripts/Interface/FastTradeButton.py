from datetime import datetime

from src.test.scripts.framework.Driver import Driver
from src.test.scripts.page.QuotePage import QuotePage
from src.test.scripts.page.LoginPage import LoginPage


class FastTradeButton:
    # 快买快卖功能键
    draw_line_btn = {'x': 660 / 1080, 'y': 144 / 2201}
    fast_trade_btn = {'x': 780 / 1080, 'y': 144 / 2201}
    add_fav_btn = {'x': 900 / 1080, 'y': 144 / 2201}
    more_fun_btn = {'x': 1020 / 1080, 'y': 144 / 2201}

    # 退出快买快卖提示框
    quit_ft_ntf = ('text', '是否要退出快买快卖？')
    # 不再提示勾选框
    no_more_ntf = ('text', '不再提示')
    # 不再提示确定
    no_ntf_confirm = ('text', '确定')
    # 不再提示取消
    no_ntf_cancel = ('text', '取消')

    # 下单提示框
    trade_confirm_ntf = ('text', '下单/改单操作确认')

    # 手数选择
    num_choose = {'x': 90 / 1080, 'y': 2171 / 2201}
    # 价格选择
    price_choose = {'x': 270 / 1080, 'y': 2171 / 2201}
    # 买
    buy_button = {'x': 480 / 1080, 'y': 2171 / 2201}
    # 卖
    sell_button = {'x': 720 / 1080, 'y': 2171 / 2201}
    # 平/锁仓
    cover_button = {'x': 960 / 1080, 'y': 2171 / 2201}

    number_keys = {
        '1': {'x': 135 / 1080, 'y': 1740 / 2201}, '2': {'x': 405 / 1080, 'y': 1740 / 2201},
        '3': {'x': 675 / 1080, 'y': 1740 / 2201},
        '4': {'x': 135 / 1080, 'y': 1895 / 2201}, '5': {'x': 405 / 1080, 'y': 1895 / 2201},
        '6': {'x': 675 / 1080, 'y': 1895 / 2201},
        '7': {'x': 135 / 1080, 'y': 2050 / 2201}, '8': {'x': 405 / 1080, 'y': 2050 / 2201},
        '9': {'x': 675 / 1080, 'y': 2050 / 2201},
        '00': {'x': 135 / 1080, 'y': 2165 / 2201}, '0': {'x': 405 / 1080, 'y': 2165 / 2201},
        '<-': {'x': 675 / 1080, 'y': 2165 / 2201},
        'plus': {'x': 945 / 1080, 'y': 1820 / 2201}, 'minus': {'x': 945 / 1080, 'y': 2128 / 2201},
    }

    price_keys = {
        '1': {'x': 323 / 1080, 'y': 1740 / 2201}, '2': {'x': 539 / 1080, 'y': 1740 / 2201},
        '3': {'x': 755 / 1080, 'y': 1740 / 2201},
        '4': {'x': 323 / 1080, 'y': 1895 / 2201}, '5': {'x': 539 / 1080, 'y': 1895 / 2201},
        '6': {'x': 755 / 1080, 'y': 1895 / 2201},
        '7': {'x': 323 / 1080, 'y': 2050 / 2201}, '8': {'x': 539 / 1080, 'y': 2050 / 2201},
        '9': {'x': 755 / 1080, 'y': 2050 / 2201},
        '.': {'x': 323 / 1080, 'y': 2165 / 2201}, '0': {'x': 539 / 1080, 'y': 2165 / 2201},
        '<-': {'x': 755 / 1080, 'y': 2165 / 2201},
        'plus': {'x': 975 / 1080, 'y': 1820 / 2201}, 'minus': {'x': 975 / 1080, 'y': 2128 / 2201},
        'buy': {'x': 480 / 1080, 'y': 1460 / 2201}, 'sell': {'x': 720 / 1080, 'y': 1460 / 2201},
    }

    @staticmethod
    def goToFastTrade(driver):
        t1 = datetime.now()
        # Driver.click(driver, FastTradeButton.fast_trade_btn)
        Driver.click(driver, FastTradeButton.fast_trade_btn)
        t2 = datetime.now()
        print(f'第一次点击\n{t2 - t1}')
        if Driver.check_element_exist(driver, LoginPage.login_company):
            LoginPage.login_common(driver)
            t5 = datetime.now()
            print(f'登录耗时\n{t5 - t2}')
            Driver.click(driver, FastTradeButton.fast_trade_btn)
            t6 = datetime.now()
            print(f'第二次点击\n{t6 - t5}')

    @staticmethod
    def noMoreNtf(driver):
        if Driver.check_element_exist(driver, FastTradeButton.quit_ft_ntf):
            Driver.click(driver, FastTradeButton.no_more_ntf)
            Driver.click(driver, FastTradeButton.no_ntf_confirm)

    @staticmethod
    def noMoreTradeNtf(driver):
        if Driver.check_element_exist(driver, FastTradeButton.trade_confirm_ntf):
            Driver.click(driver, FastTradeButton.no_more_ntf)
            Driver.click(driver, FastTradeButton.no_ntf_confirm)

    @staticmethod
    def clickBuyButton(driver):
        Driver.click(driver, FastTradeButton.buy_button)

    @staticmethod
    def clickSellButton(driver):
        Driver.click(driver, FastTradeButton.sell_button)

    @staticmethod
    def clickCoverButton(driver):
        Driver.click(driver, FastTradeButton.cover_button)

    @staticmethod
    def clickPriceButton(driver):
        Driver.click(driver, FastTradeButton.price_choose)

    @staticmethod
    def trade_via_price(driver, method, price):
        if method not in ['buy', 'sell']:
            return None
        for num in str(price):
            print(num)
            Driver.click(driver, FastTradeButton.price_keys[num])
        Driver.click(driver, FastTradeButton.price_keys[method])


if __name__ == '__main__':
    dd = Driver(0).driver
    log = QuotePage(dd)
    log.goToOneQuote('CF105')
    FastTradeButton.goToFastTrade(dd)
    FastTradeButton.clickPriceButton(dd)
    FastTradeButton.trade_via_price(dd, 'buy', 14875)
    FastTradeButton.noMoreTradeNtf(dd)
