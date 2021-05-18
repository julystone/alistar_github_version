from src.test.scripts.page.setting.RightToolBar import RightToolBar
from src.test.scripts.page.setting.SettingBasePage import SettingBasePage


class TradeCalendar(SettingBasePage):
    # 详细信息
    month = ('resourceId', "esunny.test:id/activity_es_trade_calendar_tv_month")
    year = ('resourceId', "esunny.test:id/activity_es_trade_calendar_tv_year")
    calendar_month = ('resourceId', "esunny.test:id/vp_month")
    calendar_week = ('resourceId', "esunny.test:id/vp_week")
    # 校验项
    title_text = "交易日历"

    def getCurMonth(self):
        return self.get_text(self.month)

    def getCurYear(self):
        return self.get_text(self.year)

    def swipeCalendar(self):
        if self.check_element_exist(self.calendar_month):
            self.swipe('up')
        else:
            self.swipe('down')
        return self


if __name__ == '__main__':
    RightToolBar().goToCalendar()
    debugPage = TradeCalendar()
    res = debugPage.getCurMonth()
    print(res)
    debugPage.swipeCalendar()
    # AP.goToUploadPage()
