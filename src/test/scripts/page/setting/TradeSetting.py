import time

from src.test.scripts.page.setting._SettingBasePage import SettingBasePage


class TradeSetting(SettingBasePage):
    title = ("resourceId", "esunny.test:id/toolbar_title")
    Default_price_type = ('resourceId', 'esunny.test:id/es_activity_trade_setting_tv_defaule_price')
    Backhand_Price_Type = ('resourceId', 'esunny.test:id/es_activity_trade_setting_tv_defaule_reverse_price')
    Drow_Price_Tyce = ('resourceId', 'esunny.test:id/es_activity_trade_setting_tv_defaule_drawline_price')
    Default_lot = ('text', '默认手数')
    Overpriced_points = ('text', '超价点数')
    Market_order_settings = ('text', '市价单设置')
    Stop_loss_parameter_settings = ('text', '止损参数设置')
    Big_single_split = ('resourceId', 'esunny.test:id/es_activity_trade_setting_switch_separete_order')

    title_text = '交易设置'

    def getDefaultPriceType(self):  # 获取当前默认价格类型
        return self.get_text(self.Default_price_type)

    def gotoDefaultPriceType(self):  # 跳转默认价格选择界面
        self.click(self.Default_price_type)
        return DefaultPriceType()

    def getBackhandPriceType(self):  # 获取当前反手价格类型
        return self.get_text(self.Backhand_Price_Type)

    def gotoBackhandPriceType(self):  # 跳转反手价选择界面
        self.click(self.Backhand_Price_Type)
        return BackhandPriceType()

    def getDrawPriceType(self):  # 获取画线下单配置
        return self.get_text(self.Drow_Price_Tyce)

    def gotoDrawPriceType(self):  # 跳转画线下单配置界面
        self.click(self.Drow_Price_Tyce)
        return DrawPriceType()

    def gotoDefaultLot(self):  # 跳转默认手数
        self.click(self.Default_lot)
        return DefaultLot()

    def gotoOverPricedPoints(self):  # 跳转超价点数
        self.click(self.Overpriced_points)
        return OverpricedPoints()

    def gotoMarketOrderSettings(self):  # 市价单设置
        self.click(self.Market_order_settings)
        return MarketOrderSettings()

    def gotoStoplossParameterSettings(self):  # 止损参数设置
        self.click(self.Stop_loss_parameter_settings)
        return StoplossParameterSettings()

    def getBigSingleSplitStatus(self):  # 大单拆分状态
        return self.findElemWithoutException(self.Big_single_split).info['checked']

    def BigSingleSplitOpen(self):  # 大单拆分开
        status = self.getBigSingleSplitStatus()
        if not status:
            self.click(self.Big_single_split)

    def BigSingleSplitClose(self):  # 大单拆分关
        status = self.getBigSingleSplitStatus()
        if status:
            self.click(self.Big_single_split)


class DefaultPriceType(SettingBasePage):  # 默认价格选择
    title_text = '默认价格'
    loc = ('resourceId', 'esunny.test:id/es_item_choose_default_price_tv_check')
    Latest_price = ('text', '最新价')
    Queuing_price = ('text', '排队价')
    market_price = ('text', '市价')
    Counterparty_price = ('text', '对手价')
    Latest_overpriced = ('text', '最新价超')
    Queuing_overprice = ('text', '排队价超')
    Counterparty_overprice = ('text', '对手价超')

    def getPriceType(self):  # 获取当前选中价格类型
        elem = self.findElemWithoutException(self.loc)
        return elem.sibling().info['text']

    def select_Latest_price(self):
        self.click(self.Latest_price)
        time.sleep(0.1)

    def select_Queuing_price(self):
        self.click(self.Queuing_price)
        time.sleep(0.1)

    def select_market_price(self):
        self.click(self.market_price)
        time.sleep(0.1)

    def select_Counterparty_price(self):
        self.click(self.Counterparty_price)
        time.sleep(0.1)

    def select_Latest_overpriced(self):
        self.click(self.Latest_overpriced)
        time.sleep(0.1)

    def select_Queuing_overprice(self):
        self.click(self.Queuing_overprice)
        time.sleep(0.1)

    def select_Counterparty_overprice(self):
        self.click(self.Counterparty_overprice)
        time.sleep(0.1)


class BackhandPriceType(SettingBasePage):  # 反手价格选择
    title_text = '反手价格'
    Latest_price = ('text', '最新价')
    Queuing_price = ('text', '排队价')
    market_price = ('text', '市价')
    Counterparty_price = ('text', '对手价')
    loc = ('resourceId', 'esunny.test:id/es_item_choose_default_price_tv_check')

    def getPriceType(self):  # 获取当前选中价格类型
        elem = self.findElemWithoutException(self.loc)
        return elem.sibling().info['text']

    def select_Latest_price(self):
        self.click(self.Latest_price)
        time.sleep(0.1)

    def select_Queuing_price(self):
        self.click(self.Queuing_price)
        time.sleep(0.1)

    def select_market_price(self):
        self.click(self.market_price)
        time.sleep(0.1)

    def select_Counterparty_price(self):
        self.click(self.Counterparty_price)
        time.sleep(0.1)


class DrawPriceType(SettingBasePage):
    title_text = '画线下单价格'
    Latest_price = ('text', '画线价(最新价)')
    Queuing_price = ('text', '排队价')
    market_price = ('text', '市价')
    Counterparty_price = ('text', '对手价')
    Over_price = ('text', '超价')
    loc = ('resourceId', 'esunny.test:id/es_item_choose_default_price_tv_check')

    def getPriceType(self):  # 获取当前选中价格类型
        elem = self.findElemWithoutException(self.loc)
        return elem.sibling().info['text']

    def select_Latest_price(self):
        self.click(self.Latest_price)
        time.sleep(0.1)

    def select_Queuing_price(self):
        self.click(self.Queuing_price)
        time.sleep(0.1)

    def select_market_price(self):
        self.click(self.market_price)
        time.sleep(0.1)

    def select_Counterparty_price(self):
        self.click(self.Counterparty_price)
        time.sleep(0.1)

    def select_Over_price(self):
        self.click(self.Over_price)
        time.sleep(0.1)


class DefaultLot(SettingBasePage):
    title_text = '默认手数'
    variety = '2'

    def getPriceType(self, exchange):  # 获取当前选中价格类型
        a = ('text', exchange)
        while True:
            elem = self.findElemWithoutException(a)
            if elem:
                break
            self.swipe(direction='up', box=(169, 771, 137, 1244))
        self.click(a)


class OverpricedPoints(SettingBasePage):
    pass


class MarketOrderSettings(SettingBasePage):
    title_text = '市价单设置'
    stop_order = ('resourceId', 'esunny.test:id/es_market_price_rl_stop_order_common')  # 禁止下单
    price_rl_down = ('resourceId', 'esunny.test:id/es_market_price_rl_price_up_down_order_common')  # 涨跌停下单
    stop_order_cffex = ('resourceId', 'esunny.test:id/es_market_price_rl_stop_order_CFFEX')  # 禁止下单-中金所
    price_rl_down_cffex = ('resourceId', 'esunny.test:id/es_market_price_rl_price_up_down_order_CFFEX')  # 涨跌停下单-中金所
    loc_other1 = ('resourceId', 'esunny.test:id/es_item_choose_stop_order_common_tv_check')
    loc_other2 = ('resourceId', 'esunny.test:id/es_item_choose_price_up_down_common_tv_check')
    loc_cffex1 = ('resourceId', 'esunny.test:id/es_item_choose_stop_order_CFFEX_tv_check')
    loc_cffex2 = ('resourceId', 'esunny.test:id/es_item_choose_price_up_down_CFFEX_tv_check')

    def getprice(self):
        for loc in [self.loc_other1, self.loc_other2]:
            elem = self.findElemWithoutException(loc)
            if elem:
                break
        return elem.sibling().info['text']

    def getpricecffex(self):
        for loc in [self.loc_cffex1, self.loc_cffex2]:
            elem = self.findElemWithoutException(loc)
            if elem:
                break
        return elem.sibling().info['text']

    def select_stop_order(self):
        self.click(self.stop_order)

    def select_price_rl_down(self):
        self.click(self.price_rl_down)

    def select_stop_order_cffex(self):
        self.click(self.stop_order_cffex)

    def select_price_rl_down_cffex(self):
        self.click(self.price_rl_down_cffex)


class StoplossParameterSettings(SettingBasePage):
    title_text = '止损参数设置'
    stop_loss_auto_switch = ('resourceId', 'esunny.test:id/es_activity_stop_loss_auto_switch')  # 开仓自动止盈止损
    default_strategy = ('resourceId', 'esunny.test:id/es_activity_stop_loss_tv_default_strategy')  # 默认策略
    default_order_price = ('text', '默认委托价格')
    base_price = ('resourceId', 'esunny.test:id/es_activity_stop_loss_tv_benchmark_price')  # 基准价
    spread_parameters = ('text', '默认止损点差参数')

    def getSwitchStatus(self):  # 获取开关状态
        return self.findElemWithoutException(self.stop_loss_auto_switch).info['checked']

    def switch_open(self):
        status = self.getSwitchStatus()
        if status:
            pass
        else:
            self.click(self.stop_loss_auto_switch)

    def switch_close(self):
        status = self.getSwitchStatus()
        if status:
            self.click(self.stop_loss_auto_switch)
        else:
            pass

    def getDefaultStrategy(self):  # 获取默认策略
        return self.get_text(self.default_strategy)

    def gotoDefaultStrategy(self):  # 跳转默认策略
        self.click(self.default_strategy)
        return self.DefaultStrategy()

    def gotoDefaultOrderPrice(self):  # 跳转默认委托价格
        self.click(self.default_order_price)
        return self.DefaultOrderPrice()

    def getBasePrcie(self):  # 获取基准价
        return self.get_text(self.base_price)

    def gotoBasePrcie(self):  # 跳转基准价
        self.click(self.base_price)
        return self.BasePrcie()

    class DefaultStrategy(SettingBasePage):
        title_text = '默认策略'
        loc_stop_loss_profit = ('resourceId', 'esunny.test:id/es_item_choose_stop_both_tv_check')
        loc_stop_loss = ('resourceId', 'esunny.test:id/es_item_choose_stop_lose_tv_check')
        loc_stop_profit = ('resourceId', 'esunny.test:id/es_item_choose_stop_surplus_tv_check')
        loc_Dynamic_tracking = ('resourceId', 'esunny.test:id/es_item_choose_dynamic_tracking_tv_check')
        stop_loss_profit = ('text', '限价止损+限价止盈')
        stop_loss = ('text', '限价止损')
        stop_profit = ('text', '限价止盈')
        Dynamic_tracking = ('text', '动态追踪')

        def getStrategy(self):
            for loc in [self.loc_stop_loss_profit, self.loc_stop_loss, self.loc_stop_profit, self.loc_Dynamic_tracking]:
                elem = self.findElemWithoutException(loc)
                if elem:
                    break
            return elem.sibling().info['text']

        def selectStopLossProfit(self):
            self.click(self.stop_loss_profit)

        def selectStopLoss(self):
            self.click(self.stop_loss)

        def selectStopProfit(self):
            self.click(self.stop_profit)

        def selectDynamicTracking(self):
            self.click(self.Dynamic_tracking)

    class DefaultOrderPrice(SettingBasePage):
        title_text = '默认委托价格'
        pass

    class BasePrcie(SettingBasePage):
        title_text = '基准价'
        loc_order_price = ('resourceId', 'esunny.test:id/es_item_choose_order_price_tv_check')
        loc_counter_price = ('resourceId', 'esunny.test:id/es_item_choose_counter_price_tv_check')
        loc_last_price = ('resourceId', 'esunny.test:id/es_item_choose_last_price_tv_check')
        order_price = ('text', '委托价')
        counter_price = ('text', '委托时的对手价')
        last_price = ('text', '委托时的最新价')

        def getPresentBasePrice(self):
            for loc in [self.loc_counter_price, self.loc_last_price, self.loc_order_price]:
                elem = self.findElemWithoutException(loc)
                if elem:
                    break
            return elem.sibling().info['text']

        def selectOrderPrice(self):
            self.click(self.order_price)

        def selectCounterPrice(self):
            self.click(self.counter_price)

        def selectLastPrice(self):
            self.click(self.last_price)

    class SpreadParameters(SettingBasePage):
        title_text = '默认止损点差参数'
        pass


if __name__ == '__main__':
    # d1=TradeSetting().getBigSingleSplitStatus()
    # d2=TradeSetting().BigSingleSplitOpen()
    # d3 = TradeSetting().getBigSingleSplitStatus()
    b = DefaultLot().getPriceType('欧洲ICEU')

    print(b)
