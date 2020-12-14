from datetime import datetime

from src.test.scripts.framework.Driver import Driver
from src.test.scripts.page.QuotePage import QuotePage
from src.test.scripts.page.LoginPage import LoginPage


class FastTradeButton:
    # 快买快卖功能键
    fast_trade_btn = ('id', 'esunny.test:id/es_kline_toolbar_right_third')

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

    # 买
    buy_button = ('text', '买')
    # 卖
    sell_button = ('text', '卖')
    # 平
    cover_button = ('text', '平')
    # 锁仓
    lock_button = ('text', '锁仓')

    @staticmethod
    def goToFastTrade(driver):
        t1 = datetime.now()
        Driver.click(driver, FastTradeButton.fast_trade_btn)
        t2 = datetime.now()
        print(f'第一次点击{t2} - {t1}')
        if Driver.check_element_exist(driver, LoginPage.login_company):
            LoginPage.login_common(driver)
            t5 = datetime.now()
            print(f'登录耗时{t5} - {t2}')
            Driver.click(driver, FastTradeButton.fast_trade_btn)
            t6 = datetime.now()
            print(f'第二次点击{t6} - {t5}')

    @staticmethod
    def noNtfMore(driver):
        if Driver.check_element_exist(driver, FastTradeButton.quit_ft_ntf):
            Driver.click(driver, FastTradeButton.no_more_ntf)
            Driver.click(driver, FastTradeButton.no_ntf_confirm)

    @staticmethod
    def noTradeNtfMore(driver):
        if Driver.check_element_exist(driver, FastTradeButton.trade_confirm_ntf):
            Driver.click(driver, FastTradeButton.no_more_ntf)
            Driver.click(driver, FastTradeButton.no_ntf_confirm)

    @staticmethod
    def clickBuyButton(driver):
        Driver.click(driver, FastTradeButton.buy_button)

    @staticmethod
    def clickSellButton(driver):
        Driver.click(driver, FastTradeButton.sell_button)


if __name__ == '__main__':
    dd = Driver(0).driver
    log = QuotePage(dd)
    log.goToOneQuote('CF105')
    FastTradeButton.goToFastTrade(dd)
    FastTradeButton.clickBuyButton(dd)
