from appium.webdriver.common.mobileby import MobileBy as By

from common.BasePage import Page
from common.Driver import Driver


class RightToolBar(Page):
    # menu功能键
    menu_button = (By.ID, 'esunny.test:id/toolbar_right_first')
    # 右侧边栏 - 交易登录
    login_port = ('text', '交易登录')

    def goToLoginPage(self):
        Driver.click(self.driver, self.menu_button)
        Driver.click(self.driver, self.login_port)
        return self
