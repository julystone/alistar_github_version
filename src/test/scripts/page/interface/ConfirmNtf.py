from datetime import datetime

from src.test.scripts.framework.Driver import Driver
from src.test.scripts.page.navigate.QuotePage import QuotePage
from src.test.scripts.page.common.LoginPage import LoginPage

"""
封装多种通知
"""


class ConfirmNtf:
    # 不再提示
    no_more = ('text', '不再提示')
    # dialog_title
    dialog_title = ('id', 'esunny.test:id/es_base_custom_dialog_title')
    # 取消
    cancel_button = ('id', 'esunny.test:id/es_base_custom_dialog_cancel')
    # 确定
    confirm_button = ('id', 'esunny.test:id/ed_base_custom_dialog_setting')

    # TODO 添加更多通知弹框

    @staticmethod
    def noMoreNtf(driver):
        if Driver.check_element_exist(driver, ConfirmNtf.dialog_title):
            Driver.click(driver, ConfirmNtf.no_more)
            Driver.click(driver, ConfirmNtf.confirm_button)


if __name__ == '__main__':
    pass
