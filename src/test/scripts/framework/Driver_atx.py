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
class Driver:
    def __init__(self, addr, package_name, implicitly_time=20):
        self._d = u2.connect(addr)
        self._d.implicitly_wait(implicitly_time)
        # self.windowSize = self._d.window_size()
        self.width, self.height = self._d.window_size()
        self.deviceInfo = self._d.device_info
        self._session = self._d.session(package_name=package_name)

    # def __del__(self):
    #     self._session.close()

    def setDriver(self, newDriver):
        self._d = newDriver

    def getDriver(self):
        return self._d

    def appStart(self, package_name, activity, stop):
        self.getDriver().app_start(package_name=package_name, activity=activity, wait=True, stop=stop)

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

    def get_screenshot_as_file(self, extra=""):
        timeStamp = f"{time.strftime('%Y%m%d%H%M%S_', time.localtime())}"
        my_log.info("正在保存当前截图")
        self.getDriver().screenshot(SCREENSHOT_DIR + timeStamp + extra + ".png")

    def get_screenshot_as_png(self):
        # timeStamp = f"{time.strftime('%Y%m%d%H%M%S_', time.localtime())}"
        my_log.info("正在保存当前截图")
        return self.getDriver().screenshot()

    def findElement(self, loc):
        via = loc[0].upper()
        if via == 'TEXT':
            return self.getDriver()(text=loc[1])
        elif via == 'PART-TEXT':
            return self.getDriver()(textContains=loc[1])
        elif via == 'RESOURCE-ID':
            return self.getDriver()(resourceId=loc[1])
        else:
            print("match rules not found")

    # def findElemByImage(self, imagepath):
    #     return self.find_element_by_image(imagepath)

    def findElemWithoutException(self, loc):
        """
        对findElement做一层封装，不报错
        @param loc: locator
        @return:    WebElement对象 或 None
        """
        elem = None
        try:
            elem = self.findElement(loc)
        except NoSuchElementException:
            print(f"{loc}元素没有定位到")
            my_log.info(f"{loc}元素没有定位到")
        except TimeoutException:
            print(f"{loc}元素定位超时")
            my_log.info(f"{loc}元素定位超时")
        return elem

    def find_elements(self, loc):
        # 对查找元素返回一整个符合定位的列表
        if "text" == loc[0]:
            loc = ("xpath", f"//*[@text='{loc[1]}']")
        elif "part-text" == loc[0]:
            loc = ("xpath", f"//*[contains(@text, '{loc[1]}')]")
        WebDriverWait(self.getDriver(), 20).until(EC.presence_of_element_located(loc), message="TimeOut")
        return self.getDriver().find_elements(*loc)

    def check_element_exist(self, loc):
        ret = self.findElement(loc).exists()
        return ret

    def input_text(self, loc, text):
        elem = self.findElemWithoutException(loc)
        elem.send_keys(text, clear=True)

    @staticmethod
    def loc_coord(loc):
        elem = self.findElemWithoutException(loc)
        return elem.location_in_view

    def click(self, loc):
        if isinstance(loc, dict):
            return self.click_coordinate(loc=loc)
        elif isinstance(loc, tuple):
            return self.findElement(loc).click()

    def click_coordinate(self, loc=None, x=None, y=None):
        if None is (loc or x or y):
            return "error Input"
        elif loc is None:
            time.sleep(0.5)
            return os.system(f"adb shell input tap {x} {y}")
        else:
            time.sleep(0.5)
            temp = {'x': self.width * loc['x'], 'y': self.height * loc['y']}
            return os.system(f"adb shell input tap {temp['x']} {temp['y']}")

    @staticmethod
    def long_press(loc=None, x=None, y=None, duration=1000):
        if loc is not None:
            coordinate = self.loc_coord(loc)
            x, y = coordinate['x'], coordinate['y']
        os.system(f"adb shell input swipe {x} {y} {x} {y} {duration}")

    def swipe(self, direction):
        self.getDriver().swipe_ext(direction.lower())

    def scroll_until_elemDisplayed(self, loc):
        # Driver.swipe(driver, direction='U', duration=80)
        ret = True

        ret = self.findElement(loc).scroll
        for _ in range(10):
            ret = self.check_element_exist(loc)
            if ret:
                break
            self.swipe(direction='U', duration=300)
        return ret

    @staticmethod
    def get_text(loc):
        return self.findElemWithoutException(loc).text

    @staticmethod
    def get_toast_message(toast_message):
        loc = ('part-text', toast_message)
        return self.get_text(loc)

    # @staticmethod
    # def scroll_to_elem(driver, loc):
    #     webDriver.getDriver().webelement.WebElement.click()
    #     webDriver.getDriver().webDriver.getDriver().WebDriver.tap()
    #     ActionHelpers.tap()
    #     pass

    @staticmethod
    def quit():
        self.getDriver().quit()


if __name__ == '__main__':
    self.deviceInit(1)
    self.findElemByImage('./pics/add.jpg')
    self.quit()
