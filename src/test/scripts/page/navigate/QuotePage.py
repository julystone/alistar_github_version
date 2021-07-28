from _NavigateBasePage import NavigateBasePage
from src.test.scripts.framework.Asserter import Asserter


class QuotePage(NavigateBasePage):
    # 行情授权弹框
    auth_dialog = ('resourceId', "esunny.test:id/es_base_custom_dialog_title")
    auth_cancel_btn = ('text', '取消')

    # 主力排名、行情列表、滑动定位栏
    quote_main = ("resourceId", "esunny.test:id/es_quote_sort_main")
    quote_list = ("resourceId", "esunny.test:id/tv_quote_contractName")
    scroll_bar = ("resourceId", "esunny.estarandroid:id/es_rv_quote_commodity_select")

    # 校验项
    exchange_switch_btn = ("resourceId", "esunny.test:id/toolbar_left_first")

    def selfCheck(self):
        self.watcher_handle("行情授权弹框", self.auth_dialog, self.auth_cancel_btn)
        Asserter.PageHasElem(self, self.quote_main)

    def getQuoteList(self):
        return self.findElement(self.quote_list)

    def goToSingleQuotePage(self, quoteName, exchangeName=None):
        if exchangeName is not None:
            self.changeExchange(exchangeName)
        loc = ('part-text', quoteName.upper())
        self.swipe_until_loc(loc)
        self.click(loc)
        from src.test.scripts.page.singleQuote.MinPage import MinPage
        return MinPage()

    def changeExchange(self, exchangeName):
        exchangeName = exchangeName.upper()
        loc = ('textContains', exchangeName)
        self.click(self.exchange_switch_btn) \
            .swipe_until_loc(loc) \
            .click(loc)
        Asserter.TextContainsText(self.getCurTitle(), exchangeName)
        return self

    def scrollToCommodity(self, commodity):
        locator = ('text', commodity)
        self.swipe_until_loc(locator, self.scroll_bar, 'horizon')
        self.click(locator)

    def goToOptionPage(self):
        self.changeExchange('OPTION')

    def goToMainSortPage(self):
        self.click(self.quote_main)
        return self.MainSortPage()

    class MainSortPage(NavigateBasePage):
        scroll_bar = ("resourceId", "esunny.estarandroid:id/es_rv_quote_commodity_select")
        # 校验项
        title_text = '主力排名'

        def switchToColumn(self, column):
            locator = ('text', column)
            self.swipe_until_loc(locator, self.scroll_bar, 'horizon')
            self.click(locator)


if __name__ == '__main__':
    debugPage = QuotePage()
    debugPage.goToSingleQuotePage('沪金2112', '上期所').goToNewsPage().goToF10Page()
