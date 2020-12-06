from src.test.scripts.framework.Driver import Driver


class BottomToolBar:
    # 4功能键 - 自选
    self_list = ('text', '自选')
    # 4功能键 - 行情
    quote_list = ('text', '行情')
    # 4功能键 - 交易
    trade_page = ('text', '交易')
    # 4功能键 - 资讯
    news_page = ('text', '资讯')

    # 5功能键 - 资讯
    news_page_5 = ('text', '资讯')
    # 5功能键 - 盘口
    dish_page_5 = ('text', '盘口')
    # 5功能键 - 分时
    time_sharing_5 = ('text', '盘口')
    # 5功能键 - K线
    Kline_page_5 = ('text', '盘口')
    # 5功能键 - 交易
    trade_page_5 = ('text', '盘口')

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
