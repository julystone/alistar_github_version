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

    def quitPage(self):
        self.click(self.quit_btn)


if __name__ == '__main__':
    debugPage = SettingBasePage()
    res = debugPage.quitPage()
