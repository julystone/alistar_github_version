import time
from typing import Union

import uiautomator2 as u2
from uiautomator2 import UiObject

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

    # _count = 0

    def __new__(cls, *args, **kwargs):
        # cls._count += 1
        if cls._single is None:
            cls._single = object.__new__(cls)
            cls.ConnectionInit()
        # print(cls._count)
        return cls._single

    @classmethod
    def ConnectionInit(cls):
        global PACKAGE_NAME
        pre = cls.prepareForAndroidATX()
        cls._addr = pre['addr']
        cls._d = u2.connect(cls._addr)

        cls._implicitly_time = pre['implicitly_time']
        cls._d.settings['wait_timeout'] = (int(cls._implicitly_time))

        cls._packageName = pre['appPackage']
        PACKAGE_NAME = cls._packageName

        cls.width, cls.height = cls._d.window_size()
        cls.deviceInfo = cls._d.device_info

    @classmethod
    def setDriver(cls, newDriver):
        cls._d = newDriver

    @classmethod
    def getDriver(cls) -> u2.Device:
        return cls._d

    @classmethod
    def getPackageName(cls):
        return cls._packageName

    @staticmethod
    def prepareForAndroidATX(configChoice=1):
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

    def getDriver(self) -> u2.Device:
        return self._d

    def getPackageName(self) -> str:
        return self._packageName

    def appStart(self, stop=False):
        self.getDriver().app_start(package_name=self._packageName, wait=True, stop=stop)
        self.dialog_handle(('text', '未获取到权限'), ('text', '取消'))
        self.getDriver()(text="自选").wait(20)

    def appRestart(self):
        self.appStart(stop=True)

    def get_screenshot_as_file(self, extra=""):
        timeStamp = f"{time.strftime('%Y%m%d%H%M%S_', time.localtime())}"
        my_log.info("正在保存当前截图")
        self.getDriver().screenshot(SCREENSHOT_DIR + timeStamp + extra + ".png")

    def get_screenshot_as_png(self):
        my_log.info("正在保存当前截图")
        # pass
        return self.getDriver().screenshot(format='pillow')

    def locAdaptor(self, loc):
        # TODO 不同包号id会更改
        if self.getPackageName() not in loc[1]:
            temp = loc[1].replace('esunny.test', PACKAGE_NAME)
            loc = (loc[0], temp)
        loc = list(loc)
        via = loc[0].lower()
        if via in ['text']:
            loc[0] = 'text'
        elif via in ['part-text', 'parttext', 'textcontains']:
            loc[0] = 'textContains'
        elif via in ['resource-id', 'resourceid', 'id']:
            loc[0] = 'resourceId'
        elif via in ['xpath']:
            return loc[1]
        return {loc[0]: loc[1]}

    def findElement(self, loc) -> UiObject:
        loc = Driver.locAdaptor(self, loc)
        if isinstance(loc, dict):
            return self.getDriver()(**loc)
        else:
            return self.getDriver().xpath(loc)

    def findElemWithoutException(self, loc: Union[tuple, UiObject]):
        """
        对findElement做一层封装，不报错
        @param loc: locator或者UiObject对象
        @return:    UiObject对象 或 None
        """
        if isinstance(loc, UiObject):
            return loc
        self.wait_element(loc, 1.5)
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
        elem = self.findElemWithoutException(loc)
        return elem.exists

    def changeOneSwitch(self, switch, expect):
        # 开关按钮操作
        if self.getCurSwitchStatus(switch) != expect:
            self.click(switch)
        return self

    def changeOneCheck(self, check, expect):
        # 勾选项操作
        if self.getCurCheckStatus(check) != expect:
            self.click(check)
        return self

    def getCurSwitchStatus(self, switch):
        # 检测switch开关是否打开，eg：深度买红买绿
        return self.findElemWithoutException(switch).info['checked']

    def getCurItemStatus(self, item):
        # 检测板块是否被选中
        return self.findElemWithoutException(item).info['selected']

    def getCurCheckStatus(self, check):
        # 检测圆形勾选栏是否勾选，eg：记住密码
        elem = self.findElemWithoutException(check)
        if elem.get_text() == '\ue617':
            return True
        elif elem.get_text() == '\ue61c':
            return False

    def getCurSortStatus(self, sort):
        # 检测排序的三角控件是否启用(黑色)，eg：合约排序
        elem = self.findElemWithoutException(sort)
        if elem.get_text() == '\ue65b':
            return True
        elif elem.get_text() == '\ue65a':
            return False

    def wait_element(self, loc, timeout):
        elem = self.findElement(loc)
        return elem.wait(timeout=timeout)

    def wait_element_gone(self, loc, timeout):
        elem = self.findElemWithoutException(loc)
        if elem is None:
            return True
        return elem.wait_gone(timeout=timeout)

    def loc2coord(self, loc):
        elem = self.findElemWithoutException(loc)
        return elem.center()

    def click(self, loc):
        elem = self.findElemWithoutException(loc)
        elem.click()
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

    def force_sleep(self, seconds):
        time.sleep(seconds)
        return self

    def long_click(self, loc=None, x=None, y=None, duration=1000):
        if loc is not None:
            coordinate = self.loc2coord(loc)
            x, y = coordinate['x'], coordinate['y']
        self.getDriver().long_click(x, y, duration)
        # os.system(f"adb shell input swipe {x} {y} {x} {y} {duration}")

    def swipe(self, direction, *args, **kwargs):
        """
        :param direction: up, down, left, right  Caps Included
        :return: None
        """
        self.getDriver().swipe_ext(direction.lower(), *args, **kwargs)
        return self

    # def swipe_zone(self, direction, loc):
    #     elem = self.findElemWithoutException(loc)
    #     scale = elem.info["visibleBounds"]
    #     quyu = (scale['left'], scale['top'], scale['right'], scale['bottom'])
    #     self.getDriver().swipe_ext(direction,box=quyu)

    def swipe_loc(self, direction, loc):
        # 指定某区域上下滑动
        elem = self.findElemWithoutException(loc)
        if direction == '上划':
            elem.scroll.vert.backward()
        elif direction == '下滑':
            elem.scroll.toEnd()

    def swipe_until_text(self, text, loc):
        # 上下滑动至出现指定text
        elem = self.findElemWithoutException(loc)
        elem.scroll.to(text=text)

    def swipe_until_loc(self, loc):
        loc = self.locAdaptor(loc)
        self.getDriver()(scrollable=True).scroll.to(**loc)
        return self

    def set_text(self, loc, text):
        elem = self.findElemWithoutException(loc)
        elem.set_text(text)

    def get_text(self, loc):
        elem = self.findElemWithoutException(loc)
        return elem.get_text()

    def get_toast_message(self, toast_message):
        loc = ('part-text', toast_message)
        return self.get_text(loc)

    def dialog_handle(self, dialog, btn):
        if self.check_element_exist(dialog):
            elem = self.findElemWithoutException(btn)
            res = elem.click_gone()
            assert res is True
        return self


if __name__ == '__main__':
    d = Driver()
    res = d.get_text(("resourceId", "esunny.test:id/es_activity_system_setting_tv_language"))
    print(res)
    # d.swipe_zone('up', (0, 221, 359, 2040))
