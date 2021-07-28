from src.test.scripts.page.BasePage.BasePageWithBottom import BasePageWithBottom


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
    draw_line_buy = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_buy_button")
    draw_line_sell = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_sell_button")
    draw_line_cover_long = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_long_button")
    draw_line_cover_short = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_short_button")
    draw_line_lots = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_lots_tv")
    draw_line_confirm = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_confirm_button")

    thud_trade_lots = ("resourceId", "esunny.estarandroid:id/es_kline_qty_text")
    thud_trade_price = ("resourceId", "esunny.estarandroid:id/es_kline_price_text")
    thud_trade_buy = ("resourceId", "esunny.estarandroid:id/es_kline_buy_button")
    thud_trade_sell = ("resourceId", "esunny.estarandroid:id/es_kline_sell_button")
    thud_trade_cover = ("resourceId", "esunny.estarandroid:id/es_kline_cover_button")

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

    def drawLineMode(self, into: bool):
        if into:
            if self.findElemWithoutException(self.draw_line_bar) is None:
                self.click(self.draw_line)
            else:
                print("Now has been in DrawLineMode")
        else:
            if self.findElemWithoutException(self.draw_line_bar) is not None:
                self.click(self.draw_line)
        return self

    def thudTradeMode(self, into: bool):
        if into:
            if self.findElemWithoutException(self.thud_trade_lots) is None:
                self.click(self.thud_trade)
            else:
                print("Now has been in ThudTradeMode")
        else:
            if self.findElemWithoutException(self.thud_trade_lots) is not None:
                self.click(self.thud_trade)
        return self

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
    debugPage.goToNewsPage().goToF10Page().quitPage()
