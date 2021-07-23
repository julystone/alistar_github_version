import os

import allure
import pytest

from src.test.scripts.framework import Asserter
from src.test.scripts.framework.BaseTest import BaseTest
from src.test.scripts.framework.DataUtil import ReadExcel
from src.test.scripts.framework.OsPathUtil import DATA_DIR, REPORT_DIR
from src.test.scripts.page.setting.LoginPage import LoginPage
from src.test.scripts.page.setting.RightToolBar import RightToolBar

file_path = DATA_DIR + r"/TestData.xlsx"
sheet_name = 'Login'
wb = ReadExcel(file_path, sheet_name)
cases = wb.read_data_obj()


# TODO feature、story、step 后续都能写到excel里，隔离开代码
# TODO 为啥我的feature story不写进allure 报告里  和last failed有关吗？


@allure.feature("登录模块")
@pytest.mark.specific
class TestLoginPage(BaseTest):
    @allure.title("{case.testName}")
    @pytest.mark.core
    @pytest.mark.parametrize("case", cases)
    def testcase_login(self, case, DriverInit):
        if not case.ifDDT:
            pytest.skip("No need to DDT")
        RightToolBar().goToLoginPage()
        LoginPage() \
            .chooseCompany(case.com) \
            .inputUserNo(case.acc) \
            .inputPassWord(case.pwd) \
            .clickSubmit()

        Asserter.shouldHaveText(case.checkpoint1)

    @allure.title("测试点击风险责任书")
    def testcase_clickRiskBook(self, DriverInit):
        RightToolBar().goToLoginPage()
        LoginPage() \
            .clickRiskBook()
        Asserter.notHaveText('请输入用户名')

    @allure.title("测试点击左上角返回按钮")
    def testcase_clickBackwards(self, DriverInit):
        RightToolBar().goToLoginPage()
        LoginPage() \
            .clickBackwards()
        Asserter.notHaveText('请输入用户名')

    @allure.title("测试密码输入 安全键盘的弹出")
    def estcase_clickPwdInput(self, DriverInit):
        RightToolBar().goToLoginPage()
        LoginPage() \
         .clickSubmit()
        Asserter.shouldHaveText('安全键盘')
        # assert login_page._check_element_exist(('part-text', '安全键盘')) is True


if __name__ == '__main__':
    os.system(f"pytest test_login.py -v --lf --alluredir {REPORT_DIR}\\.allureTemp")
    os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
