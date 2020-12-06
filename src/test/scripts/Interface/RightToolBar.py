from src.test.scripts.framework.Driver import Driver


class RightToolBar:
    # menu功能键
    menu_button = ('id', 'esunny.test:id/toolbar_right_first')
    # 右侧边栏 - 交易登录
    trade_login = ('text', '交易登录')
    # 右侧边栏 - 行情设置
    quote_setting = ('text', '行情设置')
    # 右侧边栏 - 交易设置
    trade_setting = ('text', '交易设置')
    # 有侧边栏 - 行情登陆
    quote_login = ('text', '行情登陆')
    # 右侧边栏 - 价格预警 - 未登陆行情账号不会出现
    price_warning = ('text', '价格预警')
    # 右侧边栏 - 云端服务 - 未登陆行情账号不会出现
    cloud_service = ('text', '云端服务')
    # 右侧边栏 - 在线开户
    create_accountOL = ('text', '在线开户')
    # 右侧边栏 - 星耀商场
    quote_mall = ('text', '星耀商场')
    # 右侧边栏 - 换肤
    skin_setting = ('text', '换肤')
    # 右侧边栏 - 设置
    common_setting = ('text', '设置')
    # 右侧边栏 - 关于
    about = ('text', '关于')
    # 右侧边栏 - 止损开仓
    stop_open = ('text', '关于')
    # 右侧边栏 - 云条件单
    cond_order = ('text', '关于')
    # 右侧边栏 - 止损止盈
    stop_order = ('text', '关于')

    @staticmethod
    def goToLoginPage(driver):
        Driver.click(driver, RightToolBar.menu_button)
        Driver.click(driver, RightToolBar.trade_login)

    @staticmethod
    def goToQuoteSetting(driver):
        Driver.click(driver, RightToolBar.quote_setting)

    @staticmethod
    def goToQuoteLoginPage(driver):
        Driver.click(driver, RightToolBar.quote_login)

    @staticmethod
    def goToPriceWarning(driver):
        Driver.click(driver, RightToolBar.price_warning)

    @staticmethod
    def goToCloudService(driver):
        Driver.click(driver, RightToolBar.cloud_service)

    @staticmethod
    def goToQuoteMall(driver):
        Driver.click(driver, RightToolBar.quote_mall)

    @staticmethod
    def goToSkinChange(driver):
        Driver.click(driver, RightToolBar.skin_setting)

    @staticmethod
    def goToCommonSetting(driver):
        Driver.click(driver, RightToolBar.common_setting)

    @staticmethod
    def goToAbout(driver):
        Driver.click(driver, RightToolBar.about)

    @staticmethod
    def goToStopOpen(driver):
        Driver.click(driver, RightToolBar.stop_open)

    @staticmethod
    def goToCondOrder(driver):
        Driver.click(driver, RightToolBar.cond_order)

    @staticmethod
    def goToStopOrder(driver):
        Driver.click(driver, RightToolBar.stop_order)
