import allure

from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.page.interface.Keyboard import LotsKeyBoard, PriceKeyBoard
from src.test.scripts.page.interface._Interface import Interface

"""
封装快买快卖
"""


class ThudTradeMode(Interface):
    quit_btn = ("resourceId", "esunny.estarandroid:id/es_kline_toolbar_left")

    # 底部栏
    thud_trade_lots = ("resourceId", "esunny.estarandroid:id/es_kline_qty_text")
    thud_trade_price = ("resourceId", "esunny.estarandroid:id/es_kline_price_text")
    thud_trade_buy = ("resourceId", "esunny.estarandroid:id/es_kline_buy_button")
    thud_trade_sell = ("resourceId", "esunny.estarandroid:id/es_kline_sell_button")
    thud_trade_cover = ("resourceId", "esunny.estarandroid:id/es_kline_cover_button")

    def selfCheck(self):
        Asserter.PageHasElem(self, self.thud_trade_lots)

    @allure.step("设置手数")
    def setLots(self, lots=1):
        print(f"设置手数 {lots}")
        my_log.info(f"设置手数 {lots}")
        self.click(self.thud_trade_lots)
        LotsKeyBoard().lotsInput(lots)
        return self

    @allure.step("设置价格")
    def setPrice(self, price='对手价'):
        print(f"设置价格 {price}")
        my_log.info(f"设置价格 {price}")
        self.click(self.thud_trade_price)
        PriceKeyBoard().priceInput(price)
        return self

    @allure.step("点击 买")
    def clickBuy(self):
        print("点击 买")
        my_log.info("点击 买")
        self.click(self.thud_trade_buy)
        return self

    @allure.step("点击 卖")
    def clickSell(self):
        print("点击 卖")
        my_log.info("点击 卖")
        self.click(self.thud_trade_sell)
        return self

    @allure.step("退出模式")
    def quitMode(self):
        # self.add_watcher("退出模式", "是否要退出快买快卖？", "确定")
        self.click(self.quit_btn)
        if self.findElemViaText("确定"):
            self.clickText("确定")


if __name__ == '__main__':
    debugPage = ThudTradeMode()
    debugPage.quitMode()
