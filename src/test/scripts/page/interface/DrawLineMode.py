import allure

from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.page.interface.Keyboard import LotsKeyBoard
from src.test.scripts.page.interface._Interface import Interface

"""
封装画线下单
"""


class DrawLineMode(Interface):
    quit_btn = ("resourceId", "esunny.estarandroid:id/es_kline_toolbar_left")

    # 底部栏
    draw_line_bar = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_menu_bar")
    draw_line_buy = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_buy_button")
    draw_line_sell = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_sell_button")
    draw_line_cover_long = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_long_button")
    draw_line_cover_short = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_short_button")
    draw_line_lots = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_lots_tv")
    draw_line_confirm = ("resourceId", "esunny.estarandroid:id/es_kline_draw_line_confirm_button")

    def selfCheck(self):
        Asserter.PageHasElem(self, self.draw_line_bar)

    @allure.step("设置手数 {lots}")
    def setLots(self, lots=1):
        self.click(self.draw_line_lots)
        LotsKeyBoard().lotsInput(lots)
        return self

    @allure.step("点击 买")
    def clickBuy(self):
        self.click(self.draw_line_buy)
        return self

    @allure.step("点击 卖")
    def clickSell(self):
        self.click(self.draw_line_sell)
        return self

    @allure.step("点击 确定")
    def clickConfirm(self):
        self.click(self.draw_line_confirm)
        if self.findElemViaText("确定"):
            self.clickText("确定")
        return self

    @allure.step("退出模式")
    def quitMode(self):
        self.click(self.quit_btn)
        if self.findElemViaText("确定"):
            self.clickText("确定")


if __name__ == '__main__':
    debugPage = DrawLineMode()
    debugPage.setLots(12).clickConfirm()
