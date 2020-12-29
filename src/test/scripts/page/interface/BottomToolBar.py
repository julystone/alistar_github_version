from src.test.scripts.framework.Driver import Driver


class BottomToolBar:
    # 4功能键 - 自选
    self_list = ('id', 'esunny.test:id/nav_item_favorite')
    # 4功能键 - 行情
    quote_list = ('id', 'esunny.test:id/nav_item_quote')
    # 4功能键 - 资讯
    news_page = ('id', 'esunny.test:id/nav_item_news')
    # 4功能键 - 交易
    trade_page = ('id', 'esunny.test:id/nav_item_trade')

    # 5功能键 - 资讯
    news_page_2 = ('id', 'esunny.test:id/es_kline_bottom_knb_news')
    # 5功能键 - 交易
    trade_page_2 = ('id', 'esunny.test:id/es_kline_bottom_knb_trade')
    # 5功能键 - 盘口
    dish_page = ('id', 'esunny.test:id/es_kline_bottom_knb_pannel')
    # 5功能键 - 分时
    time_sharing = ('id', 'esunny.test:id/es_kline_bottom_knb_min')
    # 5功能键 - K线
    Kline_page = ('id', 'esunny.test:id/es_kline_bottom_knb_klines')

    @staticmethod
    def goToSelfList():
        Driver.click(BottomToolBar.self_list)

    @staticmethod
    def goToQuoteList():
        Driver.click(BottomToolBar.quote_list)

    @staticmethod
    def goToDishPage():
        Driver.click(BottomToolBar.dish_page)

    @staticmethod
    def goToTimeSharing():
        Driver.click(BottomToolBar.time_sharing)

    @staticmethod
    def goToKlinePage():
        Driver.click(BottomToolBar.Kline_page)

    @staticmethod
    def goToNewsPage():
        if Driver.check_element_exist(BottomToolBar.news_page):
            Driver.click(BottomToolBar.news_page)
        else:
            Driver.click(BottomToolBar.news_page_2)

    @staticmethod
    def goToTradePage():
        if Driver.check_element_exist(BottomToolBar.trade_page):
            Driver.click(BottomToolBar.trade_page)
        else:
            Driver.click(BottomToolBar.trade_page_2)
