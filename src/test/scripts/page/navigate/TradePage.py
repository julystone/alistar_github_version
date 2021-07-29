import allure

from _NavigateBasePage import NavigateBasePage
from src.test.scripts.page.interface.Keyboard import LotsKeyBoard
from src.test.scripts.page.interface.Keyboard import PriceKeyBoard


class TradePage(NavigateBasePage):
    # TODO 交易界面需要大改
    # 顶部栏标题、点价、跳转K线
    dot_trade = ("resourceId", 'esunny.test:id/toolbar_left_first')
    go_quote = ("resourceId", 'esunny.test:id/toolbar_left_second')

    # 合约选择、手数、价格、买、卖
    contract_select = ("resourceId", 'esunny.test:id/et_trade_contract')
    lots_select = ("resourceId", 'esunny.test:id/et_trade_lots')
    price_select = ("resourceId", 'esunny.test:id/et_trade_price')
    buy_button = ("resourceId", 'esunny.test:id/tradeBtnPrimal_buy')
    sell_button = ("resourceId", 'esunny.test:id/tradeBtnPrimal_sell')

    # 持仓、挂单、委托、成交页签
    tag_pos = ("resourceId", 'esunny.test:id/textView_trade_position')
    tag_ask = ("resourceId", 'esunny.test:id/textView_trade_parorder')
    tag_order = ("resourceId", 'esunny.test:id/textView_trade_order')
    tag_match = ("resourceId", 'esunny.test:id/textView_trade_match')

    # 委托列表
    order_list = ("resourceId", 'esunny.test:id/recyclerview_trade_order')
    # 成交列表
    match_list = ("resourceId", 'esunny.test:id/recyclerview_trade_match')

    # 校验项
    block_choose = "交易"

    @allure.step("选择合约")
    def setContract(self, contract):
        loc = ('part-text', contract)
        self.click(self.contract_select).click(loc)
        return self

    @allure.step("设置手数")
    def setLots(self, lots=1):
        self.click(self.lots_select)
        LotsKeyBoard().lotsInput(lots)
        return self

    @allure.step("设置价格")
    def setPrice(self, price='对手价'):
        self.click(self.price_select)
        PriceKeyBoard().priceInput(price)
        return self

    @allure.step("点击 买")
    def clickBuy(self):
        self.click(self.buy_button)
        return self

    @allure.step("点击 卖")
    def clickSell(self):
        self.click(self.sell_button)
        return self

    @allure.step("检查委托列表")
    def checkMatchList(self):
        # 查看成交列表第一条是否有
        first_match_temp = self.find_elements(self.match_list)[1]
        first_match = self.find_elements(first_match_temp)[1]
        first_match_2 = self.find_elements(first_match)
        for elem in first_match_2:
            print(self.get_text(elem))
        # first_order = Driver.find_elements(self.order_list)[1][1]
        # Asserter.shouldElemExist(first_order, first_match)


if __name__ == '__main__':
    debugPage = TradePage()
    debugPage.setContract('红枣').setPrice('233').setLots(233).clickBuy()
# android.widget.TextView - esunny.test:id/order_list_tv_contract_no
