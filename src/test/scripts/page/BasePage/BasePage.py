from abc import ABC, abstractmethod


class BasePage(ABC):
    def __init__(self):
        super(BasePage, self).__init__()
        self.selfCheck()

    @abstractmethod
    def selfCheck(self):
        pass
