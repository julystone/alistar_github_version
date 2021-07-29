from enum import Enum

import allure

from src.test.scripts.framework.MyLogger import my_log
from src.test.scripts.page.rightToolBar._SettingBasePage import SettingBasePage


class LoginPage(SettingBasePage):
    # 后台选址、账号输入、密码输入、提交按钮、保存账号、保存密码
    login_company = ("resourceId", 'esunny.test:id/et_login_company')
    login_userNo = ("resourceId", 'esunny.test:id/et_login_userno')
    login_pwd = ("resourceId", 'esunny.test:id/et_login_pwd')
    login_submit = ("resourceId", r'esunny.test:id/tv_login_submit')
    save_account = ("resourceId", r'esunny.test:id/es_login_activity_login_itv_save_account')
    save_pwd = ("resourceId", r'esunny.test:id/es_login_activity_login_etv_save_pwd')

    # 已阅读勾选、风险提示书
    login_notice = ("resourceId", 'esunny.test:id/es_activity_login_notice_check')
    risk_book = ("resourceId", r'esunny.test:id/es_activity_login_tv_state_confirm')

    # 启明星、北斗星
    local = ("resourceId", "esunny.estarandroid:id/es_activity_company_rl_local_future")  # 内盘
    foreign = ("resourceId", "esunny.estarandroid:id/es_activity_company_rl_foreign_future")  # 外盘
    informal = ("resourceId", "esunny.estarandroid:id/es_activity_company_rl_informal")  # 模拟交易
    formal = ("resourceId", "esunny.estarandroid:id/es_activity_company_rl_formal")  # 实盘交易

    local_enum = Enum('local', {'True': local, 'False': foreign})
    informal_enum = Enum('informal', {'True': informal, 'False': formal})

    # 校验项
    title_text = '交易登录'

    def getCurCompany(self):
        return self.get_text(self.login_company)

    def getCurUserNo(self):
        return self.get_text(self.login_userNo)

    def checkAccountSaved(self):
        return self.getCurCheckStatus(self.save_account)

    def checkPwdSaved(self):
        return self.getCurCheckStatus(self.save_pwd)

    def checkRiskBook(self):
        return self.getCurCheckStatus(self.login_notice)

    def goToRiskBook(self):
        self.click(self.risk_book)
        return self.RiskBook()

    def goToCompanyChoose(self):
        self.click(self.login_company)
        return self.CompanyChoose()

    @allure.step("切换  {company}  后台")
    def chooseCompany(self, company, local, informal):
        print(f"正在切换{company}后台")
        self.goToCompanyChoose()\
            .chooseCompany(company, local, informal)
        return self

    @allure.step("输入账号  {userNo}")
    def inputUserNo(self, userNo):
        print(f"正在输入userNo {userNo}")
        my_log.info(f"正在输入userNo {userNo}")
        self.set_text(self.login_userNo, userNo)
        self.getDriver().press("back")
        return self

    @allure.step("输入密码  {pwd}")
    def inputPassWord(self, pwd):
        print(f"正在输入passWord {pwd}")
        my_log.info(f"正在输入passWord {pwd}")
        self.set_text(self.login_pwd, pwd)
        self.click(self.title)
        return self

    @allure.step("点击提交")
    def clickSubmit(self):
        self.click(self.login_submit)
        return self

    def login_common(self, company='启明星', userNo='Q1223871051', pwd='111111'):
        # 通用登录不提供页面跳转前置
        if not self.checkAccountSaved():
            self.chooseCompany(company)\
                .inputUserNo(userNo)\
                .inputPassWord(pwd)\
                .clickSubmit()\
                .force_sleep(2)
        return self

    class RiskBook(SettingBasePage):
        # 校验项
        title_text = '服务协议'

    class CompanyChoose(SettingBasePage):
        # 校验项
        title_text = '选择公司'

        def chooseCompany(self, company, local, informal):
            self.click(LoginPage.local_enum[str(local)].value)
            self.click(LoginPage.informal_enum[str(informal)].value)
            locator = ('part-text', company)
            self.swipe_until_loc(locator).click(locator)
            return self


if __name__ == '__main__':
    lg = LoginPage()
    # lg.login_common()
    # input("点击继续")
    res = lg.inputUserNo("444")
    res = lg.inputPassWord("444")
