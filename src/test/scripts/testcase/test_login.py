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
sheet_name = 'Login'
wb = ReadExcel(file_path, sheet_name)
cases = wb.read_data_obj()


# 测试用例 = 测试对象的功能 + 测试数据
@allure.feature("测试登录界面")
class TestLoginPage(TestBase):
    # @allure.story("参数化测试多组登录账号")
    # @pytest.mark.parametrize("case", cases)
    # def testcase_login(self, case, getDriver):
    #     if not case.ifDDT:
    #         pytest.skip("No need to DDT")
    #     login_page = LoginPage(getDriver)
    #     login_page.gotoLoginPage() \
    #         .verify() \
    #         .chooseCompany(case.com) \
    #         .inputUserNo(case.acc) \
    #         .inputPassWord(case.pwd) \
    #         .clickSubmit()
    #     try:
    #         assert Driver.check_element_exist(login_page.driver, ('part-text', case.checkpoint1)) is True
    #     except AssertionError as e:
    #         Driver.get_screenshots_as_file(login_page.driver, extra=case.testNo)
    #         raise e

    @allure.story("参数化测试多组登录账号")
    @pytest.mark.parametrize("case", cases)
    def testcase_login(self, case, getDriverFactory):
        if not case.ifDDT:
            pytest.skip("No need to DDT")
        login_page = LoginPage(getDriverFactory())
        login_page.gotoLoginPage() \
            .verify() \
            .chooseCompany(case.com) \
            .inputUserNo(case.acc) \
            .inputPassWord(case.pwd) \
            .clickSubmit()
        try:
            assert Driver.check_element_exist(login_page.driver, ('part-text', case.checkpoint1)) is True
        except AssertionError as e:
            Driver.get_screenshots_as_file(login_page.driver, extra=case.testNo)
            raise e

    @allure.story("测试点击风险责任书")
    def testcase_clickRiskBook(self, getDriver):
        login_page = LoginPage(getDriver)
        login_page.gotoLoginPage()
        Driver.click(login_page.driver, login_page.risk_book)
        assert Driver.check_element_exist(login_page.driver, login_page.login_submit) is False

    @allure.story("测试点击左上角返回按钮")
    def testcase_clickBackwards(self, getDriver):
        login_page = LoginPage(getDriver)
        login_page.gotoLoginPage()
        Driver.click(login_page.driver, login_page.return_button)
        try:
            assert Driver.check_element_exist(login_page.driver, login_page.risk_book) is False
        except AssertionError as e:
            Driver.get_screenshots_as_file(login_page.driver)
            raise e

    @allure.story("测试密码输入 安全键盘的弹出")
    def testcase_clickPwdInput(self, getDriver):
        login_page = LoginPage(getDriver)
        login_page.gotoLoginPage()
        Driver.click(login_page.driver, login_page.login_pwd)
        assert Driver.check_element_exist(login_page.driver, login_page.risk_book) is False
        # assert login_page._check_element_exist(('part-text', '安全键盘')) is True


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o


if __name__ == '__main__':
    cmd1 = f"pytest test_login_pytest.py -v --lf --alluredir {REPORT_DIR}\\.allureTemp"
    Shell.invoke(cmd1)
    cmd2 = f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean"
    Shell.invoke(cmd2)
    # os.system(f"pytest test_login.py -v --lf --alluredir {REPORT_DIR}\\.allureTemp")
    # os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
