# TODO _find_elements  还没调通
# TODO 截图嵌入报告中
# TODO 启动Appium
# TODO 发送邮件模块
from abc import ABC, abstractmethod

from src.test.scripts.framework.Driver_atx import Driver


class BasePage(ABC):
    def __init__(self):
        super(BasePage, self).__init__()
        self.selfCheck()

    @staticmethod
    def operationDeco(operation):
        def wrapper(self, *args, **kwargs):
            page = operation(self, *args, **kwargs)
            if page is None:
                return self
        return wrapper

    @abstractmethod
    def selfCheck(self):
        pass
