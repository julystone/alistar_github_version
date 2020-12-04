from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from common.BasePage import Page


class SelfPage(Page):
    # 自选titile
    self_title = (By.ID, 'esunny.test:id/toolbar_title')
    # 右侧菜单键
    menu_button = (By.ID, 'esunny.test:id/toolbar_right_first')
    # 右侧加号
    add_button = (By.ID, 'esunny.test:id/toolbar_right_second')
    # 左侧扳手键
    sort_button = (By.ID, 'esunny.test:id/toolbar_left_first')
    # 右侧边栏 - 交易登录
    login_port = ('text', '交易登录')

    def __init__(self):
        Page.__init__(self)

    def click_menu(self):
        self._click(self.menu_button)

    def goToLoginPage(self):
        self.click_menu()
        self._click(self.login_port)
        pass

    def is_page_changed(self):
        """
        检测页面是否改变
        :return: True 则页面已不再是登录页面
        """
        print("检测当前是否仍在页面")
        try:
            element = self._find_element(By.XPATH, u'//p[@class="sloganText2"]')
        except NoSuchElementException:
            print("NoSuchElementFound")
            return True
        else:
            print(element)
            return False
