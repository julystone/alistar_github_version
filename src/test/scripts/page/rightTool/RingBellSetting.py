from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver_atx import Driver


class RingBellSetting(Page, Driver):
    # title
    title = ('text', '价格预警音')

    # 详细信息
    bellList = ("resourceId", "esunny.test:id/es_activity_price_warning_rv")
    check = ("resourceId", "esunny.test:id/es_item_choose_default_price_tv_check")

    def __init__(self):
        super().__init__()
        self.selfCheck(self.bellList)

    def getCurrentBell(self):
        elem = self.findElemWithoutException(self.check)
        return elem.sibling().info['text']


if __name__ == '__main__':
    debugPage = RingBellSetting()
    res = debugPage.getCurrentBell()
    print(res)
    # debugPage.pageBack()
qq