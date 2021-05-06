import os
import time

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import uiautomator2 as u2

from src.test.scripts.framework import ConfigUtil, BasePage
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.framework.OsPathUtil import SCREENSHOT_DIR


# TODO 启动Appium
class Device:
    d = u2.connect()


class PageOperation:
    @staticmethod
    def goToPage(Page):
        return Page.makeAPage()

    @staticmethod
    def SessionInit(packageName):
        return Device().d.session(packageName)

    @staticmethod
    def getWindowSize():
        return Operation.getDevice().window_size()

    @staticmethod
    def prepareForAndroidAppium(configChoice=0, ip='localhost', port='4723'):
        test_config = ConfigUtil.ConfigData(configChoice)
        desired_caps = {'deviceName': 'test_phone',
                        'platformName': test_config.get('test_phone', 'platformName'),
                        'platformVersion': test_config.get('test_phone', 'platformVersion'),
                        'appPackage': test_config.get('test_phone', 'appPackage'),
                        'appActivity': test_config.get('test_phone', 'appActivity'),
                        'automationName': "UiAutomator1",
                        'noReset': test_config.get('test_phone', 'noReset'),
                        'ignoreUnimportantViews': True,
                        'setWaitForIdleTimeout': 5
                        }
        driver = webdriver.Remote(f'http://{ip}:{port}/wd/hub', desired_caps)
        return driver

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
    def get_screenshot_as_file(extra=""):
        timeStamp = f"{time.strftime('%Y%m%d%H%M%S_', time.localtime())}"
        my_log.info("正在保存当前截图")
        Operation.getDevice().screenshot(SCREENSHOT_DIR + timeStamp + extra + ".png")

    @staticmethod
    def get_screenshot_as_png():
        # timeStamp = f"{time.strftime('%Y%m%d%H%M%S_', time.localtime())}"
        my_log.info("正在保存当前截图")
        return Operation.getDevice().get_screenshot_as_png()

    @staticmethod
    def findElement(loc):
        """
        对基础方法find_element做一层封装
        @param loc: locator
        @return:    WebElement对象
        """
        # 对查找元素做一层封装，对text、partial_text使用XPATH定位
        if "text" == loc[0]:
            loc = ("xpath", f"//*[@text='{loc[1]}']")
        elif "part-text" == loc[0]:
            loc = ("xpath", f"//*[contains(@text, '{loc[1]}')]")
        WebDriverWait(Operation.getDevice(), 10).until(EC.presence_of_element_located(loc), message="TimeOut")
        return Operation.getDevice().find_element(*loc)

    @staticmethod
    def findElemByImage(imagepath):
        return Operation.getDevice().find_element_by_image(imagepath)

    @staticmethod
    def findElemWithoutException(loc):
        """
        对findElement做一层封装，不报错
        @param loc: locator
        @return:    WebElement对象 或 None
        """
        elem = None
        try:
            elem = Operation.findElement(loc)
        except NoSuchElementException:
            print(f"{loc}元素没有定位到")
            my_log.info(f"{loc}元素没有定位到")
        except TimeoutException:
            print(f"{loc}元素定位超时")
            my_log.info(f"{loc}元素定位超时")
        return elem

    @staticmethod
    def find_elements(loc):
        # 对查找元素返回一整个符合定位的列表
        if "text" == loc[0]:
            loc = ("xpath", f"//*[@text='{loc[1]}']")
        elif "part-text" == loc[0]:
            loc = ("xpath", f"//*[contains(@text, '{loc[1]}')]")
        WebDriverWait(Operation.getDevice(), 20).until(EC.presence_of_element_located(loc), message="TimeOut")
        return Operation.getDevice().find_elements(*loc)

    @staticmethod
    def check_element_exist(loc):
        ret = True
        if isinstance(loc, dict):
            return ret
        elem = Operation.findElemWithoutException(loc)
        if None is elem:
            ret = False
        my_log.info(f"{loc} {ret}")
        return ret

    @staticmethod
    def scroll_until_elemDisplayed(loc):
        # Driver.swipe(driver, direction='U', duration=80)
        ret = True
        for _ in range(10):
            ret = Operation.check_element_exist(loc)
            if ret:
                break
            Operation.swipe(direction='U', duration=300)
        return ret

    @staticmethod
    def input_text(loc, text):
        elem = Operation.findElemWithoutException(loc)
        elem.clear()
        elem.send_keys(text)

    @staticmethod
    def loc_coord(loc):
        elem = Operation.findElemWithoutException(loc)
        return elem.location_in_view

    @staticmethod
    def click(loc):
        if isinstance(loc, dict):
            return Operation.click_coordinate(loc=loc)
        elif isinstance(loc, tuple):
            return Operation.findElement(loc).click()

    @staticmethod
    def click_coordinate(loc=None, x=None, y=None):
        if None is (loc or x or y):
            return "error Input"
        elif loc is None:
            time.sleep(0.5)
            return os.system(f"adb shell input tap {x} {y}")
        else:
            time.sleep(0.5)
            temp = {'x': Operation.getDevice().width * loc['x'], 'y': Operation.getDevice().height * loc['y']}
            return os.system(f"adb shell input tap {temp['x']} {temp['y']}")

    @staticmethod
    def long_press(loc=None, x=None, y=None, duration=1000):
        if loc is not None:
            coordinate = Operation.loc_coord(loc)
            x, y = coordinate['x'], coordinate['y']
        os.system(f"adb shell input swipe {x} {y} {x} {y} {duration}")

    @staticmethod
    def swipe(direction, duration=80):
        """
        调用ActionHelpers实现屏幕的滑动操作。4个坐标顺序分别为：
        :param driver:      Webdriver对象
        :param direction:   方向，可以填入[“L”, "R", "U", "D"]
        :param duration:    滑动速度，默认快速滑动，0ms
        :return:            None
        """
        size = list(Operation.getDevice().size.values())
        pattern = {"L": (3 / 4, 1 / 2, 1 / 4, 1 / 2),
                   "R": (1 / 4, 1 / 2, 3 / 4, 1 / 2),
                   "U": (1 / 2, 3 / 4, 1 / 2, 1 / 4),
                   "D": (1 / 2, 1 / 4, 1 / 2, 3 / 4)}
        params = [pattern[direction][i] * (size + size)[i] for i in range(4)]
        # return ActionHelpers.swipe(driver, *params, duration=duration)
        os.system(f"adb shell input swipe {params[0]} {params[1]} {params[2]} {params[3]} {duration}")
        time.sleep(1)

    @staticmethod
    def get_text(loc):
        return Operation.findElemWithoutException(loc).text

    @staticmethod
    def get_toast_message(toast_message):
        loc = ('part-text', toast_message)
        return Operation.get_text(loc)

    # @staticmethod
    # def scroll_to_elem(driver, loc):
    #     webDriver.getDriver().webelement.WebElement.click()
    #     webDriver.getDriver().webDriver.getDriver().WebDriver.tap()
    #     ActionHelpers.tap()
    #     pass

    @staticmethod
    def quit():
        Operation.getDevice().quit()


if __name__ == '__main__':
    Operation.deviceInit(1)
    Operation.findElemByImage('./pics/add.jpg')
    Operation.quit()
