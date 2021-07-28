import os

import allure

from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.interface.RightToolBar import RightToolBar
from src.test.scripts.page.navigate.FavPage import FavPage
from src.test.scripts.page.setting.CommonSetting import CommonSetting
from src.test.scripts.testcase.BaseTest import BaseTest
from utils.OsPathUtil import REPORT_DIR


# TODO feature、story、step 后续都能写到excel里，隔离开代码
# TODO 为啥我的feature story不写进allure 报告里  和last failed有关吗？


@allure.feature("系统设置")
class TestCommonSetting(BaseTest):
    def recover_steps(self):
        Driver().appRestart()
        FavPage().goToRightToolBar()
        RightToolBar().goToCommonSetting()
        self.testPage = CommonSetting()

    def init_steps(self):
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
        after = self.testPage.changeLang("繁体中文").getCurLang()
        Asserter.TextEqualText(after, "繁体中文")

        # 页面恢复
        self.testPage.changeLang(before)

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

    @allure.title("点击清除自选，校验弹框")
    def testcase_switchScreenOnRing(self):
        self.testPage.clearFavorites()
        Asserter.PageHasText(self.testPage, "提示")
        self.testPage.clickText("取消")

    @allure.title("点击清除账号，校验弹框")
    def testcase_switchScreenOnRing(self):
        self.testPage.clearAccount()
        Asserter.PageHasText(self.testPage, "提示")
        self.testPage.clickText("取消")


if __name__ == '__main__':
    os.system(f"pytest TestSetting.py -vlsx --lf --alluredir {REPORT_DIR}\\.allureTemp")
    os.system(f"allure generate {REPORT_DIR}\\.allureTemp -o {REPORT_DIR}\\allure --clean")
