import time

from appium.webdriver.common.mobileby import MobileBy as By

from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.Interface.BottomToolBar import BottomToolBar


class SelfPage(Page):
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
    # 列表内合约
    quote_in_list = ('resource-id', 'esunny.test:id/item_list_quote_ll_main')

    def verify(self):
        # Driver.check_element_exist(self.driver, self.forth_title_switch)
        pass
        return self

    def goToSelfPage(self):
        BottomToolBar.goToSelfList(self.driver)
        return self

    def switchThirdTitle(self):
        Driver.click(self.driver, self.third_title_switch)
        return self

    def switchForthTitle(self):
        Driver.click(self.driver, self.forth_title_switch)
        return self

    def chooseBlock(self, block_name='内盘主力'):
        Driver.click(self.driver, self.block_change)
        locator = ('part-text', block_name)
        Driver.click(self.driver, locator)
        return self

    def goToOneQuote(self, quote_name='苹果101'):
        print(f"正在进入{quote_name}合约")
        locator = ('part-text', quote_name)
        Driver.click(self.driver, locator)
        return self

    def long_press_quote(self):
        print("long_press")
        size = Driver.getWindowSize(self.driver)
        print(size)
        Driver.long_press(self.driver, x=size["x"] * 0.5, y=size["y"] * 0.5)
        return self


if __name__ == '__main__':
    dd = Driver(0).driver
    log = SelfPage(dd)
    try:
        # log.goToSelfPage(). \
        log.verify(). \
            goToOneQuote("棉花105").\
            long_press_quote()
        print("1111")
        time.sleep(5)
    except Exception as e:
        print(e)
    log.quit()
