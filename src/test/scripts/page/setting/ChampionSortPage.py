from src.test.scripts.page.setting._SettingBasePage import SettingBasePage


class ChampionSort(SettingBasePage):
    # 成交持仓页面
    match_title = ("resourceId", "esunny.test:id/es_activity_champion_tv_match_position")
    exchange_choose = ("resourceId", "esunny.test:id/es_activity_champion_tv_exchange")
    commodity_choose = ("resourceId", "esunny.test:id/es_activity_champion_tv_commodity")
    contract_choose = ("resourceId", "esunny.test:id/es_activity_tv_contract_or_company")
    date_choose = ("resourceId", "esunny.test:id/es_activity_champion_tv_date")
    pie_chart = ("resourceId", "esunny.test:id/es_champion_cakesurfaceview")
    trend_icon = ("resourceId", "esunny.test:id/es_item_champion_pic")
    wait_bar = ("resourceId", "esunny.test:id/progress_bar")

    # 持仓结构页面
    position_title = ("resourceId", "esunny.test:id/es_activity_champion_tv_position_struct")

    version = ('resource-id', "esunny.test:id/activity_es_about_tv_version_value")
    upload = ('resource-id', "esunny.test:id/activity_es_about_rl_daily")
    feedback = ('resource-id', "esunny.test:id/activity_es_about_rl_feedback")
    privacy = ('resource-id', "esunny.test:id/activity_es_about_rl_privacy")
    # 校验项
    title_text = "成交持仓"

    def selfCheck(self):
        assert self.check_element_exist(self.match_title)

    def getCurChosenTitle(self):
        title1 = self.findElemWithoutException(self.match_title)
        title2 = self.findElemWithoutException(self.position_title)
        if self.getCurItemStatus(title1):
            return title1.get_text()
        elif self.getCurItemStatus(title2):
            return title2.get_text()

    def getCurExchange(self):
        return self.get_text(self.exchange_choose)

    def getCurCommodity(self):
        return self.get_text(self.commodity_choose)

    def getCurContract(self):
        return self.get_text(self.contract_choose)

    def getCurDate(self):
        return self.get_text(self.date_choose)

    def changeMeta(self, chooseLoc, text):
        self.click(chooseLoc)
        self.clickText(text)
        return self

    def changeExchange(self, exchangeName):
        return self.changeMeta(self.exchange_choose, exchangeName)

    def changeCommodity(self, commodityName):
        return self.changeMeta(self.commodity_choose, commodityName)

    def changeContract(self, contractName):
        return self.changeMeta(self.contract_choose, contractName)

    def changeDate(self, date):
        return self.changeMeta(self.date_choose, date)

    def goToTrendPage(self):
        self.click(self.trend_icon)
        return self.TrendPage()

    class TrendPage(SettingBasePage):
        title_text = '走势图'
        week_trend = ("resourceId", "esunny.test:id/es_benefit_day_tv_one_week")
        month_trend = ("resourceId", "esunny.test:id/es_benefit_day_tv_two_week")
        three_month_trend = ("resourceId", "esunny.test:id/es_benefit_day_tv_custom")

        def getCurTrend(self):
            for loc in [self.week_trend, self.month_trend, self.three_month_trend]:
                if self.getCurItemStatus(loc):
                    break
            return self.findElemWithoutException(loc).get_text()


if __name__ == '__main__':
    debugPage = ChampionSort()
    res = debugPage.goToTrendPage().getCurTrend()
    print(res)
