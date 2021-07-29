from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.page.navigate._NavigateBasePage import NavigateBasePage


class OptionPage(NavigateBasePage):
    # 标题处
    exchange_switch_btn = ("resourceId", "esunny.estarandroid:id/toolbar_left_first")
    TL_change_btn = ("resourceId", "esunny.estarandroid:id/toolbar_left_second")
    strategy_trade = ("resourceId", "esunny.estarandroid:id/toolbar_right_second")
    # 标的物栏
    contractName = ("resourceId", "esunny.estarandroid:id/es_tv_option_bet_contractName")
    due_date = ("resourceId", "esunny.estarandroid:id/es_tv_option_bet_sreies_date")
    left_days = ("resourceId", "esunny.estarandroid:id/es_tv_option_bet_sreies_date_still")
    jump_quote = ("resourceId", "esunny.estarandroid:id/es_itv_jump")
    # 主体
    sort_btn = ("resourceId", "esunny.estarandroid:id/es_t_option_itv_sort")
    # 校验项
    block_choose = '期权'

    def getContractName(self):
        return self.get_text(self.contractName)

    def getDueDate(self):
        return self.get_text(self.due_date)

    def changeExchange(self, exchangeName):
        exchangeName = exchangeName.upper()
        loc = ('textContains', exchangeName)
        self.click(self.exchange_switch_btn) \
            .swipe_until_loc(loc) \
            .click(loc)
        Asserter.TextContainsText(self.getCurTitle(), exchangeName)
        return self

    def goToStrategyTrade(self):
        self.click(self.strategy_trade)
        return self.StrategyTradePage()

    class StrategyTradePage(NavigateBasePage):
        scroll_bar = ("resourceId", "esunny.estarandroid:id/es_rv_quote_commodity_select")
        # 校验项
        title_text = '主力排名'

        def switchToColumn(self, column):
            locator = ('text', column)
            self.swipe_until_loc(locator, self.scroll_bar, 'horizon')
            self.click(locator)


if __name__ == '__main__':
    debugPage = OptionPage()
    print(debugPage.getContractName())
