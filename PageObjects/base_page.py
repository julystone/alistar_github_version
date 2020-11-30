import time

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common.R_r_os import SCREENSHOT_DIR
from common.R_r_log import my_log


# TODO _find_elements  还没调通
# TODO check_elements_exist 需要重新整理
# TODO 截图
# TODO 日志

class Page:
    def __init__(self, driver):
        # 打开浏览器，访问网址
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.size = self.driver.get_window_size()
        self.timeout = 30

    def _get_screenshots_as_file(self):
        # 对PO具体截图
        png_name = f"{time.strftime('screen_%Y_%m_%d_%H_%M_%S', time.localtime())}.png"
        self.driver.get_screenshot_as_file(SCREENSHOT_DIR + png_name)
        my_log.info("[S]正在保存当前截图")

    def try_except(self, func):
        # 对断言失败的进行截屏保存
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except AssertionError:
                self._get_screenshots_as_file()
        return wrapper

    def _find_element(self, *loc):
        # 对查找元素做一层封装，对text、partial_text使用XPATH定位
        if "text" == loc[0]:
            loc = ("xpath", f"//*[@text='{loc[1]}']")
        elif "part-text" == loc[0]:
            loc = ("xpath", f"//*[contains(@text, '{loc[1]}')]")
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(loc), message="TimeOut")
            return self.driver.find_element(*loc)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"[F]{loc}元素没有定位到")
            my_log.error(f"[F]{loc}元素没有定位到")
            self._get_screenshots_as_file()
            raise e

    def _find_elements(self, *loc):
        # 对查找元素返回一整个列表
        if "text" == loc[0]:
            loc = ("xpath", f"//*[@text='{loc[1]}']")
        elif "part-text" == loc[0]:
            loc = ("xpath", f"//*[contains(@text, '{loc[1]}')]")
        # try:
        return self.driver.find_elements(*loc)

    def _check_element_exist(self, loc):
        try:
            self._find_element(*loc)
        except (TimeoutException, NoSuchElementException):
            print(f"[F]{loc}元素不存在")
            my_log.info(f"[F]{loc}元素不存在")
            return False
        print(f"[S]{loc}元素存在")
        my_log.info(f"[S]{loc}元素存在")
        return True

    def _input_text(self, loc, text):
        self._find_element(*loc).clear().send_keys(text)

    def _click(self, loc):
        self._find_element(*loc).click()

    def get_text(self, loc):
        return self._find_element(*loc).texts

    def get_toast_message(self, toast_message):
        loc = ('part-text', toast_message)
        return self.get_text(loc)

    def swipe_up(self, duration=500, times=1):
        x1 = self.size['width'] * 0.5  # x坐标
        x2 = self.size['width'] * 0.5  # x坐标
        y1 = self.size['height'] * 0.75  # 起始y坐标
        y2 = self.size['height'] * 0.25  # 终点y坐标
        for i in range(times):
            self.driver.swipe(x1, y1, x2, y2, duration)

    def swipe_down(self, duration=500, times=1):
        x1 = self.size['width'] * 0.5  # x坐标
        x2 = self.size['width'] * 0.5  # x坐标
        y1 = self.size['height'] * 0.25  # 起始y坐标
        y2 = self.size['height'] * 0.75  # 终点y坐标
        for i in range(times):
            self.driver.swipe(x1, y1, x2, y2, duration)

    def swipe_left(self, duration=500, times=1):
        x1 = self.size['width'] * 0.75  # x坐标
        x2 = self.size['width'] * 0.25  # x坐标
        y1 = self.size['height'] * 0.5  # 起始y坐标
        y2 = self.size['height'] * 0.5  # 终点y坐标
        for i in range(times):
            self.driver.swipe(x1, y1, x2, y2, duration)

    def swipe_right(self, duration=500, times=1):
        x1 = self.size['width'] * 0.25  # x坐标
        x2 = self.size['width'] * 0.75  # x坐标
        y1 = self.size['height'] * 0.5  # 起始y坐标
        y2 = self.size['height'] * 0.5  # 终点y坐标
        for i in range(times):
            self.driver.swipe(x1, y1, x2, y2, duration)
