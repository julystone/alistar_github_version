from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.framework.BasePage import BasePage
from src.test.scripts.framework.Driver_atx import Driver


class SettingBasePage(BasePage, Driver):
    # 顶部栏
    title = ("resourceId", "esunny.test:id/toolbar_title")
    quit_btn = ("resourceId", "esunny.test:id/toolbar_left_icons")
    # 校验项
    title_text = "测试标题"

    def __init__(self):
        Driver.__init__(self)
        BasePage.__init__(self)

    def selfCheck(self):
        self.force_sleep(2)
        Asserter.TextEqualText(self.getCurTitle(), self.title_text)
        # pass

    def getCurTitle(self):
        # 获取当前标题
        return self.get_text(self.title)

    def quitPage(self):
        self.click(self.quit_btn)
        return self


if __name__ == '__main__':
    debugPage = SettingBasePage()
    debugPage.title = ('text', '常用系统设置')
    loc1 = ("text", "1分钟")
    elem1 = debugPage.findElemWithoutException(loc1).sibling()
    loc2 = ("text", "15分钟")
    elem2 = debugPage.findElemWithoutException(loc2).sibling()
    print(debugPage.checkIfChosen(elem1))
    print(debugPage.checkIfChosen(elem2))

    # debugPage.quitPage()
