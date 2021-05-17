from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver_atx import Driver


class SettingBasePage(Page, Driver):
    # 顶部栏
    title = ("resourceId", "esunny.test:id/toolbar_title")
    quit_btn = ("resourceId", "esunny.test:id/toolbar_left_icons")

    def selfCheck(self):
        pass

    def getCurTitle(self):
        return self.get_text(self.title)

    def changeOneSwitch(self, switch, expect):
        switch_selector = self.findElemWithoutException(switch)
        if switch_selector.info['checked'] != expect:
            switch_selector.click()

    def getCurSwitchStatus(self, switch):
        return self.findElemWithoutException(switch).info['checked']

    def getCurItemStatus(self, item):
        return self.findElemWithoutException(item).info['selected']

    def quitPage(self):
        self.click(self.quit_btn)


if __name__ == '__main__':
    debugPage = SettingBasePage()
    debugPage.title = ('text', '系统设置')
    debugPage.quit_btn = ("resourceId", "esunny.test:id/es_activity_system_setting_iv_back")

    debugPage.quitPage()
