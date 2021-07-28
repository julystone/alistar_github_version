from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.page.singleQuote._SingleQuoteBasePage import SingleQuoteBasePage


class NewsPage(SingleQuoteBasePage):
    # F10
    f10 = ("resourceId", "esunny.estarandroid:id/es_kline_toolbar_right_third")

    # 校验项
    block_choose = '资讯'

    def goToF10Page(self):
        self.click(self.f10)
        return F10Page()

    def drawLineMode(self, into: bool):
        print("NewsPage Can't Enhance DrawLineMode")
        return self

    def thudTradeMode(self, into: bool):
        return self.goToF10Page()


class F10Page(NewsPage):
    quit_btn = ("resourceId", "esunny.estarandroid:id/es_activity_f10_back")
    title = ("text", "F10")

    # 校验项
    title_text = 'F10'

    def selfCheck(self):
        Asserter.PageHasElem(self, self.title)
