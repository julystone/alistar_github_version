import os

import allure
import pytest

from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.navigate.FavPage import FavPage
from src.test.scripts.page.navigate.QuotePage import QuotePage
from src.test.scripts.testcase.BaseTest import BaseTest
from utils.DataUtil import ReadExcel
from utils.OsPathUtil import REPORT_DIR, DATA_DIR

"""
测试行情进出，一级二级板块选择
"""

file_path = DATA_DIR + r"/QuoteTestData.xlsx"
sheet_name = 'Quote2'
wb = ReadExcel(file_path, sheet_name)
case_list = wb.read_data_obj()


@allure.feature("行情登陆")
class TestQuote(BaseTest):
    @classmethod
    def init_steps_class(cls):
        Driver().add_watcher("行情授权提示", "提示", "取消")

    def recover_steps(self):
        Driver().appRestart()
        self.testPage = FavPage().goToQuotePage()

    def init_steps(self):
        self.testPage = QuotePage()

    @allure.title("{case.testName}")
    @pytest.mark.parametrize("case", case_list)
    def testcase_LoginMulti(self, case):
        if not case.ifDDT:
            pytest.skip("No need to DDT")
        self.testPage.changeExchange(case.exchangeName) \
            .scrollToCommodity(case.barName)
        tempPage = self.testPage.goToSingleQuotePage(case.quoteName)
        try:
            Asserter.PageHasText(self.testPage, case.checkpoint1)
        except AssertionError:
            Asserter.PageHasText(self.testPage, case.checkpoint2)

        # 页面恢复
        tempPage.quitPage()
    #
    # # @allure.story("登录参数化测试")
    # @allure.title("进入后退出交易登录")
    # def testcase_quitPage(self):
    #     self.testPage.quitPage()
    #     tempPage = rightToolBar()
    #     Asserter.PageHasText(tempPage, '关于')
    #
    #     # 页面恢复
    #     tempPage.goToLoginPage()
    #
    # @allure.title("记住密码勾选测试")
    # def testcase_checkSavePwd(self):
    #     self.meta_checkTest(check=self.testPage.save_pwd)
    #
    # @allure.title("保存账号勾选测试")
    # def testcase_checkSaveAccount(self):
    #     self.meta_checkTest(check=self.testPage.save_account)
    #
    # @allure.title("同意风险提示书勾选测试")
    # def testcase_checkLoginNotice(self):
    #     self.meta_checkTest(check=self.testPage.login_notice)
    #


if __name__ == '__main__':
    os.system(f"pytest TestSetting.py -vlsx --lf --alluredir {REPORT_DIR}\\.allureTemp")
    os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
