import time

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.test.scripts.framework import ConfigUtil
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.framework.OsPathUtil import SCREENSHOT_DIR


# TODO _find_elements  还没调通
# TODO 截图嵌入报告中
# TODO 启动Appium
# TODO 发送邮件模块

class Driver:
    def __init__(self, configChoice):
        self.driver = self.prepareForAndroidAppium(configChoice)
        self.size = self.driver.get_window_size()

    @staticmethod
    def prepareForAndroidAppium(configChoice=0):
        test_config = ConfigUtil.ConfigData(configChoice)
        desired_caps = {'platformName': test_config.get('test_phone', 'platformName'),
                        'platformVersion': test_config.get('test_phone', 'platformVersion'),
                        'appPackage': test_config.get('test_phone', 'appPackage'),
                        'appActivity': test_config.get('test_phone', 'appActivity'),
                        'noReset': test_config.get('test_phone', 'noReset')}
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @staticmethod
    def prepareForIOSAppium(configChoice):
        # TODO iOS还没调试
        test_config = ConfigUtil.ConfigData(configChoice)
        desired_caps = {'platformName': test_config.get('test_phone', 'platformName'),
                        'platformVersion': test_config.get('test_phone', 'platformVersion'),
                        'appPackage': test_config.get('test_phone', 'appPackage'),
                        'appActivity': test_config.get('test_phone', 'appActivity'),
                        'noReset': test_config.get('test_phone', 'noReset')}
        return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @staticmethod
    def get_screenshots_as_file(driver, extra=""):
        timeStamp = f"{time.strftime('%Y%m%d%H%M%S_', time.localtime())}"
        driver.get_screenshot_as_file(SCREENSHOT_DIR + timeStamp + extra + ".png")
        my_log.info("正在保存当前截图")

    @staticmethod
    def findElement(driver, loc):
        # 对查找元素做一层封装，对text、partial_text使用XPATH定位
        if "text" == loc[0]:
            loc = ("xpath", f"//*[@text='{loc[1]}']")
        elif "part-text" == loc[0]:
            loc = ("xpath", f"//*[contains(@text, '{loc[1]}')]")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located(loc), message="TimeOut")
        return driver.findElement(*loc)

    @staticmethod
    def findElemWithoutException(driver, loc):
        elem = None
        try:
            elem = Driver.findElement(driver, loc)
        except Exception:
            print(f"{loc}元素没有定位到")
            my_log.info(f"{loc}元素没有定位到")
        return elem

    @staticmethod
    def find_elements(driver, loc):
        # 对查找元素返回一整个列表
        if "text" == loc[0]:
            loc = ("xpath", f"//*[@text='{loc[1]}']")
        elif "part-text" == loc[0]:
            loc = ("xpath", f"//*[contains(@text, '{loc[1]}')]")
        # try:
        return driver.find_elements(*loc)

    @staticmethod
    def check_element_exist(driver, loc):
        ret = True
        elem = Driver.findElemWithoutException(driver, loc)
        if None is elem:
            ret = False
        my_log.info(f"{loc} {ret}")
        return ret

    @staticmethod
    def input_text(driver, loc, text):
        elem = Driver.findElemWithoutException(driver, loc)
        elem.clear()
        elem.send_keys(text)

    @staticmethod
    def click(driver, loc):
        Driver.findElemWithoutException(driver, loc).click()

    @staticmethod
    def get_text(driver, loc):
        return Driver.findElemWithoutException(driver, loc).text

    @staticmethod
    def get_toast_message(driver, toast_message):
        loc = ('part-text', toast_message)
        return Driver.get_text(driver, loc)

    @staticmethod
    def quit(driver):
        driver.quit()

