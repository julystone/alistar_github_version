import os

import allure
import pytest

from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.interface.RightToolBar import RightToolBar
from src.test.scripts.page.navigate.FavPage import FavPage
from src.test.scripts.page.rightToolBar.LoginPage import LoginPage
from src.test.scripts.testcase.BaseTest import BaseTest
from utils.DataUtil import ReadExcel
from utils.OsPathUtil import REPORT_DIR, DATA_DIR

file_path = DATA_DIR + r"/LoginTestData.xlsx"
sheet_name = 'Login2'
wb = ReadExcel(file_path, sheet_name)
case_list = wb.read_data_obj()


@allure.feature("交易登录")
class TestLogin(BaseTest):
    pytestmark = [pytest.mark.smoke]

    @classmethod
    def init_steps_class(cls):
        Driver().add_watcher('消息弹框', '上一条', '上一条')

    def init_steps(self):
        self.testPage = LoginPage()

    def recover_steps(self):
        Driver().appRestart()
        self.testPage = FavPage().goToRightToolBar().goToLoginPage()

    @allure.title("{case.testName}")
    @pytest.mark.parametrize("case", case_list)
    def testcase_LoginMulti(self, case):
        max_await_time = 30
        if not case.ifDDT:
            pytest.skip("No need to DDT")
        self.testPage \
            .chooseCompany(case.com, case.local, case.informal) \
            .inputPassWord(case.pwd) \
            .inputUserNo(case.acc) \
            .clickSubmit()
        loading_circle = (
            'xpath', '//*[@resource-id="esunny.estarandroid:id/customer_toast_container"]/android.widget.ImageView[1]')
        self.testPage.wait_element_gone(loading_circle, max_await_time)
        try:
            Asserter.PageHasText(self.testPage, case.checkpoint1)
        except AssertionError:
            Asserter.PageHasText(self.testPage, case.checkpoint2)

        # 页面恢复
        try:
            RightToolBar().goToLoginPage()
        except AttributeError:
            print("页面异常，无法自动恢复")

    @allure.title("进入后退出交易登录")
    def testcase_quitPage(self):
        self.testPage.quitPage()
        # 页面恢复
        RightToolBar().goToLoginPage()

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
