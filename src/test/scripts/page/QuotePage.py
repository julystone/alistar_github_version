import time

from appium.webdriver.common.mobileby import MobileBy as By

from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.Interface.BottomToolBar import BottomToolBar


class QuotePage(Page):
    # title
    title = (By.ID, 'esunny.test:id/toolbar_title')
    # 左侧进入板块选择
    block_change = (By.ID, 'esunny.test:id/toolbar_left_first')
    # 合约名称-合约代码
    first_text = (By.ID, 'esunny.test:id/es_quote_fragment_header_tv_contract_name_double')
    # 最新-昨结
    second_text = (By.ID, 'esunny.test:id/es_quote_fragment_header_tv_last_double')
    # 切换涨跌涨幅
    third_title_switch = (By.ID, 'esunny.test:id/es_quote_fragment_header_tv_change_double')
    # 账号输入
    forth_title_switch = (By.ID, 'esunny.test:id/es_quote_fragment_header_tv_position_double')
    # 自选合约列表名
    contract_name_list = (By.ID, 'esunny.test:id/tv_quote_contractName')
    # 自选合约列表号
    contract_no_list = (By.ID, 'esunny.test:id/tv_quote_contractNo')

    def verify(self):
        # TODO verify  这个元素定位不到
        Driver.check_element_exist(self.driver, self.forth_title_switch)
        pass
        return self

    def goToQuotePage(self):
        BottomToolBar.goToQuoteList(self.driver)
        return self

    def switchThirdTitle(self):
        Driver.click(self.driver, self.third_title_switch)
        return self

    def switchForthTitle(self):
        Driver.click(self.driver, self.forth_title_switch)
        return self

    def chooseBlock(self, block_name='内盘主力'):
        Driver.click(self.driver, self.block_change)
        # Driver.scroll_until_elemDisplayed(self.driver, self.block_change)
        locator = ('part-text', block_name)
        Driver.click(self.driver, locator)
        return self

    def goToOneQuote(self, quote_name='苹果101'):
        print(f"正在进入{quote_name}合约")
        locator = ('part-text', quote_name)
        Driver.scroll_until_elemDisplayed(self.driver, locator)
        Driver.click(self.driver, locator)
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

    def get_quote_list(self):
        print('get quote list')
        return Driver.find_elements(self.driver, self.contract_name_list)

    @staticmethod
    def goToOneQuote_common(driver, block_name, quoteName):
        quote = QuotePage(driver)
        quote.goToQuotePage(). \
            chooseBlock(block_name). \
            goToOneQuote(quoteName)


if __name__ == '__main__':
    dd = Driver(0).driver
    log = QuotePage(dd)
    try:
        # log.goToSelfPage(). \
        # log.verify(). \
        BottomToolBar.goToQuoteList(dd)
        print(len(log.get_quote_list()))
    except Exception as e:
        print(e)
        raise e
    input("点击继续")
    log.quit()
