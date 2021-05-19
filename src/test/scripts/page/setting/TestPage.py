from src.test.scripts.framework.BasePage import BasePage
from src.test.scripts.framework.Driver_atx import Driver


class TradeCalendar(BasePage, Driver):
    # title
    title = ('text', '交易日历')

    # 详细信息
    month = ('text', 'MA')
    year = ('text', 'EMA')
    calendar_month = ('resourceId', "esunny.test:id/vp_month")
    calendar_week = ('resourceId', "esunny.test:id/vp_week")

    def selfCheck(self):
        pass

    def getCurMonth(self):
        res = self.findElement(self.month)
        print(res)
        res1 = self.findElement(self.year)
        print(res1)

    def getCurYear(self):
        return self.get_text(self.year)

    def swipeCalendar(self):
        if self.check_element_exist(self.calendar_month):
            self.swipe('up')
        else:
            self.swipe('down')
        return self


if __name__ == '__main__':
    debugPage = TradeCalendar()
    res = debugPage.getCurMonth()
    print(res)
    # AP.goToUploadPage()
