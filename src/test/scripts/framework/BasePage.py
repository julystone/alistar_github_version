# TODO _find_elements  还没调通
# TODO 截图嵌入报告中
# TODO 启动Appium
# TODO 发送邮件模块


class Page:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def verify(driver):
        return Page(driver)

    def quit(self):
        return self.driver.quit()


