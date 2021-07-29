import os

import allure
import pytest

from src.test.scripts.framework.Driver_atx import Driver
# conftest.py
from utils import DataUtil


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        if report.outcome == 'failed':
            # Driver().get_screenshot_as_file(extra=item.funcargs["case"].testNo)
            with allure.step("添加失败截图..."):
                allure.attach(Driver().get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)
            DataUtil

# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """当测试失败的时候，自动截图，展示到html报告中"""
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_")+".png"
#             screen_img = Driver().get_screenshot_as_png()
#             if file_name:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
#                        'οnclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra


@pytest.fixture(scope='session')
def rootdir(request):
    return os.path.join(request.config.rootdir)
