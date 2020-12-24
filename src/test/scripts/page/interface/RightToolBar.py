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
    def goToLoginPage(driver):
        Driver.click(driver, RightToolBar.menu_button)
        if Driver.check_element_exist(Driver, RightToolBar.trade_login):
            Driver.click(driver, RightToolBar.trade_login)
        else:
            Driver.click(driver, RightToolBar.multi_login)

    @staticmethod
    def goToQuoteSetting(driver):
        Driver.click(driver, RightToolBar.quote_setting)

    @staticmethod
    def goToQuoteLoginPage(driver):
        Driver.click(driver, RightToolBar.quote_login)

    @staticmethod
    def goToPriceWarning(driver):
        Driver.click(driver, RightToolBar.price_warn)

    @staticmethod
    def goToCloudService(driver):
        Driver.click(driver, RightToolBar.cloud_service)

    @staticmethod
    def goToQuoteMall(driver):
        Driver.click(driver, RightToolBar.starShine_mall)

    @staticmethod
    def SkinChange(driver):
        Driver.click(driver, RightToolBar.skin_change)

    @staticmethod
    def goToCommonSetting(driver):
        Driver.click(driver, RightToolBar.common_setting)

    @staticmethod
    def goToAbout(driver):
        Driver.click(driver, RightToolBar.about)

    @staticmethod
    def goToCondOrder(driver):
        Driver.click(driver, RightToolBar.condition_order)

    @staticmethod
    def goToStopTrade(driver):
        Driver.click(driver, RightToolBar.stop_trade)

    @staticmethod
    def goToStopOrder(driver):
        Driver.click(driver, RightToolBar.stop_loss_opening)
