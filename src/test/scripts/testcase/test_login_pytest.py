import unittest

from src.test.scripts.framework.BaseTest import TestBase
from src.test.scripts.framework.DataUtil import ReadExcel
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.framework.OsPathUtil import DATA_DIR
from src.test.scripts.page.LoginPage import LoginPage
from src.test.scripts.framework import ConfigUtil
from src.test.resources.ddt import ddt, data

test_config = ConfigUtil.ConfigData()

file_path = DATA_DIR + r"/TestData.xlsx"
sheet_name = 'Login1'
wb = ReadExcel(file_path, sheet_name)
cases = wb.read_data_obj()


# 测试用例 = 测试对象的功能 + 测试数据
@ddt
class TestLoginPage(TestBase):
    @data(*cases)
    def testcase_login(self, case):
        if not case.ifDDT:
            self.skipTest("NoDDT")
        login_page = LoginPage(self.driver)
        login_page.verify()\
            .gotoLoginPage()\
            .chooseCompany(case.com)\
            .inputUserNo(case.acc)\
            .inputPassWord(case.pwd)\
            .clickSubmit()
        try:
            assert Driver.check_element_exist(self.driver, ('part-text', case.checkpoint1)) is True
        except AssertionError as e:
            Driver.get_screenshots_as_file(self.driver, extra=case.testNo)
            raise e

    def testcase_clickRiskBook(self):
        login_page = LoginPage(self.driver)
        login_page.gotoLoginPage()
        Driver.click(self.driver, login_page.risk_book)
        assert Driver.check_element_exist(self.driver, login_page.login_submit) is False

    def testcase_clickBackwards(self):
        login_page = LoginPage(self.driver)
        login_page.gotoLoginPage()
        Driver.click(self.driver, login_page.return_button)
        try:
            assert Driver.check_element_exist(self.driver, login_page.risk_book) is False
        except AssertionError as e:
            Driver.get_screenshots_as_file(self.driver)
            raise e

    def testcase_clickPwdInput(self):
        login_page = LoginPage(self.driver)
        login_page.gotoLoginPage()
        Driver.click(self.driver, login_page.login_pwd)
        assert Driver.check_element_exist(self.driver, login_page.risk_book) is False
        # assert login_page._check_element_exist(('part-text', '安全键盘')) is True


if __name__ == '__main__':
    test_dir = "./"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="testcase_*")
    runner = unittest.TextTestRunner()
    runner.run(discover)
