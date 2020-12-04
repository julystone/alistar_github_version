import time

from appium.webdriver.common.mobileby import MobileBy as By

from PageObjects.right_tool_bar import RightToolBar
from common.BasePage import Page
from common.Driver import Driver
from common.MyLogger import my_log


class LoginPage(Page):
    # title
    title = (By.ID, 'esunny.test:id/toolbar_title')
    # 左侧退出按钮
    return_button = (By.ID, 'esunny.test:id/toolbar_left_first')
    # 后台选址
    login_company = (By.ID, 'esunny.test:id/et_login_company')
    # 账号输入
    login_userno = (By.ID, 'esunny.test:id/et_login_userno')
    # 密码输入
    login_pwd = (By.ID, 'esunny.test:id/et_login_pwd')
    # 提交按钮
    login_submit = (By.ID, r'esunny.test:id/tv_login_submit')
    # 保存账号
    save_account = (By.ID, r'esunny.test:id/es_login_activity_login_itv_save_account')
    # 保存密码
    save_pwd = (By.ID, r'esunny.test:id/es_login_activity_login_etv_save_pwd')
    # 已阅读勾选
    login_notice = (By.ID, 'esunny.test:id/es_activity_login_notice_check')
    # 风险提示书
    risk_book = (By.ID, r'esunny.test:id/es_activity_login_tv_state_confirm')

    # 启明星后台
    qiMing = ('part-text', '启明星（上海仿真）')
    # 北斗星后台
    beiDou = ('part-text', '北斗星（上海仿真）')

    def gotoLoginPage(self):
        right_tool_bar = RightToolBar(self.driver)
        right_tool_bar.goToLoginPage()
        return self

    # 选择后台
    def choose_company(self, text):
        print(f"正在切换{text}后台")
        my_log.info(f"正在切换{text}后台")
        Driver.click(self.driver, self.login_company)
        time.sleep(2)
        Driver.click(self.driver, self.qiMing)
        return self

    def input_userNo(self, userNo):
        print(f"正在输入userNo{userNo}")
        my_log.info(f"正在输入userNo{userNo}")
        Driver.input_text(self.driver, self.login_userno, userNo)
        return self

    def input_passWord(self, pwd):
        print(f"正在输入passWord{pwd}")
        my_log.info(f"正在输入passWord{pwd}")
        Driver.input_text(self.driver, self.login_pwd, pwd)
        return self

    def click_submit(self):
        print("点击登录按钮")
        my_log.info("点击登录按钮")
        Driver.click(self.driver, self.login_submit)
        return self

    # def check_login(self):
    #     print("检测是否登录成功")
    #     my_log.info("检测是否登录成功")
    #     assert self._check_element_exist(self.click_submit()) is False
    #     return self


if __name__ == '__main__':
    driver = Driver(0)
    log = LoginPage(driver.driver)
    try:
        log.gotoLoginPage(). \
            choose_company("启明星"). \
            input_userNo("Q1223871051"). \
            input_passWord("111111"). \
            click_submit()
    except Exception as e:
        print(e)
    log.driver.quit()
