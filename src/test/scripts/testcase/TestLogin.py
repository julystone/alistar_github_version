import os

import allure
import pytest

from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.framework.BaseTest import BaseTest
from src.test.scripts.framework.DataUtil import ReadExcel
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.framework.OsPathUtil import REPORT_DIR, DATA_DIR
from src.test.scripts.page.navigate._NavigateBasePage import NavigateBasePage
from src.test.scripts.page.setting.LoginPage import LoginPage
from src.test.scripts.page.interface.RightToolBar import RightToolBar

# file_path = DATA_DIR + r"/TestData.xlsx"
# sheet_name = 'Login'
# wb = ReadExcel(file_path, sheet_name)
# cases = wb.read_data_obj()


# TODO feature、story、step 后续都能写到excel里，隔离开代码
# TODO 登录页面没办法截屏


file_path = DATA_DIR + r"/TestData.xlsx"
sheet_name = 'Login2'
wb = ReadExcel(file_path, sheet_name)
case_list = wb.read_data_obj()


@allure.feature("交易登录")
class TestLogin(BaseTest):
    def recover_steps(self):
        Driver().appRestart()
        self.testPage = NavigateBasePage().goToRightToolBar().goToLoginPage()

    def init_steps(self):
        self.testPage = LoginPage()

    @allure.title("{case.testName}")
    @pytest.mark.parametrize("case", case_list)
    def testcase_LoginMulti(self, case):
        max_await_time = 30
        if not case.ifDDT:
            pytest.skip("No need to DDT")
        self.testPage \
            .chooseCompany(case.com, case.local, case.informal) \
            .inputUserNo(case.acc) \
            .inputPassWord(case.pwd) \
            .click(self.testPage.login_submit)
        loading_circle = (
            'xpath', '//*[@resource-id="esunny.estarandroid:id/customer_toast_container"]/android.widget.ImageView[1]')
        self.testPage.wait_element_gone(loading_circle, max_await_time)
        try:
            Asserter.PageHasText(self.testPage, case.checkpoint1)
        except AssertionError:
            Asserter.PageHasText(self.testPage, case.checkpoint2)

    # @allure.story("登录参数化测试")
    @allure.title("进入后退出交易登录")
    def testcase_quitPage(self):
        self.testPage.quitPage()
        tempPage = RightToolBar()
        Asserter.PageHasText(tempPage, '关于')

        # 页面恢复
        tempPage.goToLoginPage()

    @allure.title("记住密码勾选测试")
    def testcase_checkSavePwd(self):
        self.meta_checkTest(check=self.testPage.save_pwd)

    @allure.title("保存账号勾选测试")
    def testcase_checkSaveAccount(self):
        self.meta_checkTest(check=self.testPage.save_account)

    @allure.title("同意风险提示书勾选测试")
    def testcase_checkLoginNotice(self):
        self.meta_checkTest(check=self.testPage.login_notice)


if __name__ == '__main__':
    os.system(f"pytest TestSetting.py -vlsx --lf --alluredir {REPORT_DIR}\\.allureTemp")
    os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
