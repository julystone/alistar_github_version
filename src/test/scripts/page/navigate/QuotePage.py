import allure
from appium.webdriver.common.mobileby import MobileBy as By

from src.test.scripts.framework import Asserter
from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.page.interface.BottomToolBar import BottomToolBar


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

    @staticmethod
    @allure.step("调用底部栏接口，进入行情页面")
    def makeAPage():
        BottomToolBar.goToQuoteList()
        Asserter.shouldElemExist(QuotePage.contract_name_list)
        return QuotePage()

    def clickThirdTitle(self):
        Driver.click(self.third_title_switch)
        return self

    def clickForthTitle(self):
        Driver.click(self.forth_title_switch)
        return self

    def chooseBlock(self, block_name='内盘主力'):
        Driver.click(self.block_change)
        # Driver.scroll_until_elemDisplayed(self.block_change)
        locator = ('part-text', block_name)
        Driver.click(locator)
        return self

    def goToOneQuote(self, quote_name='苹果101'):
        print(f"正在进入{quote_name}合约")
        locator = ('part-text', quote_name)
        Driver.scroll_until_elemDisplayed(locator)
        Driver.click(locator)
        return self

    def get_quote_list(self):
        print('get quote list')
        return Driver.find_elements(self.contract_name_list)

    @staticmethod
    def goToOneQuote_common(block_name='内盘主力', quoteName='棉花105'):
        quote = QuotePage.makeAPage()
        if block_name not in Driver.get_text(quote.title):
            quote.chooseBlock(block_name)
        quote.goToOneQuote(quoteName)
        return quote


if __name__ == '__main__':
    dd = Driver.driverInit(0)
    page = dd.goToPage(QuotePage)
    try:
        BottomToolBar.goToQuoteList(dd)
        print(len(page.get_quote_list()))
    except Exception as e:
        print(e)
        raise e
    input("点击继续")
    log.quit()
