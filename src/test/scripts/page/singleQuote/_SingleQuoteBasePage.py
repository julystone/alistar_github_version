from src.test.scripts.page.BasePage.BasePageWithBottom import BasePageWithBottom
from src.test.scripts.page.interface.DrawLineMode import DrawLineMode
from src.test.scripts.page.interface.ThudTradeMode import ThudTradeMode


class SingleQuoteBasePage(BasePageWithBottom):
    # 合约名、主力标记及退出按钮
    quit_btn = ("resourceId", "esunny.estarandroid:id/es_kline_toolbar_left")
    quote_name = ("resourceId", "esunny.estarandroid:id/es_kline_toolbar_title")
    main_notice = ("resourceId", "esunny.estarandroid:id/es_kline_toolbar_tv_quote_main_notice")

    # 左上角工具栏
    draw_line = ("resourceId", "esunny.estarandroid:id/es_kline_toolbar_right_fourth")
    thud_trade = ("resourceId", "esunny.estarandroid:id/es_kline_toolbar_right_third")
    add_fav = ("resourceId", "esunny.estarandroid:id/es_kline_toolbar_right_second")
    more_btn = ("resourceId", "esunny.estarandroid:id/es_kline_toolbar_right_first")

    # 衍生物
    draw_line_bar = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_menu_bar")

    thud_trade_lots = ("resourceId", "esunny.estarandroid:id/es_kline_qty_text")

    # 底部切换栏
    news = ('text', '资讯')
    panel = ('text', '盘口')
    min = ('text', '分时')
    kline = ('text', 'K线')
    trade = ('text', '交易')
    annal_list = [news, panel, min, kline, trade]

    # 校验项
    block_choose = '测试'

    def quitPage(self):
        self.click(self.quit_btn)
        return self

    def getCurQuote(self):
        return self.get_text(self.quote_name)

    def swipe_change_quote(self, direction):
        return self.swipe(direction)

    def swipe_change_annal(self, direction):
        return self.swipe(direction)

    def metaGoToMode(self, pageInit, page_enter):
        try:
            return pageInit()
        except AssertionError:
            self.click(page_enter)
            if self.findElemViaText("交易登录") is not None:
                from src.test.scripts.page.rightToolBar.LoginPage import LoginPage
                LoginPage().login_common()
                self.click(page_enter)
            return pageInit()

    def goToDrawLineMode(self):
        return self.metaGoToMode(lambda: DrawLineMode(), self.draw_line)

    def goToThudTradeMode(self):
        return self.metaGoToMode(lambda: ThudTradeMode(), self.thud_trade)

    def openMoreMode(self, into: bool):
        if into:
            if self.findElemWithoutException(('text', '搜索合约')) is None:
                self.click(self.more_btn)
            else:
                print("Now has been in MoreBtnMode")
        else:
            if self.findElemWithoutException(('text', '搜索合约')) is not None:
                self.click(self.more_btn)
        return self

    def addFav(self):
        self.click(self.add_fav)
        return self

    def goToMinPage(self):
        if self.getCurItemStatus(self.min) is False:
            self.click(self.min)
        from src.test.scripts.page.singleQuote.MinPage import MinPage
        return MinPage()

    def goToKlinePage(self):
        if self.getCurItemStatus(self.kline) is False:
            self.click(self.kline)
        from src.test.scripts.page.singleQuote.KlinePage import KlinePage
        return KlinePage()

    def goToTradePage(self):
        if self.getCurItemStatus(self.trade) is False:
            self.click(self.trade)
        from src.test.scripts.page.singleQuote.TradePage import TradePage
        return TradePage()

    def goToNewsPage(self):
        if self.getCurItemStatus(self.news) is False:
            self.click(self.news)
        from src.test.scripts.page.singleQuote.NewsPage import NewsPage
        return NewsPage()

    def goToPanelPage(self):
        if self.getCurItemStatus(self.panel) is False:
            self.click(self.panel)
        from src.test.scripts.page.singleQuote.PanelPage import PanelPage
        return PanelPage()


if __name__ == '__main__':
    debugPage = SingleQuoteBasePage()
    debugPage.goToThudTradeMode().goToF10Page().quitPage()
