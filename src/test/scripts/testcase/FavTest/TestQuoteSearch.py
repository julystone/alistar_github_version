import os

import allure
import pytest

from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.interface.QuoteSearch import QuoteSearch
from src.test.scripts.page.navigate.FavPage import FavPage
from src.test.scripts.testcase.BaseTest import BaseTest
from utils.DataUtil import ReadExcel
from utils.OsPathUtil import REPORT_DIR, DATA_DIR

file_path = DATA_DIR + r"/SearchTestData.xlsx"
sheet_name = 'Search2'
wb = ReadExcel(file_path, sheet_name)
case_list = wb.read_data_obj()


@allure.feature("交易登录")
class TestQuoteSearch(BaseTest):
    pytestmark = [pytest.mark.smoke]

    def init_steps(self):
        self.testPage = QuoteSearch()

    def recover_steps(self):
        Driver().appRestart()
        self.testPage = FavPage().goToQuoteSearch()

    @allure.title("搜索添加-搜索能力-{case.testName}")
    @pytest.mark.parametrize("case", case_list)
    def testcase_SearchMulti(self, case):
        if not case.ifDDT:
            pytest.skip("No need to DDT")
        self.testPage.searchQuote(case.quoteName)
        search_result = self.testPage.getSearchResult()
        try:
            Asserter.TextContainsText(search_result[0], case.checkpoint1)
        except AssertionError:
            Asserter.PageHasText(self.testPage, case.checkpoint2)

    @allure.title("进入后退出")
    def testcase_quitPage(self):
        self.testPage.quitPage()
        # 页面恢复
        FavPage().goToQuoteSearch()

    @allure.title("搜索添加-提示语显示")
    def testcase_searchText(self):
        res = self.testPage.getSearchText()
        expect = "搜索品种/合约/股票"
        Asserter.TextEqualText(res, expect)


if __name__ == '__main__':
    os.system(f"pytest TestSetting.py -vlsx --lf --alluredir {REPORT_DIR}\\.allureTemp")
    os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
