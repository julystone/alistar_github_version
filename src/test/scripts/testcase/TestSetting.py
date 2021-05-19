import os

import allure

from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.framework.BaseTest import BaseTest
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.framework.OsPathUtil import REPORT_DIR
from src.test.scripts.page.navigate.NavigateBasePage import NavigateBasePage
from src.test.scripts.page.setting.RightToolBar import RightToolBar
from src.test.scripts.page.setting.CommonSetting import CommonSetting


# file_path = DATA_DIR + r"/TestData.xlsx"
# sheet_name = 'Login'
# wb = ReadExcel(file_path, sheet_name)
# cases = wb.read_data_obj()


# TODO feature、story、step 后续都能写到excel里，隔离开代码
# TODO 为啥我的feature story不写进allure 报告里  和last failed有关吗？


@allure.feature("系统设置")
class TestCommonSetting(BaseTest):
    def start_steps(self):
        self.testPage = CommonSetting()

    def recover_steps(self):
        Driver().appRestart()
        NavigateBasePage().goToRightToolBar()
        RightToolBar().goToCommonSetting()
        self.testPage = CommonSetting()

    @allure.title("进入后退出系统设置")
    def testcase_quitPage(self):
        self.testPage.quitPage()
        tempPage = RightToolBar()
        Asserter.PageHasText(tempPage, '关于')

        # 页面恢复
        tempPage.goToCommonSetting()

    @allure.title("进入语言选择，语言切换成繁体")
    def testcase_LangChoose(self):
        # 数据备份
        before = self.testPage.getCurLang()

        # 切换成English
        tempPage = self.testPage.goToLangChoose()
        tempPage.changeLang('繁体中文').quitPage()
        after = self.testPage.getCurLang()
        Asserter.TextEqualText(after, "繁体中文")

        # 页面恢复
        self.testPage.goToLangChoose().changeLang(before).quitPage()

    def meta_switchTest(self, switch):
        # 数据备份
        before = self.testPage.getCurSwitchStatus(switch)

        # 切换
        self.testPage.click(switch)
        after = self.testPage.getCurSwitchStatus(switch)
        Asserter.BoolNotEqualBool(before, after)

        self.testPage.click(switch)

    @allure.title("断线提示音开关测试")
    def testcase_switchDisconnectRing(self):
        self.meta_switchTest(switch=self.testPage.disconnect_ring)

    @allure.title("交易提示音开关测试")
    def testcase_switchTradeRing(self):
        self.meta_switchTest(switch=self.testPage.trade_ring)

    @allure.title("消息提示音开关测试")
    def testcase_switchNotifyRing(self):
        self.meta_switchTest(switch=self.testPage.notify_ring)

    @allure.title("屏幕常亮开关测试")
    def testcase_switchScreenOnRing(self):
        self.meta_switchTest(switch=self.testPage.screen_on_switch)


if __name__ == '__main__':
    os.system(f"pytest TestSetting.py -vlsx --lf --alluredir {REPORT_DIR}\\.allureTemp")
    os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
