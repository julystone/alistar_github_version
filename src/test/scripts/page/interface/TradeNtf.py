from src.test.scripts.framework.Driver_atx import Driver

"""
封装多种通知
"""


class TradeNtf:
    # 已成交
    success = ('part-text', '已成交')
    # 已受理
    accept = ('part-text', '已受理')
    # 已排队
    queue = ('part-text', '已排队')

    @staticmethod
    def successNtf():
        Driver.check_element_exist(TradeNtf.success)

    @staticmethod
    def acceptNtf():
        Driver.check_element_exist(TradeNtf.accept)


class TopFloatBar(Driver):
    float_text = ("resourceId", "esunny.test:id/view_trade_notification_feedback")

    def getFloatText(self):
        return self.get_text(self.float_text)


if __name__ == '__main__':
    pass
