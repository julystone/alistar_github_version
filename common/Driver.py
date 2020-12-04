import time

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common import ConfigUtil
from common.MyLogger import my_log
from common.R_r_os import SCREENSHOT_DIR


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
    def _find_element(driver, loc):
        # 对查找元素做一层封装，对text、partial_text使用XPATH定位
        if "text" == loc[0]:
            loc = ("xpath", f"//*[@text='{loc[1]}']")
        elif "part-text" == loc[0]:
            loc = ("xpath", f"//*[contains(@text, '{loc[1]}')]")
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(loc), message="TimeOut")
            return driver.find_element(*loc)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"{loc}元素没有定位到")
            my_log.info(f"{loc}元素没有定位到")
            raise e

    @staticmethod
    def _find_elements(driver, loc):
        # 对查找元素返回一整个列表
        if "text" == loc[0]:
            loc = ("xpath", f"//*[@text='{loc[1]}']")
        elif "part-text" == loc[0]:
            loc = ("xpath", f"//*[contains(@text, '{loc[1]}')]")
        # try:
        return driver.find_elements(*loc)

    @staticmethod
    def check_element_exist(driver, loc):
        try:
            Driver._find_element(driver, loc)
        except (TimeoutException, NoSuchElementException):
            print(f"{loc}元素不存在")
            my_log.info(f"{loc}元素不存在")
            return False
        print(f"{loc}元素存在")
        my_log.info(f"{loc}元素存在")
        return True

    @staticmethod
    def input_text(driver, loc, text):
        Driver._find_element(driver, loc).clear().send_keys(text)

    @staticmethod
    def click(driver, loc):
        Driver._find_element(driver, loc).click()

    @staticmethod
    def get_text(driver, loc):
        return Driver._find_element(driver, loc).text

    @staticmethod
    def get_toast_message(driver, toast_message):
        loc = ('part-text', toast_message)
        return Driver.get_text(driver, loc)

