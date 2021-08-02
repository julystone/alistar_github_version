from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.BasePage.BasePage import BasePage


class Interface(Driver, BasePage):
    def __init__(self):
        Driver.__init__(self)
        BasePage.__init__(self)

    def selfCheck(self):
        super().selfCheck()

    pass
