import time

from appium import webdriver
from appium.webdriver.extensions.action_helpers import ActionHelpers
from appium.webdriver.common.touch_action import TouchAction
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

    @staticmethod
    def getWindowSize(driver):
        return driver.get_window_size()

    @staticmethod
    def prepareForAndroidAppium(configChoice=0, ip='localhost', port='4723'):
        test_config = ConfigUtil.ConfigData(configChoice)
        desired_caps = {'deviceName': 'test_phone',
                        'platformName': test_config.get('test_phone', 'platformName'),
                        'platformVersion': test_config.get('test_phone', 'platformVersion'),
                        'appPackage': test_config.get('test_phone', 'appPackage'),
                        'appActivity': test_config.get('test_phone', 'appActivity'),
                        'noReset': test_config.get('test_phone', 'noReset')}
        return webdriver.Remote(f'http://{ip}:{port}/wd/hub', desired_caps)

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
    def get_screenshot_as_file(driver, extra=""):
        timeStamp = f"{time.strftime('%Y%m%d%H%M%S_', time.localtime())}"
        my_log.info("正在保存当前截图")
        driver.get_screenshot_as_file(SCREENSHOT_DIR + timeStamp + extra + ".png")

    @staticmethod
    def get_screenshot_as_png(driver):
        # timeStamp = f"{time.strftime('%Y%m%d%H%M%S_', time.localtime())}"
        my_log.info("正在保存当前截图")
        return driver.get_screenshot_as_png()

    @staticmethod
    def findElement(dv, loc):
        """
        对基础方法find_element做一层封装
        @param dv:  传入的driver
        @param loc: locator
        @return:    WebElement对象
        """
        # 对查找元素做一层封装，对text、partial_text使用XPATH定位
        if "text" == loc[0]:
            loc = ("xpath", f"//*[@text='{loc[1]}']")
        elif "part-text" == loc[0]:
            loc = ("xpath", f"//*[contains(@text, '{loc[1]}')]")
        WebDriverWait(dv, 5).until(EC.presence_of_element_located(loc), message="TimeOut")
        return dv.find_element(*loc)

    @staticmethod
    def findElemWithoutException(driver, loc):
        """
        对findElement做一层封装，不报错
        @param driver:  传入的driver
        @param loc: locator
        @return:    WebElement对象 或 None
        """
        elem = None
        try:
            elem = Driver.findElement(driver, loc)
        except NoSuchElementException:
            print(f"{loc}元素没有定位到")
            my_log.info(f"{loc}元素没有定位到")
        except TimeoutException:
            print(f"{loc}元素定位超时")
            my_log.info(f"{loc}元素定位超时")
        return elem

    @staticmethod
    def find_elements(dv, loc):
        # 对查找元素返回一整个符合定位的列表
        if "text" == loc[0]:
            loc = ("xpath", f"//*[@text='{loc[1]}']")
        elif "part-text" == loc[0]:
            loc = ("xpath", f"//*[contains(@text, '{loc[1]}')]")
        WebDriverWait(dv, 20).until(EC.presence_of_element_located(loc), message="TimeOut")
        return dv.find_elements(*loc)

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
        elem = Driver.findElemWithoutException(driver, loc)
        coordinate = elem.location_in_view
        # 解决页面刷新过快，定位到元素后，点击过慢的问题
        return ActionHelpers.tap(driver, [(coordinate['x'], coordinate['y'])])

    @staticmethod
    def long_press(driver, loc=None, x=None, y=None):
        if loc is not None:
            elem = Driver.findElemWithoutException(driver, loc)
            return TouchAction.press(driver, el=elem)
        elif x is not None and y is not None:
            return TouchAction.press(driver, x=x, y=y)

    @staticmethod
    def get_text(driver, loc):
        return Driver.findElemWithoutException(driver, loc).text

    @staticmethod
    def get_toast_message(driver, toast_message):
        loc = ('part-text', toast_message)
        return Driver.get_text(driver, loc)

    # @staticmethod
    # def scroll_to_elem(driver, loc):
    #     webdriver.webelement.WebElement.click()
    #     webdriver.webdriver.WebDriver.tap()
    #     ActionHelpers.tap()
    #     pass

    @staticmethod
    def quit(driver):
        driver.quit()


if __name__ == '__main__':
    a = webdriver.webelement.WebElement.location_in_view
    dic = {1: 11, 2: 22}
    print(tuple(dic.values()))
