import os

import allure

from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.framework.BaseTest import TestBase
from src.test.scripts.framework.OsPathUtil import REPORT_DIR
from src.test.scripts.page.setting.CommonSetting import CommonSetting
from src.test.scripts.page.setting.RightToolBar import RightToolBar


# file_path = DATA_DIR + r"/TestData.xlsx"
# sheet_name = 'Login'
# wb = ReadExcel(file_path, sheet_name)
# cases = wb.read_data_obj()


# TODO feature、story、step 后续都能写到excel里，隔离开代码
# TODO 为啥我的feature story不写进allure 报告里  和last failed有关吗？


@allure.feature("系统设置")
class TestCommonSetting(TestBase):
    def setup_class(self):
        try:
            self.testPage = CommonSetting()
        except AttributeError:
            RightToolBar().goToCommonSetting()
            self.testPage = CommonSetting()
        print("setup_class")

    def teardown_class(self):
        pass

    def teardown_function(self):
        self.testPage.selfCheck()

    @allure.title("进入后退出系统设置")
    def testcase_quitPage(self, DriverInit):
        self.testPage.quitPage()
        tempPage = RightToolBar()
        Asserter.PageHasText(tempPage, '关于')

        # 页面恢复
        tempPage.goToCommonSetting()

    @allure.title("进入语言选择，语言切换成English")
    def testcase_LangChoose(self, DriverInit):
        # 数据备份
        before = self.testPage.getCurLang()

        # 切换成English
        tempPage = self.testPage.goToLangChoose()
        after = tempPage.changeLang('English').getCurLang()
        # after = self.commonSettingPage.getCurLang()
        Asserter.TextEqualText(after, "English")

        # 页面恢复
        tempPage.changeLang(before).quitPage()

    def meta_switchTest(self, switch):
        # 数据备份
        before = self.testPage.getCurSwitchStatus(switch)

        # 切换
        self.testPage.click(switch)
        after = self.testPage.getCurSwitchStatus(switch)
        Asserter.BoolNotEqualBool(before, after)

        self.testPage.click(switch)

    @allure.title("断线提示音开关测试")
    def testcase_switchDisconnectRing(self, DriverInit):
        self.meta_switchTest(switch=self.testPage.disconnect_ring)

    @allure.title("交易提示音开关测试")
    def testcase_switchTradeRing(self, DriverInit):
        self.meta_switchTest(switch=self.testPage.trade_ring)

    @allure.title("消息提示音开关测试")
    def testcase_switchNotifyRing(self, DriverInit):
        self.meta_switchTest(switch=self.testPage.notify_ring)

    @allure.title("屏幕常亮开关测试")
    def testcase_switchNotifyRing(self, DriverInit):
        self.meta_switchTest(switch=self.testPage.screen_on_switch)


if __name__ == '__main__':
    os.system(f"pytest TestSetting.py -v --lf --alluredir {REPORT_DIR}\\.allureTemp")
    os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
