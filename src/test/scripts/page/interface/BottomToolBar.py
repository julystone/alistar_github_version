from src.test.scripts.framework.Driver import Driver


class BottomToolBar:
    # 4功能键 - 自选
    self_list = {'x': 1 / 8, 'y': 1853 / 1920}
    # 4功能键 - 行情
    quote_list = {'x': 3 / 8, 'y': 1853 / 1920}
    # 4功能键 - 交易
    trade_page = {'x': 5 / 8, 'y': 1853 / 1920}
    # 4功能键 - 资讯
    news_page = {'x': 7 / 8, 'y': 1853 / 1920}

    # 5功能键 - 资讯
    news_page_2 = {'x': 1 / 10, 'y': 2171 / 2201}
    # 5功能键 - 交易
    trade_page_2 = {'x': 3 / 10, 'y': 2171 / 2201}
    # 5功能键 - 盘口
    dish_page = {'x': 5 / 10, 'y': 2171 / 2201}
    # 5功能键 - 分时
    time_sharing = {'x': 7 / 10, 'y': 2171 / 2201}
    # 5功能键 - K线
    Kline_page = {'x': 9 / 10, 'y': 2171 / 2201}

    @staticmethod
    def goToSelfList():
        Driver.click(BottomToolBar.self_list)

    @staticmethod
    def goToQuoteList():
        Driver.click(BottomToolBar.quote_list)

    @staticmethod
    def goToNewsPage():
        Driver.click(BottomToolBar.news_page)

    @staticmethod
    def goToTradePage():
        Driver.click(BottomToolBar.trade_page)

    # 以下为5列表

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
    def goToNewsPage2():
        Driver.click(BottomToolBar.news_page_2)

    @staticmethod
    def goToTradePage2():
        Driver.click(BottomToolBar.trade_page_2)
