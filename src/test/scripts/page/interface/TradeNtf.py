from datetime import datetime

from src.test.scripts.framework.Driver import Driver
from src.test.scripts.page.navigate.QuotePage import QuotePage
from src.test.scripts.page.common.LoginPage import LoginPage

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


if __name__ == '__main__':
    pass
