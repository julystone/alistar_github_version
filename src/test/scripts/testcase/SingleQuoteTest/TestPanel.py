import os

import allure
import pytest

from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.navigate.FavPage import FavPage
from src.test.scripts.page.navigate.QuotePage import QuotePage
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
        self.testPage = QuotePage()

    def recover_steps(self):
        Driver().appRestart()
        self.testPage = FavPage().goToQuotePage()

    @allure.title("盘口-均价显示-上证SSE")
    def testcase_quitPage(self):
        page = self.testPage.goToSingleQuotePage(quoteName='上证指数', exchangeName='上证SSE').goToPanelPage()
        # 页面恢复


if __name__ == '__main__':
    os.system(f"pytest TestSetting.py -vlsx --lf --alluredir {REPORT_DIR}\\.allureTemp")
    os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
