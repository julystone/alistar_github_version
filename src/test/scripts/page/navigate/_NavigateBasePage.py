import allure

from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.framework.BasePage import BasePage
from src.test.scripts.framework.Driver_atx import Driver


class NavigateBasePage(BasePage, Driver):
    # 顶部栏
    title = ("resourceId", "esunny.test:id/toolbar_title")
    right_tool = ('xpath', '//*[@resource-id="esunny.test:id/toolbar_right_icons"]/android.widget.FrameLayout[1]')

    # 底部导航
    switch2fav = ("resourceId", "esunny.test:id/nav_item_favorite")
    switch2quote = ("resourceId", "esunny.test:id/nav_item_quote")
    switch2trade = ("resourceId", "esunny.test:id/nav_item_trade")
    switch2news = ("resourceId", "esunny.test:id/nav_item_news")

    # 校验项
    title_text = "导航栏测试标题"

    def __init__(self):
        Driver.__init__(self)
        BasePage.__init__(self)

    def selfCheck(self):
        self.force_sleep(2)
        with allure.step("校验当前页面："+self.title_text):
            allure.attach(body=self.get_screenshot_as_png(), name='当前页面', attachment_type=allure.attachment_type.PNG)
            Asserter.TextEqualText(self.getCurTitle(), self.title_text)

    def getCurTitle(self):
        return self.get_text(self.title)

    def goToRightToolBar(self):
        self.wait_element(self.right_tool, 20)
        self.click(self.right_tool)
        from src.test.scripts.page.interface.RightToolBar import RightToolBar
        return RightToolBar()

    def goToFavPage(self):
        self.click(self.switch2fav)

    def goToQuotePage(self):
        self.click(self.switch2quote)

    def goToTradePage(self):
        self.click(self.switch2trade)
        return self

    def goToNewsPage(self):
        self.click(self.switch2news)


if __name__ == '__main__':
    debugPage = NavigateBasePage()
    res = debugPage.goToFavPage()
