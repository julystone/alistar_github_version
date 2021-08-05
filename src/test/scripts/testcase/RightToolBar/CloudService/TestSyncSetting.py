import os

import allure
import pytest

from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.interface.RightToolBar import RightToolBar
from src.test.scripts.page.navigate.FavPage import FavPage
from src.test.scripts.page.rightToolBar.CloudServicePage import CloudServicePage
from src.test.scripts.page.rightToolBar.QuoteSetting import QuoteSetting
from src.test.scripts.testcase.BaseTest import BaseTest
from utils.OsPathUtil import REPORT_DIR


@allure.feature("设置同步")
class TestSyncSetting(BaseTest):
    pytestmark = [pytest.mark.smoke]

    def init_steps(self):
        self.testPage = CloudServicePage()

    def recover_steps(self):
        Driver().appRestart()
        self.rightToolBar = FavPage().goToRightToolBar()
        self.testPage = FavPage().goToRightToolBar().goToCloudServicePage()

    @allure.title("101148:云端服务-设置同步-常用周期设置")
    def testcase_001(self):
        self.testPage.settingSync("upload").quitPage()
        RightToolBar().goToQuoteSetting()
        QuoteSetting().goToCommonPeriodSetting().deletePeriod("1分钟").quitPage()
        QuoteSetting().quitPage()
        
        RightToolBar().goToCloudServicePage()
        self.testPage.settingSync("download").quitPage()


if __name__ == '__main__':
    os.system(f"pytest TestSetting.py -vlsx --lf --alluredir {REPORT_DIR}\\.allureTemp")
    os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
