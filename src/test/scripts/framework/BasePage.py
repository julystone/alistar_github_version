# TODO _find_elements  还没调通
# TODO 截图嵌入报告中
# TODO 启动Appium
# TODO 发送邮件模块
from abc import ABC, abstractmethod

from src.test.scripts.framework.Driver_atx import Driver


class Page(ABC, Driver):
    BACK_BUTTON = ('resource-id', "esunny.test:id/toolbar_left_icons")

    def pageBack(self):
        self.click(self.BACK_BUTTON)
