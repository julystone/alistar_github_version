import os
import subprocess

import allure
import pytest

from src.test.scripts.framework.BaseTest import TestBase
from src.test.scripts.framework.DataUtil import ReadExcel
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.framework.OsPathUtil import DATA_DIR, REPORT_DIR
from src.test.scripts.page.LoginPage import LoginPage

file_path = DATA_DIR + r"/TestData.xlsx"
sheet_name = 'Login1'
wb = ReadExcel(file_path, sheet_name)
cases = wb.read_data_obj()


def screenshot_allure(func):
    def get_err_screenshot(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except AssertionError as e:
            png = Driver.get_screenshot_as_file(kwargs["driver"])
            allure.attach(png, allure.attachment_type.PNG)
            raise e
        return get_err_screenshot


# TODO feature、story、step 后续都能写到excel里，隔离开代码

# 测试用例 = 测试对象的功能 + 测试数据
@allure.feature("测试登录界面")
class TestLoginPage(TestBase):
    @allure.story("参数化测试多组登录账号")
    @pytest.mark.parametrize("case", cases)
    def testcase_login(self, case, getDriver):
        if not case.ifDDT:
            pytest.skip("No need to DDT")
        login_page = LoginPage(getDriver)
        login_page.gotoLoginPage() \
            .verify() \
            .chooseCompany(case.com) \
            .inputUserNo(case.acc) \
            .inputPassWord(case.pwd) \
            .clickSubmit()
        assert Driver.check_element_exist(login_page.driver, ('part-text', case.checkpoint1)) is True

    # @allure.story("参数化测试多组登录账号")
    # @pytest.mark.parametrize("case", cases)
    # def testcase_login(self, case, getDriverFactory):
    #     if not case.ifDDT:
    #         pytest.skip("No need to DDT")
    #     login_page = LoginPage(getDriverFactory())
    #     login_page.gotoLoginPage() \
    #         .verify() \
    #         .chooseCompany(case.com) \
    #         .inputUserNo(case.acc) \
    #         .inputPassWord(case.pwd) \
    #         .clickSubmit()
    #     assert Driver.check_element_exist(login_page.driver, ('part-text', case.checkpoint1)) is True

    @allure.story("测试点击风险责任书")
    def estcase_clickRiskBook(self, getDriver):
        login_page = LoginPage(getDriver)
        login_page.gotoLoginPage() \
            .verify()
        with allure.step("点击风险责任书"):
            Driver.click(login_page.driver, login_page.risk_book)
        assert Driver.check_element_exist(login_page.driver, login_page.login_submit) is False

    @allure.story("测试点击左上角返回按钮")
    def estcase_clickBackwards(self, getDriver):
        login_page = LoginPage(getDriver)
        login_page.gotoLoginPage() \
            .verify()
        with allure.step("点击左上角返回按钮"):
            Driver.click(login_page.driver, login_page.return_button)
        try:
            assert Driver.check_element_exist(login_page.driver, login_page.risk_book) is False
        except AssertionError as e:
            Driver.get_screenshot_as_file(login_page.driver)
            raise e

    @allure.story("测试密码输入 安全键盘的弹出")
    def estcase_clickPwdInput(self, getDriver):
        login_page = LoginPage(getDriver)
        login_page.gotoLoginPage() \
            .verify()
        with allure.step("点击密码输入框"):
            Driver.click(login_page.driver, login_page.login_pwd)
        with allure.step("检测到键盘"):
            assert Driver.check_element_exist(login_page.driver, login_page.risk_book) is False
        # assert login_page._check_element_exist(('part-text', '安全键盘')) is True


if __name__ == '__main__':
    os.system(f"pytest test_login.py -v --lf --alluredir {REPORT_DIR}\\.allureTemp")
    os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
