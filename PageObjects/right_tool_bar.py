from appium.webdriver.common.mobileby import MobileBy as By

from PageObjects.base_page import Page


class RightToolBar(Page):
    # menu功能键
    menu_button = (By.ID, 'esunny.test:id/toolbar_right_first')
    # 右侧边栏 - 交易登录
    login_port = ('text', '交易登录')

    def goToLoginPage(self):
        self._click(self.menu_button)
        self._click(self.login_port)
