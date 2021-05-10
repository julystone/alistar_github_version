from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.rightTool.CommonSetting import CommonSetting


class RightToolBar(Page, Driver):
    # menu功能键
    menu_button = ('xpath', '//*[@resource-id="esunny.test:id/toolbar_right_icons"]/android.widget.FrameLayout[1]')
    # 右侧边栏 - 交易类
    trade_login = ('text', '交易登录')
    multi_login = ('text', '多账号登录')
    quote_setting = ('text', '行情设置')
    trade_setting = ('text', '交易设置')
    condition_order = ('text', '云条件单')
    stop_trade = ('text', '止损止盈')
    stop_loss_opening = ('text', '止损开仓')
    price_warn = ('text', '价格预警')
    trade_related = ('text', '交易相关')
    message = ('text', '消息')

    # 右侧边栏 - 行情类
    quote_login = ('text', '行情登陆')
    cloud_service = ('text', '云端服务')
    open_account = ('text', '在线开户')
    trade_calendar = ('text', '交易日历')
    starShine_mall = ('text', '星耀商场')
    skin_change = ('text', '换肤')
    common_setting = ('text', '设置')
    about = ('text', '关于')

    def __init__(self):
        super().__init__()
        if not self.check_element_exist(self.trade_login):
            self.click(self.menu_button)
            self.check_element_exist(self.trade_login)

    def goToLoginPage(self):
        self.click(self.menu_button)
        if self.check_element_exist(self.trade_login):
            self.click(self.trade_login)
        else:
            self.click(self.multi_login)

    def goToQuoteSetting(self):
        self.click(self.quote_setting)

    def goToQuoteLoginPage(self):
        self.click(self.quote_login)

    def goToPriceWarning(self):
        self.click(self.price_warn)

    def goToCloudService(self):
        self.click(self.cloud_service)

    def goToQuoteMall(self):
        self.click(self.starShine_mall)

    def SkinChange(self):
        self.click(self.skin_change)

    def goToCommonSetting(self):
        self.click(self.common_setting)
        return CommonSetting()

    def goToAbout(self):
        self.click(self.about)

    def goToCondOrder(self):
        self.click(self.condition_order)

    def goToStopTrade(self):
        self.click(self.stop_trade)

    def goToStopOrder(self):
        self.click(self.stop_loss_opening)

    def goToCalendar(self):
        self.click(self.trade_calendar)


if __name__ == '__main__':
    Rt = RightToolBar()
    Rt.click(Rt.menu_button)
    Rt.goToAbout()
