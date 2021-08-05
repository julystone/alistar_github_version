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
sheet_name_test = 'Quote_test'
sheet_name_all = 'Quote_all'
sheet_name_smoke = 'Quote_smoke'
case_list_test = ReadExcel(file_path, sheet_name_test).read_data_obj()
case_list_all = ReadExcel(file_path, sheet_name_all).read_data_obj()
case_list_smoke = ReadExcel(file_path, sheet_name_smoke).read_data_obj()


@allure.feature("进入合约")
class TestQuote(BaseTest):
    @classmethod
    def init_steps_class(cls):
        Driver().add_watcher("行情授权提示", "提示", "取消")

    def recover_steps(self):
        Driver().appRestart()
        self.testPage = FavPage().goToQuotePage()

    def init_steps(self):
        self.testPage = QuotePage()

    @pytest.mark.core
    @allure.title("{case.testName}")
    @pytest.mark.parametrize("case", case_list_all)
    def testcase_LoginMulti(self, case):
        if not case.ifDDT:
            pytest.skip("No need to DDT")
        if case.exchangeName:
            self.testPage.changeExchange(case.exchangeName)
            Asserter.TextContainsText(self.testPage.getCurTitle(), case.checkpoint1)

        if case.barName:
            self.testPage.scrollToCommodity(case.barName)
            Asserter.TextContainsText(self.testPage.getQuoteList()[0], case.checkpoint2)

        if case.quoteName:
            quotePage = self.testPage.goToSingleQuotePage(case.quoteName)
            Asserter.TextContainsText(quotePage.getCurQuote(), case.checkpoint3)
            # 页面恢复
            quotePage.quitPage()

    @pytest.mark.smoke
    @allure.title("{case.testName}")
    @pytest.mark.parametrize("case", case_list_smoke)
    def testcase_LoginMulti(self, case):
        if not case.ifDDT:
            pytest.skip("No need to DDT")
        if case.exchangeName:
            self.testPage.changeExchange(case.exchangeName)
            Asserter.TextContainsText(self.testPage.getCurTitle(), case.checkpoint1)

        if case.barName:
            self.testPage.scrollToCommodity(case.barName)
            Asserter.TextContainsText(self.testPage.getQuoteList()[0], case.checkpoint2)

        if case.quoteName:
            quotePage = self.testPage.goToSingleQuotePage(case.quoteName)
            Asserter.TextContainsText(quotePage.getCurQuote(), case.checkpoint3)
            # 页面恢复
            quotePage.quitPage()


if __name__ == '__main__':
    os.system(f"pytest TestSetting.py -m smoke -vlsx --lf --alluredir {REPORT_DIR}\\.allureTemp")
    os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
