import time

import uiautomator2 as u2

from src.test.scripts.framework import ConfigUtil
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.framework.OsPathUtil import SCREENSHOT_DIR

# Driver：页面驱动程序，可实例化。
# Connection： 手机配置、连接实例，单例即可
# TODO 将Driver中可提出单例的，移到Connection中

PACKAGE_NAME = None


class Connection:
    _packageName = None
    _d = None
    _single = None
    _count = 0

    def __new__(cls, *args, **kwargs):
        cls._count += 1
        if cls._single is None:
            cls._single = object.__new__(cls)
            cls.ConnectionInit()
        print(cls._count)
        return cls._single

    @classmethod
    def ConnectionInit(cls):
        global PACKAGE_NAME
        pre = cls.prepareForAndroidATX()
        cls._addr = pre['addr']
        cls._d = u2.connect(cls._addr)

        cls._implicitly_time = pre['implicitly_time']
        cls._d.implicitly_wait(int(cls._implicitly_time))

        cls._packageName = pre['appPackage']
        PACKAGE_NAME = cls._packageName

        cls.width, cls.height = cls._d.window_size()
        cls.deviceInfo = cls._d.device_info

    @classmethod
    def setDriver(cls, newDriver):
        cls._d = newDriver

    @classmethod
    def getDriver(cls):
        return cls._d

    @classmethod
    def getPackageName(cls):
        return cls._packageName

    @staticmethod
    def prepareForAndroidATX(configChoice=0):
        print("读取配置")
        test_config = ConfigUtil.ConfigData(configChoice)
        desired_caps = {'addr': test_config.get('test_phone', 'addr'),
                        'implicitly_time': test_config.get('test_phone', 'implicitly_time'),
                        'appPackage': test_config.get('test_phone', 'appPackage'),
                        'appActivity': test_config.get('test_phone', 'appActivity'),
                        }
        return desired_caps

    @staticmethod
    def prepareForIOSAppium(configChoice):
        # TODO iOS还没调试
        pass


class Driver:
    def __init__(self):
        self._d = Connection().getDriver()
        self._packageName = PACKAGE_NAME

    def getDriver(self):
        return self._d

    def getPackageName(self):
        return self._packageName

    def appStart(self, stop=False):
        self.getDriver().app_start(package_name=self._packageName, wait=True, stop=stop)
        self.findElement(("id", "esunny.test:id/tv_start_loading")).wait_gone()

    def appRestart(self):
        self.appStart(stop=True)
        print("restart success")

    def get_screenshot_as_file(self, extra=""):
        timeStamp = f"{time.strftime('%Y%m%d%H%M%S_', time.localtime())}"
        my_log.info("正在保存当前截图")
        self.getDriver().screenshot(SCREENSHOT_DIR + timeStamp + extra + ".png")

    def get_screenshot_as_png(self):
        my_log.info("正在保存当前截图")
        return self.getDriver().screenshot(format='raw')

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
            self.wait_element(loc, 1.5)
            return self.getDriver()(**loc)
        else:
            return self.getDriver().xpath(loc)

    def findElemWithoutException(self, loc):
        """
        对findElement做一层封装，不报错
        @param loc: locator
        @return:    WebElement对象 或 None
        """
        elem = self.findElement(loc)
        if not elem.exists:
            elem = None
            print(f"{loc}元素没有定位到")
            my_log.info(f"{loc}元素没有定位到")
        return elem

    def findElemViaText(self, text):
        loc = ('text', text)
        return self.findElemWithoutException(loc)

    def find_elements(self, loc):
        # 对查找元素返回一整个符合定位的列表
        return self.findElement(loc)

    def check_element_exist(self, loc):
        ret = self.findElement(loc).exists
        return ret

    def wait_element(self, loc, timeout):
        assert self.getDriver()(**loc).wait(timeout=timeout)

    def loc2coord(self, loc):
        elem = self.findElemWithoutException(loc)
        return elem.center()

    def click(self, loc):
        self.findElemWithoutException(loc).click()
        return self

    def clickText(self, text):
        loc = ('text', text)
        return self.click(loc)

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
        return self

    def scroll_until_locDisplayed(self, loc):
        loc = Driver.locAdaptor(loc)
        self.getDriver()(scrollable=True).scroll.to(**Driver.locAdaptor(loc))
        return self

    def set_text(self, loc, text):
        elem = self.findElemWithoutException(loc)
        elem.set_text(text)

    def get_text(self, loc):
        return self.findElemWithoutException(loc).get_text()

    def get_toast_message(self, toast_message):
        loc = ('part-text', toast_message)
        return self.get_text(loc)

    def dialog_handle(self, dialog, btn):
        if self.check_element_exist(dialog):
            res = self.findElement(btn).click_gone()
            # self.click(btn)
            # self.driver.sleep(0.5)
            assert res is True
        return self


if __name__ == '__main__':
    d = Driver()
    print(d.getDriver())
    d1 = Driver()
    print(d1.getDriver())
    d2 = Driver()
    print(d2.getDriver())
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
