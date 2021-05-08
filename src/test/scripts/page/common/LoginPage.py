import time
from enum import Enum

from appium.webdriver.common.mobileby import MobileBy as By

from src.test.scripts.framework import Asserter
from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.framework.MyLogger import my_log
import allure


class LoginPage(Page, Driver):
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
    company_enum = Enum('company', {'启明星': qiMing, '北斗星': beiDou})

    @allure.step("调用右边栏接口，进入登录页面")
    def __init__(self):
        super().__init__()
        Asserter.shouldElemExist(self.login_pwd)

    @allure.step("普通登录")
    def login_common(self, company='启明星', userNo='Q1223871051', pwd='111111'):
        # 通用登录不提供页面跳转前置
        login_page = LoginPage()
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
        self.click(self.login_company)
        locator = self.company_enum[company].value
        self.scroll_until_locDisplayed(locator)
        self.click(locator)
        return self

    @allure.step("输入交易账号")
    def inputUserNo(self, userNo):
        print(f"正在输入userNo {userNo}")
        my_log.info(f"正在输入userNo {userNo}")
        self.set_text(self.login_userNo, userNo)
        return self

    @allure.step("输入交易密码")
    def inputPassWord(self, pwd):
        print(f"正在输入passWord {pwd}")
        my_log.info(f"正在输入passWord {pwd}")
        self.set_text(self.login_pwd, pwd)
        return self

    @allure.step("点击登录")
    def clickSubmit(self):
        print("点击登录按钮")
        my_log.info("点击登录按钮")
        self.click(self.login_submit)
        return self

    @allure.step("点击风险责任书")
    def clickRiskBook(self):
        print("点击风险责任书")
        my_log.info("点击风险责任书")
        self.click(self.risk_book)
        return self

    @allure.step("点击登录")
    def clickBackwards(self):
        print("点击登录按钮")
        my_log.info("点击登录按钮")
        self.click(self.quit_button)
        return self

    @allure.step("检查账号密码是否已经保存")
    def checkAccountSaved(self):
        print("检查账号密码是否已经保存")
        if Driver.get_text(self.login_pwd) is None:
            print("账密未保存")
            return False
        print("账密已记住")
        return True


if __name__ == '__main__':
    lg = LoginPage()
    lg.makeAPage()

    LoginPage.makeAPage()\
        .login_common()

    input("点击继续")
    Driver.quit()
    # log.quit()
    # pytest.main(["-v", "--alluredir", f"{REPORT_DIR}/.allureTemp"])
    # os.system(f"allure generate {REPORT_DIR}/.allureTemp -o {REPORT_DIR}/allure --clean")
