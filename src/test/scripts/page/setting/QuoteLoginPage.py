from src.test.scripts.page.setting._SettingBasePage import SettingBasePage


class QuoteLoginPage(SettingBasePage):
    # 详细信息
    user_no = ("resourceId", "esunny.test:id/et_login_userno")
    password = ("resourceId", "esunny.test:id/et_login_pwd")
    login_submit = ("resourceId", "esunny.test:id/tv_login_submit")
    # 校验项
    title_text = "行情账号登录"

    def getCurUserno(self):
        return self.get_text(self.user_no)

    def setUserNo(self, user_no):
        self.set_text(self.user_no, user_no)
        self.click(self.title)
        return self

    def setPwd(self, password):
        self.set_text(self.password, password)
        self.click(self.title)
        return self

    def quoteLoginCommon(self, user_no, password):
        if not self.get_text(self.user_no) == user_no:
            self.setUserNo(user_no)
            self.setPwd(password)
        self.click(self.login_submit)
        self.wait_element_gone(self.user_no, 5)
        return self


if __name__ == '__main__':
    debugPage = QuoteLoginPage()
    debugPage.setUserNo(123)
    debugPage.setPwd(123)
    debugPage.quoteLoginCommon(user_no='estest020', password='123456@es')
