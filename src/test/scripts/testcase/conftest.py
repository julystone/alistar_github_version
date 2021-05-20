import os

import allure
import pytest

from src.test.scripts.framework.Driver_atx import Driver


# conftest.py


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    # print(outcome)
    report = outcome.get_result()

    if report.when == 'call':
        if report.outcome == 'failed':
            # Driver().get_screenshot_as_file(extra=item.funcargs["case"].testNo)
            with allure.step("添加失败截图..."):
                allure.attach(Driver().get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


@pytest.fixture(scope='session')
def rootdir(request):
    return os.path.join(request.config.rootdir)
