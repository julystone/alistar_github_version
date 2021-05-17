from assertpy import assert_that

from src.test.scripts.page.setting.SettingBasePage import SettingBasePage


class QuoteSetting(SettingBasePage):
    # title
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

    def selfCheck(self):
        assert_that(self.check_element_exist(self.deep_red_green)).is_true()

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

    def selfCheck(self):
        assert_that(self.check_element_exist(self.settleBand)).is_true()

    def getCurrentPriceCal(self):
        for loc in [self.settlePriceChoose, self.closePriceChoose, self.openPriceChoose]:
            elem = self.findElemWithoutException(loc)
            if elem:
                break
        return elem.sibling().info['text']


class IndexSetting(SettingBasePage):
    def selfCheck(self):
        assert_that(self.check_element_exist(('text', '量仓指标'))).is_true()

    def turnOnIndex(self, index_name):
        print(index_name)
        pass
        return self


class IndexParameterSetting(SettingBasePage):
    def selfCheck(self):
        assert_that(self.getCurTitle()).is_equal_to('指标参数修改')

    def fillInIndexNum(self, index_name, parameter_name, num):
        selector = self.clickText(index_name).findElement(('text', parameter_name))
        num_selector = selector.sibling()
        num_selector.set_text(num)


class DrawLineSetting(SettingBasePage):
    position_ave_line = ("resourceId", "esunny.test:id/es_activity_chart_setting_position_cost_switch_button")
    last_price_line = ("resourceId", "esunny.test:id/es_activity_chart_setting_last_price_switch_button")
    draw_line = ("resourceId", "esunny.test:id/es_activity_chart_setting_draw_line_switch_button")

    def selfCheck(self):
        assert_that(self.getCurTitle()).is_equal_to('图表画线设置')

    def switchPositionAveLine(self, expect):
        self.changeOneSwitch(self.position_ave_line, expect)

    def switchLastPriceLine(self, expect):
        self.changeOneSwitch(self.last_price_line, expect)

    def switchDrawLine(self, expect):
        self.changeOneSwitch(self.draw_line, expect)


class CommonPeriodSetting(SettingBasePage):
    title = ('text', '行情设置')
    quit_btn = ("resourceId", "esunny.test:id/es_activity_system_setting_iv_back")

    def selfCheck(self):
        assert_that(self.getCurTitle()).is_equal_to('常用周期设置')


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

    def selfCheck(self):
        assert_that(self.getCurTitle()).is_equal_to('行情列头设置')


class QuoteFontSize(SettingBasePage):
    def selfCheck(self):
        assert_that(self.getCurTitle()).is_equal_to('行情字体大小')


class CodeTableSetting(SettingBasePage):
    code_table_switch = ("resourceId", "esunny.test:id/es_activity_code_table_is_save_data_switch_button")
    code_table_address = ("resourceId", "esunny.test:id/es_activity_code_table_tv_quote_address")

    def selfCheck(self):
        assert_that(self.getCurTitle()).is_equal_to('码表设置')


if __name__ == '__main__':
    debugPage = PriceCalculateChoose()
    # debugPage.switchDeepGreenRed(False).switchOrderColumnDisplay(True)
    # print(debugPage.getCurQuoteFontSize())
    # print(debugPage.getCurPriceCalculate())
    debugPage.getDriver().sleep(2)
