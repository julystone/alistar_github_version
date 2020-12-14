import time

from appium.webdriver.common.mobileby import MobileBy as By

from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.Interface.BottomToolBar import BottomToolBar
from src.test.scripts.page.QuotePage import QuotePage
from src.test.scripts.page.LoginPage import LoginPage


class QuoteTimeSharingPage(Page):
    # 左上角返回键
    back_button = (By.ID, 'esunny.test:id/toolbar_left_first')
    # 左上角合约名称
    quote_name = (By.ID, 'esunny.test:id/es_kline_toolbar_title')
    # 右4划线下单
    draw_line = (By.ID, 'esunny.test:id/es_kline_toolbar_right_fourth')
    # 右3快买快卖
    fast_trade = (By.ID, 'esunny.test:id/es_kline_toolbar_right_third')
    # 右2添加自选/删除自选
    add_fav = (By.ID, 'esunny.test:id/es_kline_toolbar_right_second')
    # 右1更多功能
    more_btn = (By.ID, 'esunny.test:id/es_kline_toolbar_right_first')

    # 勾选不再提示
    no_more_ntf = ('text', '不再提示')
    # 不再提示确定
    no_ntf_confirm = ('text', '确定')
    # 不再提示取消
    no_ntf_cancel = ('text', '取消')

    def __init__(self, driver, block_name, quote_name):
        Page.__init__(self, driver)
        QuotePage(driver).goToOneQuote_common(driver, block_name, quote_name)

    def verify(self):
        Driver.check_element_exist(self.driver, self.add_fav)
        pass
        return self

    def long_press_quote(self):
        print("long_press")
        size = Driver.getWindowSize(self.driver)
        print(size)
        Driver.long_press(self.driver, y=size["height"] * 0.5, x=size["width"] * 0.5)
        return self

    def swipe_up_quote(self):
        print('swipe up')
        Driver.swipe(self.driver, 'U')
        return self

    def swipe_left_quote(self):
        print('swipe left')
        Driver.swipe(self.driver, 'L')
        return self

    def draw_line_mode(self):
        print('点击划线下单')
        Driver.click(self.driver, self.draw_line)
        if not Driver.check_element_exist(self.driver, self.draw_line):
            LoginPage.login_common(self.driver)
        Driver.click(self.driver, self.draw_line)

    def fast_trade_mode(self):
        print('点击快买快卖')
        Driver.click(self.driver, self.fast_trade)
        if not Driver.check_element_exist(self.driver, self.draw_line):
            LoginPage.login_common(self.driver)
        Driver.click(self.driver, self.fast_trade)


if __name__ == '__main__':
    dd = Driver(0).driver
    log = QuoteTimeSharingPage(dd, '内盘主力', '棉花105')
    try:
        log.verify(). \
            swipe_up_quote(). \
            long_press_quote()
    except Exception as e:
        print(e)
        raise e
    input("点击继续")
    log.quit()
