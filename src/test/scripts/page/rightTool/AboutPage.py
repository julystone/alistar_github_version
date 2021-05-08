from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.rightTool.RightToolBar import RightToolBar


class AboutPage(Page, Driver):
    # 左侧返回键、title
    title = ('text', '关于和帮助')

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

    def __init__(self):
        super().__init__()
        if not self.check_element_exist(self.title):
            RightToolBar().goToAbout()
        assert self.get_text(self.title) == '关于和帮助'

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

    def goToFeedbackPage(self):
        self.get_text(self.feedback)


if __name__ == '__main__':
    debugPage = AboutPage()
    res = debugPage.getVersion()
    print(res)
    debugPage.pageBack()
    # AP.goToUploadPage()
