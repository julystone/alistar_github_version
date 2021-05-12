from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver_atx import Driver


class NavigateBasePage(Page, Driver):
    # 顶部栏
    title = ("resourceId", "esunny.test:id/toolbar_title")
    menu_button = ('xpath', '//*[@resource-id="esunny.test:id/toolbar_right_icons"]/android.widget.FrameLayout[1]')

    # 底部导航
    switch2fav = ("resourceId", "esunny.test:id/nav_item_favorite")
    switch2quote = ("resourceId", "esunny.test:id/nav_item_quote")
    switch2trade = ("resourceId", "esunny.test:id/nav_item_trade")
    switch2news = ("resourceId", "esunny.test:id/nav_item_news")

    def __init__(self):
        super().__init__()

    def goToRightToolBar(self):
        self.click(self.menu_button)

    def getCurTitle(self):
        return self.get_text(self.title)

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
