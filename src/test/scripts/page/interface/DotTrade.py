import allure

from src.test.scripts.framework import Asserter
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.page.navigate.TradePage import TradePage
from src.test.scripts.page.rightToolBar._SettingBasePage import SettingBasePage


class DotTrade(SettingBasePage):
    # 顶部栏

    # 合约选择、手数选择、连续开仓勾选
    contract_select = ("resourceId", 'esunny.test:id/et_trade_click_order_contract')
    lots_select = ("resourceId", 'esunny.test:id/et_trade_click_order_lots')
    continue_open = ("resourceId", 'esunny.test:id/icon_trade_click_order_constant_open')

    # 买全撤
    cancel_buy_all = ("resourceId", 'esunny.test:id/tv_es_trade_click_order_cancel_buy')
    # 卖全撤
    cancel_sell_all = ("resourceId", 'esunny.test:id/tv_es_trade_click_order_cancel_sell')
    # 买3挂单价买
    buy_wait = {'x': 300 / 1080, 'y': 2000 / 2201}
    # 卖1对手价买
    sell_match = {'x': 300 / 1080, 'y': 1140 / 2201}
    # 卖3挂单价卖
    sell_wait = {'x': 785 / 1080, 'y': 1140 / 2201}
    # 买1对手价卖
    buy_match = {'x': 785 / 1080, 'y': 2000 / 2201}

    @staticmethod
    @allure.step("调用右边栏接口，进入登录页面")
    def makeAPage():
        tp = TradePage.makeAPage()
        Driver.click(tp.dot_trade)
        Asserter.shouldTextEqual(DotTrade.title, '点价下单')
        return DotTrade()

    @allure.step("选择合约")
    def setContract(self, contract):
        print(f"选择{contract}合约")
        my_log.info(f"选择{contract}合约")
        Driver.click(self.contract_select)
        locator = ('part-text', contract)
        Driver.click(locator)
        return self

    @allure.step("点价下单")
    def dotTrade(self, direction, condition):
        """
        点价下单
        :param direction: buy/sell      买/卖
        :param condition: wait/match    排位/对价成交
        :return:    self
        """
        if direction not in ['buy', 'sell'] and condition not in ['wait', 'match']:
            raise KeyError
        locator = f'{direction}_{condition}'
        Driver.click(getattr(self, locator))
        return self


if __name__ == '__main__':
    Driver.driverInit(1)
    dot = DotTrade.makeAPage()
    dot.setContract('棉花105').\
        dotTrade('buy', 'wait')
    input("点击继续")
    Driver.quit()

