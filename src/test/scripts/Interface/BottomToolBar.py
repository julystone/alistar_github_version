from src.test.scripts.framework.Driver import Driver


class BottomToolBar:
    # 4功能键 - 自选
    self_list = ('id', 'esunny.test:id/nav_item_favorite')
    # 4功能键 - 行情
    quote_list = ('id', 'esunny.test:id/nav_item_quote')
    # 4功能键 - 交易
    trade_page = ('id', 'esunny.test:id/nav_item_trade')
    # 4功能键 - 资讯
    news_page = ('id', 'esunny.test:id/nav_item_news')

    # 5功能键 - 资讯
    news_page_5 = ('id', 'esunny.test:id/es_kline_bottom_knb_news')
    # 5功能键 - 盘口
    dish_page_5 = ('id', 'esunny.test:id/es_kline_bottom_knb_pannel')
    # 5功能键 - 分时
    time_sharing_5 = ('id', 'esunny.test:id/es_kline_bottom_knb_min')
    # 5功能键 - K线
    Kline_page_5 = ('id', 'esunny.test:id/es_kline_bottom_knb_klines')
    # 5功能键 - 交易
    trade_page_5 = ('id', 'esunny.test:id/es_kline_bottom_knb_trade')

    @staticmethod
    def goToSelfList(driver):
        Driver.click(driver, BottomToolBar.self_list)

    @staticmethod
    def goToQuoteList(driver):
        Driver.click(driver, BottomToolBar.quote_list)

    @staticmethod
    def goToTradePage(driver):
        Driver.click(driver, BottomToolBar.trade_page)

    @staticmethod
    def goToNewsPage(driver):
        Driver.click(driver, BottomToolBar.news_page)

    @staticmethod
    def goToNewsPage5(driver):
        Driver.click(driver, BottomToolBar.news_page_5)

    @staticmethod
    def goToDishPage5(driver):
        Driver.click(driver, BottomToolBar.dish_page_5)

    @staticmethod
    def goToTimeSharing5(driver):
        Driver.click(driver, BottomToolBar.time_sharing_5)

    @staticmethod
    def goToKlinePage5(driver):
        Driver.click(driver, BottomToolBar.Kline_page_5)

    @staticmethod
    def goToTradePage5(driver):
        Driver.click(driver, BottomToolBar.trade_page_5)
