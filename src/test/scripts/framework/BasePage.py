# TODO _find_elements  还没调通
# TODO 截图嵌入报告中
# TODO 启动Appium
# TODO 发送邮件模块
from abc import ABC, abstractmethod


class Page(ABC):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def verify(self):
        pass

    def quit(self):
        return self.driver.quit()


