from src.test.scripts.page.setting._SettingBasePage import SettingBasePage


class AboutPage(SettingBasePage):
    # 详细信息
    packageNo = ('resource-id', 'esunny.test:id/activity_es_about_tv_package_no_value')
    quoteAddr = ('resource-id', "esunny.test:id/activity_es_about_tv_quote_address_value")
    hisQuoteAddr = ('resource-id', "esunny.test:id/activity_es_about_tv_his_quote_address_value")
    website = ('resource-id', "esunny.test:id/activity_es_about_tv_website")
    phoneNo = ('resource-id', "esunny.test:id/activity_es_about_tv_qq_value")
    weixin = ('resource-id', "esunny.test:id/activity_es_about_tv_weixin_value")
    mac = ('resource-id', "esunny.test:id/activity_es_about_tv_mac_value")
    version = ('resource-id', "esunny.test:id/activity_es_about_tv_version_value")
    upload = ('resource-id', "esunny.test:id/activity_es_about_rl_daily")
    feedback = ('resource-id', "esunny.test:id/activity_es_about_rl_feedback")
    privacy = ('resource-id', "esunny.test:id/activity_es_about_rl_privacy")
    # 校验项
    title_text = "关于和帮助"

    def getPackageNo(self):
        return self.get_text(self.packageNo)

    def getQuoteAddr(self):
        return self.get_text(self.quoteAddr)

    def getHisQuoteAddr(self):
        return self.get_text(self.hisQuoteAddr)

    def getVersion(self):
        return self.get_text(self.version)

    def goToUploadPage(self):
        self.click(self.upload)
        return self.UploadPage()

    def goToFeedbackPage(self):
        self.click(self.feedback)
        return self.FeedbackPage()

    class UploadPage(SettingBasePage):
        title_text = '上传运行日志'
        submit_btn = ("resourceId", "esunny.test:id/tv_daily_submit")
        phone_input = ("resourceId", "esunny.test:id/activity_estar_upload_daily_phone_et")
        log_list = ("resourceId", "esunny.test:id/activity_estar_upload_daily_no_file")

    class FeedbackPage:
        title_text = '反馈中心'


if __name__ == '__main__':
    debugPage = AboutPage()
    res = debugPage.getVersion()
    print(res)
    debugPage.goToUploadPage()
    debugPage.getDriver().sleep(2)
    # debugPage.findElement(debugPage.quit_btn)
    debugPage.quitPage()
