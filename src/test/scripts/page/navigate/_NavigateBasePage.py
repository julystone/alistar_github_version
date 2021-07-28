from src.test.scripts.page.BasePage.BasePageWithBottom import BasePageWithBottom


class NavigateBasePage(BasePageWithBottom):
    # 顶部栏
    title = ("resourceId", "esunny.test:id/toolbar_title")
    right_tool = ('xpath', '//*[@resource-id="esunny.test:id/toolbar_right_icons"]/android.widget.FrameLayout[1]')

    # 底部导航
    switch2fav = {"resourceId": "esunny.estarandroid:id/nav_tv_title", "text": "自选"}
    switch2quote = {"resourceId": "esunny.estarandroid:id/nav_tv_title", "text": "行情"}
    switch2trade = {"resourceId": "esunny.estarandroid:id/nav_tv_title", "text": "交易"}
    switch2news = {"resourceId": "esunny.estarandroid:id/nav_tv_title", "text": "资讯"}
    # switch2fav = ("text", "自选")
    # switch2quote = ("text", "行情")
    # switch2trade = ("text", "交易")
    # switch2news = ("text", "资讯")

    annal_list = [switch2fav, switch2quote, switch2trade, switch2news]

    def selfCheck(self):
        super().selfCheck()

    def getCurTitle(self):
        return self.get_text(self.title)

    def goToRightToolBar(self):
        self.wait_element(self.right_tool, 20)
        self.click(self.right_tool)
        from src.test.scripts.page.interface.RightToolBar import RightToolBar
        return RightToolBar()

    def goToFavPage(self):
        self.click(self.switch2fav)
        from src.test.scripts.page.navigate.FavPage import FavPage
        return FavPage()

    def goToQuotePage(self):
        self.click(self.switch2quote)
        from src.test.scripts.page.navigate.QuotePage import QuotePage
        return QuotePage()

    def goToTradePage(self):
        self.click(self.switch2trade)
        from src.test.scripts.page.navigate.TradePage import TradePage
        return TradePage()

    def goToNewsPage(self):
        self.click(self.switch2news)
        from src.test.scripts.page.navigate.NewsPage import NewsPage
        return NewsPage()


if __name__ == '__main__':
    debugPage = NavigateBasePage()
    res = debugPage.goToFavPage()
