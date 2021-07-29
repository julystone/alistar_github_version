from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.BasePage.BasePage import BasePage
from src.test.scripts.page.rightToolBar.AboutPage import AboutPage
from src.test.scripts.page.rightToolBar.ChampionSortPage import ChampionSortPage
from src.test.scripts.page.rightToolBar.CloudServicePage import CloudServicePage
from src.test.scripts.page.rightToolBar.CondOrderPage import CondOrderPage
from src.test.scripts.page.rightToolBar.LoginPage import LoginPage
from src.test.scripts.page.rightToolBar.QuoteLoginPage import QuoteLoginPage
from src.test.scripts.page.rightToolBar.QuoteSetting import QuoteSetting
from src.test.scripts.page.rightToolBar.Setting import Setting
from src.test.scripts.page.rightToolBar.TradeCalendar import TradeCalendar
from src.test.scripts.page.rightToolBar.TradeSetting import TradeSetting


class RightToolBar(Driver, BasePage):
    # menu功能键
    right_panel = ('resourceId', "esunny.test:id/fragment_login")
    # 右侧边栏 - 交易类
    trade_login = ("resourceId", "esunny.test:id/es_fragment_login_tv_login")
    multi_login = ("resourceId", "esunny.test:id/es_fragment_login_trade_login")
    quote_setting = ("resourceId", "esunny.test:id/es_fragment_login_btv_char_setting")
    trade_setting = ("resourceId", "esunny.test:id/es_fragment_login_btv_trade_setting")
    condition_order = ("resourceId", "esunny.test:id/es_fragment_login_btv_condition_order")
    stop_trade = ("resourceId", "esunny.test:id/es_fragment_login_btv_stop_trade")
    stop_open = ("resourceId", "esunny.test:id/es_fragment_login_btv_stop_open")
    price_warn = ("resourceId", "esunny.test:id/es_fragment_login_btv_price_warn")
    trade_related = ("resourceId", "esunny.test:id/es_fragment_login_btv_about_trade")
    message = ("resourceId", "esunny.test:id/es_fragment_login_btv_message")

    # 右侧边栏 - 行情类
    quote_login = ("resourceId", "esunny.test:id/es_fragment_login_btv_quote_login")
    cloud_service = ("resourceId", "esunny.test:id/es_fragment_login_btv_cloud_service")
    open_account = ("resourceId", "esunny.test:id/es_fragment_login_btv_open_account")
    star_store = ("resourceId", "esunny.test:id/es_fragment_login_btv_store")
    trade_calendar = ("resourceId", "esunny.test:id/es_fragment_login_btv_trade_calendar")
    champion_sort = ("resourceId", "esunny.test:id/es_fragment_login_btv_champion")
    skin_change = ("resourceId", "esunny.test:id/es_fragment_login_btv_change_skin")
    common_setting = ("resourceId", "esunny.test:id/es_fragment_login_btv_setting")
    about = ("resourceId", "esunny.test:id/es_fragment_login_btv_about")

    def selfCheck(self):
        self.check_element_exist(self.right_panel)

    def goToLoginPage(self) -> BasePage:
        if self.check_element_exist(self.trade_login):
            self.click(self.trade_login)
        else:
            self.click(self.multi_login)
        return LoginPage()

    def goToQuoteSetting(self) -> BasePage:
        self.click(self.quote_setting)
        return QuoteSetting()

    def goToTradeSetting(self) -> BasePage:
        self.click(self.trade_setting)
        return TradeSetting()

    def goToCondOrder(self) -> BasePage:
        self.click(self.condition_order)
        return CondOrderPage()

    def goToStopTrade(self) -> BasePage:
        self.click(self.stop_trade)

    def goToStopOrder(self) -> BasePage:
        self.click(self.stop_open)

    def goToPriceWarning(self) -> BasePage:
        self.click(self.price_warn)

    def goToTradeRelated(self) -> BasePage:
        self.click(self.trade_related)
        pass

    def goToMessage(self) -> BasePage:
        self.click(self.message)
        pass

    def goToQuoteLoginPage(self) -> QuoteLoginPage:
        self.click(self.quote_login)
        return QuoteLoginPage()

    def goToCloudServicePage(self) -> CloudServicePage:
        self.click(self.cloud_service)
        return CloudServicePage()

    def goToOpenAccount(self) -> BasePage:
        self.click(self.open_account)
        pass

    def goToQuoteMall(self) -> BasePage:
        self.click(self.star_store)

    def goToChampionSort(self) -> ChampionSortPage:
        self.click(self.champion_sort)
        return ChampionSortPage()

    def ChangeSkin(self) -> None:
        self.click(self.skin_change)

    def goToCommonSetting(self) -> BasePage:
        self.click(self.common_setting)
        return Setting()

    def goToAbout(self) -> BasePage:
        self.click(self.about)
        return AboutPage()

    def goToCalendar(self) -> BasePage:
        self.click(self.trade_calendar)
        return TradeCalendar()


if __name__ == '__main__':
    debugPage = RightToolBar()
    # Rt.click(Rt.menu_button)
    # Rt.goToAbout()
