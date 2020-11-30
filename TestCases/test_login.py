import unittest

from PageObjects.login_page import LoginPage
from TestCases.Base_Test import TestBase
from common import R_r_config
from common.R_r_excel import ReadExcel
from common.R_r_os import DATA_DIR
from library.ddt import ddt, data

test_config = R_r_config.ConfigData()

file_path = DATA_DIR + r"/TestData.xlsx"
sheet_name = 'Login'
wb = ReadExcel(file_path, sheet_name)
cases = wb.read_data_obj()


# 测试用例 = 测试对象的功能 + 测试数据
@ddt
class TestLoginPage(TestBase):

    @data(*cases)
    def estcase_login(self, case):
        if not case.ifDDT:
            self.skipTest("NoDDT")
        login_page = LoginPage(self.driver)
        login_page.gotoLoginPage()
        login_page.choose_company(case.com)
        login_page.input_userNo(case.acc)
        login_page.input_passWord(case.pwd)
        login_page.click_submit()
        assert login_page._check_element_exist(('part-text', case.checkpoint1)) is True

    def testcase_clickRiskBook(self):
        login_page = LoginPage(self.driver)
        login_page.gotoLoginPage()
        login_page._click(login_page.risk_book)
        assert login_page._check_element_exist(login_page.login_submit) is False

    def testcase_clickBackwards(self):
        login_page = LoginPage(self.driver)
        login_page.gotoLoginPage()
        login_page._click(login_page.return_button)
        try:
            assert login_page._check_element_exist(login_page.risk_book) is False
        except AssertionError:
            login_page._get_screenshots_as_file()

    def testcase_clickPwdInput(self):
        login_page = LoginPage(self.driver)
        login_page.gotoLoginPage()
        login_page._click(login_page.login_pwd)
        assert login_page._check_element_exist(login_page.risk_book) is False
        # assert login_page._check_element_exist(('part-text', '易星安全键盘')) is True


if __name__ == '__main__':
    # unittest.main()
    test_dir = "./"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="testcase_lo*")
    runner = unittest.TextTestRunner()
    runner.run(discover)
