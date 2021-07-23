from assertpy import assert_that

from src.test.scripts.page.interface.Keyboard import LotsKeyBoard
from src.test.scripts.page.setting.SettingBasePage import SettingBasePage


class QuoteSetting(SettingBasePage):
    title = ('text', '行情设置')
    quit_btn = ("resourceId", "esunny.test:id/es_activity_system_setting_iv_back")
    # K线分时相关
    price_calculate = ("resourceId", "esunny.test:id/es_activity_chart_setting_tv_price_calculate")
    index_setting = ("resourceId", "esunny.test:id/es_activity_chart_setting_rl_parameter_configure")
    index_parameter_setting = ("resourceId", "esunny.test:id/es_activity_chart_setting_rl_parameter_change")
    draw_line_setting = ("resourceId", "esunny.test:id/es_activity_chart_setting_rl_char_draw_setting")
    common_period_setting = ("resourceId", "esunny.test:id/es_activity_chart_setting_rl_period_setting")
    # 盘口相关
    deep_red_green = ("resourceId", "esunny.test:id/es_activity_chart_setting_kline_color_switch_button")
    order_column_display = ("resourceId", "esunny.test:id/es_activity_chart_setting_position_show_switch_button")
    # 行情列表相关
    exchange_choose = ("resourceId", "esunny.test:id/es_activity_chart_setting_rl_quote_setting")
    title_choose = ("resourceId", "esunny.test:id/es_activity_chart_setting_rl_single_double_title_setting")
    quote_font_size = ("resourceId", "esunny.test:id/es_activity_chart_setting_tv_text_size")
    # 其他
    code_table_setting = ("resourceId", "esunny.test:id/es_activity_chart_setting_rl_code_table")
    # 校验项
    title_text = "行情设置"

    def getCurPriceCalculate(self):
        return self.get_text(self.price_calculate)

    def goToPriceCalculateChoose(self):
        self.click(self.price_calculate)
        return PriceCalculateChoose()

    def goToIndexSetting(self):
        self.click(self.index_setting)
        return IndexSetting()

    def goToIndexParameterSetting(self):
        self.click(self.index_parameter_setting)
        return IndexParameterSetting()

    def goToDrawLineSetting(self):
        self.click(self.draw_line_setting)
        return DrawLineSetting()

    def goToCommonPeriodSetting(self):
        self.click(self.common_period_setting)
        return CommonPeriodSetting()

    def switchDeepGreenRed(self, expect):
        self.changeOneSwitch(self.deep_red_green, expect)
        return self

    def switchOrderColumnDisplay(self, expect):
        self.changeOneSwitch(self.order_column_display, expect)
        return self

    def goToExchangeChoose(self):
        self.click(self.exchange_choose)
        return ExchangeChoose()

    def goToTitleChoose(self):
        self.click(self.title_choose)
        return TitleChoose()

    def goToQuoteFontSize(self):
        self.click(self.quote_font_size)
        return QuoteFontSize()

    def getCurQuoteFontSize(self):
        return self.get_text(self.quote_font_size)

    def goToCodeTableSetting(self):
        self.click(self.code_table_setting)
        return CodeTableSetting()


class PriceCalculateChoose(SettingBasePage):
    settleBand = ("resourceId", "esunny.test:id/es_activity_price_calculate_settle")
    settlePriceChoose = ("resourceId", "esunny.test:id/es_activity_etv_price_calculate_pre_settle_price")
    closePriceChoose = ("resourceId", "esunny.test:id/es_activity_etv_price_calculate_pre_closing_price")
    openPriceChoose = ("resourceId", "esunny.test:id/es_activity_etv_price_calculate_open_price")
    zuojiesuan = ("resourceId", "esunny.test:id/es_activity_price_calculate_settle")
    zuoshoupan = ("resourceId", "esunny.test:id/es_activity_price_calculate_closing")
    jinkaipan = ("resourceId", "esunny.test:id/es_activity_price_calculate_open")

    # 校验项
    title_text = "涨跌计算方式"

    def getCurrentPriceCal(self):
        # 获取勾的位置
        for loc in [self.settlePriceChoose, self.closePriceChoose, self.openPriceChoose]:
            elem = self.findElemWithoutException(loc)
            if elem:
                break
        return elem.sibling().info['text']

    def chooseWay(self, pricetypes):
        # 选择涨跌方式
        if pricetypes in '昨结算':
            self.click(self.zuojiesuan)
        elif pricetypes in '昨收盘':
            self.click(self.zuoshoupan)
        else:
            self.click(self.jinkaipan)
        return self


class IndexSetting(SettingBasePage):
    # 校验项
    title_text = "指标配置"

    def turnOnIndex(self, index_name):
        print(index_name)
        pass
        return self


class IndexParameterSetting(SettingBasePage):
    # 校验项
    title_text = "指标参数修改"

    def fillInIndexNum(self, index_name, parameter_name, num):
        selector = self.clickText(index_name).findElement(('text', parameter_name))
        num_selector = selector.sibling().info['text']
        num_selector.click()
        LotsKeyBoard().lotsInput(num)
        self.swipe()


class DrawLineSetting(SettingBasePage):
    position_ave_line = ("resourceId", "esunny.test:id/es_activity_chart_setting_position_cost_switch_button")
    last_price_line = ("resourceId", "esunny.test:id/es_activity_chart_setting_last_price_switch_button")
    draw_line = ("resourceId", "esunny.test:id/es_activity_chart_setting_draw_line_switch_button")

    # 校验项
    title_text = "图表画线设置"

    def switchOperate(self, line_style: object, expect):
        # 开启/关闭对应开关
        if line_style == '持仓均价线':
            self.changeOneSwitch(self.position_ave_line, expect)
        elif line_style == "最新价线":
            self.changeOneSwitch(self.last_price_line, expect)
        elif line_style == "画线下单线":
            self.changeOneSwitch(self.draw_line, expect)

    # def switchPositionAveLine(self, expect):
    #     self.changeOneSwitch(self.position_ave_line, expect)
    #
    # def switchLastPriceLine(self, expect):
    #     self.changeOneSwitch(self.last_price_line, expect)
    #
    # def switchDrawLine(self, expect):
    #     self.changeOneSwitch(self.draw_line, expect)


class CommonPeriodSetting(SettingBasePage):
    title = ('text', '常用周期设置')
    quit_btn = ("resourceId", "esunny.test:id/es_activity_system_setting_iv_back")  # 返回图标
    add_commonperiods = ("resourceId", "esunny.test:id/es_activity_period_setting_tv_add")  # 添加常用周期
    cancle_selection = ("resourceId", "esunny.test:id/es_period_picker_tv_cancel")  # 添加弹窗取消按钮
    confirm_selection = ("resourceId", "esunny.test:id/tv_es_period_keyboard_confirm")  # 添加弹窗确定按钮
    cancle_check = ("resourceId", "esunny.test:id/es_activity_period_setting_tv_cancel")  # 勾选取消按钮
    delete_check = ("resourceId", "esunny.test:id/es_activity_period_setting_tv_delete")  # 删除勾选
    resetting_button = ("resourceId", "esunny.test:id/es_activity_period_setting_tv_reset")  # 重置按钮
    oneminite_line = ("text", "1分钟")  # 1分钟线
    # 校验项
    title_text = "常用周期设置"

    def checkPeriod(self):
        # 检测周期勾选状态
        # elem_text = self.findElemWithoutException(self.oneminite_line).sibling().info['text']
        elem_text = self.findElemWithoutException(self.oneminite_line)
        if elem_text == '\ue617':
            self.clickText('1分钟')
        elif elem_text == '\ue61c':
            self.clickText('1分钟')

    def deletePeriod(self):
        # 删除常用周期
        self.clickText('1分钟')
        self.click(self.delete_check)

    def addCommonPeriod(self):
        # 点击添加常用周期按钮
        self.click(self.add_commonperiods)
        self.click(self.confirm_selection)

    def resettingFunction(self):
        # 重置
        self.click(self.resetting_button)


class ExchangeChoose(SettingBasePage):
    def selfCheck(self):
        assert_that(self.getCurTitle()).is_equal_to('行情板块设置')

    def getBlockStatus(self, block_name):
        return self.getCurItemStatus(('text', block_name))

    def setBlockStatus(self, block_name, expect):
        if self.getBlockStatus(block_name) != expect:
            self.clickText(block_name)


class TitleChoose(SettingBasePage):
    is_single_line = ('resourceId', "esunny.test:id/es_activity_quote_title_setting_switch_is_show_single")
    # 校验项
    title_text = "行情列头设置"


class QuoteFontSize(SettingBasePage):
    # 校验项
    title_text = "行情字体大小"


class CodeTableSetting(SettingBasePage):
    code_table_switch = ("resourceId", "esunny.test:id/es_activity_code_table_is_save_data_switch_button")
    code_table_address = ("resourceId", "esunny.test:id/es_activity_code_table_tv_quote_address")
    # 校验项
    title_text = "码表设置"


if __name__ == '__main__':
    # debugPage = PriceCalculateChoose()
    debugPage = CommonPeriodSetting()
    # debugPage.getCurrentPriceCal()
    # res = debugPage.checkPeriod()

    res = debugPage.checkPeriod()
    # res = debugPage.resettingFunction()
    # print(res.info)
    # debugPage.switchDeepGreenRed(False).switchOrderColumnDisplay(True)
    # print(debugPage.getCurQuoteFontSize())
    # print(debugPage.getCurPriceCalculate())
    # debugPage.chooseway("昨收盘")
