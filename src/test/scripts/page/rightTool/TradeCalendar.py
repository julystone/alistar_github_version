from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.rightTool.RightToolBar import RightToolBar


class TradeCalendar(Page, Driver):
    # title
    title = ('text', '交易日历')

    # 详细信息
    month = ('resourceId', "esunny.test:id/activity_es_trade_calendar_tv_month")
    year = ('resourceId', "esunny.test:id/activity_es_trade_calendar_tv_year")
    calendar_month = ('resourceId', "esunny.test:id/vp_month")
    calendar_week = ('resourceId', "esunny.test:id/vp_week")

    def __init__(self):
        super().__init__()
        if not self.check_element_exist(self.title):
            RightToolBar().goToCommonSetting()
        assert self.get_text(self.title) == '交易日历'

    def getCurMonth(self):
        return self.get_text(self.month)

    def getCurYear(self):
        return self.get_text(self.year)

    def swipeCalendar(self):
        if self.check_element_exist(self.calendar_month):
            self.swipe('up')
        else:
            self.swipe('down')


if __name__ == '__main__':
    debugPage = TradeCalendar()
    res = debugPage.getCurMonth()
    print(res)
    debugPage.swipeCalendar()
    # AP.goToUploadPage()
