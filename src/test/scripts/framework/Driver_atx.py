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
class Connection:
    _single = None

    def __init__(self, addr):
        self.driver = u2.connect(addr)

    def __new__(cls, *args, **kwargs):
        if cls._single is None:
            cls._single = object.__new__(cls)
        return cls._single


class Driver:
    def __init__(self, addr='', implicitly_time=20):
        self._addr = addr
        self._d = Connection(addr).driver
        self._d.implicitly_wait(implicitly_time)
        self.width, self.height = self._d.window_size()
        self.deviceInfo = self._d.device_info
        self.appStart('esunny.test')

    def setDriver(self, newDriver):
        self._d = newDriver

    def getDriver(self):
        return self._d

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

    def appStart(self, package_name, activity=None, stop=False):
        if not self.getDriver().app_current()['package'] == package_name:
            self.getDriver().app_start(package_name=package_name, activity=activity, wait=True, stop=stop)

    def activityStart(self, activity):
        self.getDriver().app_start(package_name='esunny.test', activity=activity)

    def get_screenshot_as_file(self, extra=""):
        timeStamp = f"{time.strftime('%Y%m%d%H%M%S_', time.localtime())}"
        my_log.info("正在保存当前截图")
        self.getDriver().screenshot(SCREENSHOT_DIR + timeStamp + extra + ".png")

    def get_screenshot_as_png(self):
        # timeStamp = f"{time.strftime('%Y%m%d%H%M%S_', time.localtime())}"
        my_log.info("正在保存当前截图")
        return self.getDriver().screenshot()

    @staticmethod
    def locAdaptor(loc):
        if isinstance(loc, dict):
            loc = [list(loc.keys())[0], list(loc.values())[0]]
        elif isinstance(loc, tuple):
            loc = list(loc)
        via = loc[0].lower()
        if via in ['text', 'test']:
            loc[0] = 'text'
        elif via in ['part-text', 'partText']:
            loc[0] = 'textContains'
        elif via in ['resource-id', 'resourceId', 'id']:
            loc[0] = 'resourceId'
        elif via in ['xpath']:
            return loc[1]
        return {loc[0]: loc[1]}

    def findElement(self, loc):
        loc = Driver.locAdaptor(loc)
        if isinstance(loc, dict):
            return self.getDriver()(**loc)
        else:
            return self.getDriver().xpath(loc)

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

    def loc2coord(self, loc):
        elem = self.findElemWithoutException(loc)
        return elem.center()

    def click(self, loc):
        self.findElemWithoutException(loc).click()

    def click_coordinate(self, x=None, y=None):
        if None is (x or y):
            return "error Input"
        else:
            time.sleep(0.5)
            return self.getDriver().click(x, y)

    def long_click(self, loc=None, x=None, y=None, duration=1000):
        if loc is not None:
            coordinate = self.loc2coord(loc)
            x, y = coordinate['x'], coordinate['y']
        self.getDriver().long_click(x, y, duration)
        # os.system(f"adb shell input swipe {x} {y} {x} {y} {duration}")

    def swipe(self, direction):
        """
        :param direction: up, down, left, right  Caps Included
        :return: None
        """
        self.getDriver().swipe_ext(direction.lower())

    def scroll_until_locDisplayed(self, loc):
        loc = Driver.locAdaptor(loc)
        self.getDriver()(scrollable=True).scroll.to(**Driver.locAdaptor(loc))

    def set_text(self, loc, text):
        elem = self.findElemWithoutException(loc)
        elem.set_text(text)

    def get_text(self, loc):
        return self.findElemWithoutException(loc).get_text()

    def get_toast_message(self, toast_message):
        loc = ('part-text', toast_message)
        return self.get_text(loc)


if __name__ == '__main__':
    d = Driver()
    d1 = Driver()
    d2 = Driver()
    print(d2.getDriver().app_current()['package'])
    print(d2.getDriver().app_info('esunny.test'))
    # d2.getDriver().wait_activity('com.esunny.ui.login.EsLoginActivity')
    # d2.activityStart('com.esunny.ui.login.EsLoginActivity')
    # di = {'part-text': '安粮期货', }
    # dii = ('text', '纯碱110')
    # d.swipe('up')
    # print(d.getDriver().app_current())
    # d1.swipe('down')
    # d2.swipe('up')
