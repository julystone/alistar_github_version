import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By

from PageObjects.base_page import Page
from PageObjects.right_tool_bar import RightToolBar
from common import R_r_config
from common.R_r_log import my_log


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
    # save_account = (By.ID, r"esunny.test:id/es_login_activity_login_itv_save_account")
    # 保存密码
    save_pwd = (By.ID, r'esunny.test:id/es_login_activity_login_etv_save_pwd')
    # 已阅读勾选
    login_notice = (By.ID, 'esunny.test:id/es_activity_login_notice_check')
    # 风险提示书
    risk_book = (By.ID, r'esunny.test:id/es_activity_login_tv_state_confirm')

    # 启明星后台
    qiMing = ('part-text', '启明星（上海仿真2）')
    # 北斗星后台
    beiDou = ('part-text', '北斗星（上海仿真2）')

    def gotoLoginPage(self):
        right_tool_bar = RightToolBar(self.driver)
        right_tool_bar.goToLoginPage()

    # 选择后台
    def choose_company(self, text):
        print(f"正在切换{text}后台")
        my_log.info(f"正在切换{text}后台")
        self._click(self.login_company)
        time.sleep(2)
        self._click(self.qiMing)

    def input_userNo(self, userNo):
        print(f"正在输入userNo{userNo}")
        my_log.info(f"正在输入userNo{userNo}")
        self._input_text(self.login_userno, userNo)

    def input_passWord(self, pwd):
        print(f"正在输入passWord{pwd}")
        my_log.info(f"正在输入passWord{pwd}")
        self._input_text(self.login_pwd, pwd)

    def click_submit(self):
        print("点击登录按钮")
        my_log.info("点击登录按钮")
        self._click(self.login_submit)

    def check_login(self):
        print("检测是否登录成功")
        my_log.info("检测是否登录成功")
        self._get_screenshots_as_file()
        assert self._check_element_exist(self.click_submit()) is False


if __name__ == '__main__':
    test_phone_config = R_r_config.ConfigData(0)
    Desired_Caps = dict(test_phone_config["test_phone"])
    print(Desired_Caps)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', Desired_Caps)
    log = LoginPage(driver)
    try:
        log.gotoLoginPage()
        log.choose_company("启明星")
        log.input_userNo("Q1223871051")
        log.input_passWord("111111")
        log.click_submit()
    except Exception as e:
        print(e)
    log.driver.quit()
