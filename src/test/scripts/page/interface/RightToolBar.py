from src.test.scripts.framework.Driver import Driver


class RightToolBar:
    # menu功能键
    menu_button = ('id', 'esunny.test:id/toolbar_right_first')
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
    starShine_mall = ('text', '星耀商场')
    skin_change = ('text', '换肤')
    common_setting = ('text', '设置')
    about = ('text', '关于')

    @staticmethod
    def goToLoginPage():
        Driver.click(RightToolBar.menu_button)
        if Driver.check_element_exist(RightToolBar.trade_login):
            Driver.click(RightToolBar.trade_login)
        else:
            Driver.click(RightToolBar.multi_login)

    @staticmethod
    def goToQuoteSetting():
        Driver.click(RightToolBar.quote_setting)

    @staticmethod
    def goToQuoteLoginPage():
        Driver.click(RightToolBar.quote_login)

    @staticmethod
    def goToPriceWarning():
        Driver.click(RightToolBar.price_warn)

    @staticmethod
    def goToCloudService():
        Driver.click(RightToolBar.cloud_service)

    @staticmethod
    def goToQuoteMall():
        Driver.click(RightToolBar.starShine_mall)

    @staticmethod
    def SkinChange():
        Driver.click(RightToolBar.skin_change)

    @staticmethod
    def goToCommonSetting():
        Driver.click(RightToolBar.common_setting)

    @staticmethod
    def goToAbout():
        Driver.click(RightToolBar.about)

    @staticmethod
    def goToCondOrder():
        Driver.click(RightToolBar.condition_order)

    @staticmethod
    def goToStopTrade():
        Driver.click(RightToolBar.stop_trade)

    @staticmethod
    def goToStopOrder():
        Driver.click(RightToolBar.stop_loss_opening)
