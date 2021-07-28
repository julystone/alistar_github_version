from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.page.singleQuote._SingleQuoteBasePage import SingleQuoteBasePage


class PanelPage(SingleQuoteBasePage):
    # 盘口、成交明细切换页签
    pankou = ("resourceId", "esunny.estarandroid:id/es_kline_pannel_view_tv_match_detail")
    minxi = ("resourceId", "esunny.estarandroid:id/es_kline_pannel_view_tv_quote")
    # 校验项
    block_choose = '盘口'

    def drawLineMode(self, into: bool):
        print("PanelPage Can't Enhance DrawLineMode")
        return self

    def goToMinxi(self):
        if self.getCurItemStatus(self.minxi) is False:
            self.click(self.minxi)
        return MinxiPage()

    def goToPankou(self):
        if self.getCurItemStatus(self.pankou) is False:
            self.click(self.pankou)
        return PankouPage()


class MinxiPage(PanelPage):
    def selfCheck(self):
        super().selfCheck()
        Asserter.BoolTrue(self.getCurItemStatus(self.minxi))


class PankouPage(PanelPage):
    def selfCheck(self):
        super().selfCheck()
        Asserter.BoolTrue(self.getCurItemStatus(self.pankou))
