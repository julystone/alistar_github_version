import allure

from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.BasePage.BasePage import BasePage


class BasePageWithBottom(BasePage, Driver):
    # 底部切换栏列表
    annal_list = []

    # 校验项
    block_choose = '测试'

    def __init__(self):
        Driver.__init__(self)
        BasePage.__init__(self)

    def selfCheck(self):
        # self.force_sleep(2)
        with allure.step("校验当前页面：" + self.block_choose):
            # allure.attach(body=self.get_screenshot_as_png(), name='当前页面', attachment_type=allure.attachment_type.PNG)
            Asserter.TextEqualText(self.getCurSelectedPage(), self.block_choose)

    def getCurSelectedPage(self):
        for loc in self.annal_list:
            if self.getCurItemStatus(loc):
                break
        return self.findElemWithoutException(loc).info['text']


if __name__ == '__main__':
    debugPage = BasePageWithBottom()
