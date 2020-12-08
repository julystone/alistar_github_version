import os
import time

from appium.webdriver.common.mobileby import MobileBy as By

from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.Interface.RightToolBar import RightToolBar
import pytest
import allure


class LoginPage(Page):
    # title
    title = (By.ID, 'esunny.test:id/toolbar_title')
    # 左侧退出按钮
    return_button = (By.ID, 'esunny.test:id/toolbar_left_first')
    # 后台选址
    login_company = (By.ID, 'esunny.test:id/et_login_company')
    # 账号输入
    login_userNo = (By.ID, 'esunny.test:id/et_login_userno')
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

    @allure.step("校验页面")
    def verify(self):
        Driver.check_element_exist(self.driver, self.risk_book)
        return self

    @allure.step("调用右边栏接口，进入登录页面")
    def gotoLoginPage(self):
        RightToolBar.goToLoginPage(self.driver)
        return self

    @allure.step("选择开户公司")
    def chooseCompany(self, text):
        print(f"正在切换{text}后台")
        my_log.info(f"正在切换{text}后台")
        Driver.click(self.driver, self.login_company)
        time.sleep(2)
        Driver.click(self.driver, self.qiMing)
        return self

    @allure.step("输入交易账号")
    def inputUserNo(self, userNo):
        print(f"正在输入userNo{userNo}")
        my_log.info(f"正在输入userNo{userNo}")
        Driver.input_text(self.driver, self.login_userNo, userNo)
        return self

    @allure.step("输入交易密码")
    def inputPassWord(self, pwd):
        print(f"正在输入passWord{pwd}")
        my_log.info(f"正在输入passWord{pwd}")
        Driver.input_text(self.driver, self.login_pwd, pwd)
        return self

    @allure.step("点击登录")
    def clickSubmit(self):
        print("点击登录按钮")
        my_log.info("点击登录按钮")
        Driver.click(self.driver, self.login_submit)
        return self


@allure.feature("登录功能")
class TestLogin:
    @allure.story("正常登录")
    def test_login_success(self):
        dd = Driver(0).driver
        log = LoginPage(dd)
        try:
            log.gotoLoginPage(). \
                verify(). \
                chooseCompany("启明星"). \
                inputUserNo("Q1223871051"). \
                inputPassWord("111111"). \
                clickSubmit()
        except Exception as e:
            print(e)
        # log.quit()


if __name__ == '__main__':
    pytest.main(["-v", "--alluredir", "./report/.allureTemp"])
    os.system("allure generate ./report/.allureTemp -o ./report/allure --clean")
