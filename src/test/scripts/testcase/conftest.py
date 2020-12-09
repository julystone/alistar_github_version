import os

import allure
import pytest

# conftest.py
from appium.webdriver.webdriver import WebDriver

from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver import Driver

driver = None


@pytest.fixture(scope="function")
def getDriver():
    driver = Driver.prepareForAndroidAppium()
    yield driver
    driver.quit()


@pytest.fixture()
def getDriverFactory():  # fixture工厂
    driver_lists = []

    def _getDriverFactory(option=0):
        driver = Driver.prepareForAndroidAppium(option)
        driver_lists.append(driver)
        return driver

    yield _getDriverFactory

    for driver in driver_lists:
        driver.quit()


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#     # we only look at actual failing test calls, not setup/teardown
#     if rep.when == "call" and rep.failed:
#         mode = "a" if os.path.exists("failures") else "w"
#         with open("failures", mode) as f:
#             # let's also access a fixture for the fun of it
#             if "tmpdir" in item.fixturenames:
#                 extra = " (%s)" % item.funcargs["tmpdir"]
#             else:
#                 extra = ""
#             f.write(rep.nodeid + extra + "\n")
#         # pic_info = adb_screen_shot()
#         with allure.step('添加失败截图...'):
#             allure.attach(Driver.get_screenshots_as_file(driver), "失败截图", allure.attachment_type.PNG)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        # 判断用例是否失败或者xfail跳过的测试
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 获取测试用例代码中webDriver参数来获取浏览器进行抓屏
            for i in item.funcargs:
                if isinstance(item.funcargs[i], WebDriver):
                    # 截图
                    with allure.step('添加失败截图...'):
                        allure.attach(Driver.get_screenshots_as_file(driver), "失败截图", allure.attachment_type.PNG)
        report.extra = extra
