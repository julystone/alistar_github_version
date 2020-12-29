# TODO _find_elements  还没调通
# TODO 截图嵌入报告中
# TODO 启动Appium
# TODO 发送邮件模块
from abc import ABC, abstractmethod


class Page(ABC):
    driver = None

    def setDriver(self, driver):
        self.driver = driver

    @abstractmethod
    def makeAPage(self):
        pass

