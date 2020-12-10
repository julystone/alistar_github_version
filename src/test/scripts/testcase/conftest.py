import os

import allure
import pytest

from src.test.scripts.framework.Driver import Driver


# conftest.py


# TODO 添加失败、成功截图、每次assert进行截图、截图监听器

@pytest.fixture(scope="function")
def getDriver():
    driver = Driver.prepareForAndroidAppium()
    yield driver
    driver.quit()


@pytest.fixture()
def getDriverFactory():  # fixture工厂
    driver_lists = []

    def _getDriverFactory(option=0):
        dv = Driver.prepareForAndroidAppium(option)
        driver_lists.append(dv)
        return dv

    yield _getDriverFactory

    for dv in driver_lists:
        dv.quit()


@pytest.fixture()
def gg():
    driver = Driver.prepareForAndroidAppium()
    return driver


@pytest.fixture()
def gd(request):
    request.param.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    print(outcome)
    report = outcome.get_result()

    if report.when == 'call':
        if report.outcome == 'failed':
            # for i in item.funcargs:
            #     if isinstance(item.funcargs[i], WebDriver):
            #         with allure.step('添加失败截图...'):
            #             allure.attach(Driver.get_screenshot_as_png(item.funcargs[i]), "失败截图",
            #                           allure.attachment_type.PNG)
            Driver.get_screenshot_as_file(item.funcargs['getDriver'], extra=item.funcargs["case"].testNo)
            with allure.step("添加失败截图..."):
                allure.attach(Driver.get_screenshot_as_png(item.funcargs['getDriver']), "失败截图",
                              allure.attachment_type.PNG)


@pytest.fixture(scope='session')
def rootdir(request):
    return os.path.join(request.config.rootdir)
