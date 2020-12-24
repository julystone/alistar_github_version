import time

from appium.webdriver.common.mobileby import MobileBy as By

from src.test.scripts.framework import Asserter
from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver import Driver
from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.page.interface.RightToolBar import RightToolBar
import allure


class LoginPage(Page):
    # title、左侧退出按钮
    title = (By.ID, 'esunny.test:id/toolbar_title')
    quit_button = (By.ID, 'esunny.test:id/toolbar_left_first')

    # 后台选址、账号输入、密码输入、提交按钮、保存账号、保存密码
    login_company = (By.ID, 'esunny.test:id/et_login_company')
    login_userNo = (By.ID, 'esunny.test:id/et_login_userno')
    login_pwd = (By.ID, 'esunny.test:id/et_login_pwd')
    login_submit = (By.ID, r'esunny.test:id/tv_login_submit')
    save_account = (By.ID, r'esunny.test:id/es_login_activity_login_itv_save_account')
    save_pwd = (By.ID, r'esunny.test:id/es_login_activity_login_etv_save_pwd')

    # 已阅读勾选、风险提示书
    login_notice = (By.ID, 'esunny.test:id/es_activity_login_notice_check')
    risk_book = (By.ID, r'esunny.test:id/es_activity_login_tv_state_confirm')

    # 启明星、北斗星
    qiMing = ('part-text', '启明星（上海仿真）')
    beiDou = ('part-text', '北斗星（上海仿真）')

    @staticmethod
    @allure.step("调用右边栏接口，进入登录页面")
    def makeAPage(driver):
        RightToolBar.goToLoginPage(driver)
        Asserter.shouldElemExist(driver, LoginPage.login_pwd)
        return LoginPage(driver)

    @staticmethod
    @allure.step("普通登录")
    def login_common(driver, company='启明星', userNo='Q1223871051', pwd='111111'):
        # 通用登录不提供页面跳转前置
        login_page = LoginPage(driver)
        if login_page.checkAccountSaved():
            login_page.clickSubmit()
        else:
            login_page.chooseCompany(company). \
                inputUserNo(userNo). \
                inputPassWord(pwd). \
                clickSubmit()
        time.sleep(2)
        return login_page

    @allure.step("选择开户公司")
    def chooseCompany(self, company):
        print(f"正在切换{company}后台")
        my_log.info(f"正在切换{company}后台")
        Driver.click(self.driver, self.login_company)
        locator = self.qiMing if company in "启明星" else self.beiDou
        Driver.scroll_until_elemDisplayed(self.driver, locator)
        Driver.click(self.driver, locator)
        return self

    @allure.step("输入交易账号")
    def inputUserNo(self, userNo):
        print(f"正在输入userNo {userNo}")
        my_log.info(f"正在输入userNo {userNo}")
        Driver.input_text(self.driver, self.login_userNo, userNo)
        return self

    @allure.step("输入交易密码")
    def inputPassWord(self, pwd):
        print(f"正在输入passWord {pwd}")
        my_log.info(f"正在输入passWord {pwd}")
        Driver.input_text(self.driver, self.login_pwd, pwd)
        return self

    @allure.step("点击登录")
    def clickSubmit(self):
        print("点击登录按钮")
        my_log.info("点击登录按钮")
        Driver.click(self.driver, self.login_submit)
        return self

    @allure.step("检查账号密码是否已经保存")
    def checkAccountSaved(self):
        print("检查账号密码是否已经保存")
        if Driver.get_text(self.driver, self.login_pwd) is None:
            print("账密未保存")
            return False
        print("账密已记住")
        return True


if __name__ == '__main__':
    dd = Driver.driverFactory(0)
    try:
        # log = Driver.goToPage(dd, LoginPage)
        # log.chooseCompany('启明星').\
        #     inputUserNo('Q1223871051').\
        #     inputPassWord('111111').\
        #     clickSubmit()
        LoginPage.login_common(dd)
    except Exception as e:
        print(e)
        raise e
    input("点击继续")
    dd.quit()
    # log.quit()
    # pytest.main(["-v", "--alluredir", f"{REPORT_DIR}/.allureTemp"])
    # os.system(f"allure generate {REPORT_DIR}/.allureTemp -o {REPORT_DIR}/allure --clean")