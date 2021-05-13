from assertpy import assert_that

from src.test.scripts.page.setting.SettingBasePage import SettingBasePage


# TODO  how to distinguish switch status between Open with Close?


class CommonSetting(SettingBasePage):
    # title
    title = ('text', '系统设置')
    quit_btn = ("resourceId", "esunny.test:id/es_activity_system_setting_iv_back")
    # 详细信息
    language = ('resourceId', "esunny.test:id/es_activity_system_setting_tv_language")
    disconnect_ring = ('resourceId', "esunny.test:id/es_activity_system_setting_switch_is_use_rington")
    trade_ring = ('resourceId', "esunny.test:id/es_activity_system_setting_switch_is_trade_use_rington")
    notify_ring = ('resourceId', "esunny.test:id/es_activity_system_setting_switch_is_message_use_rington")
    price_ring = ('resourceId', "esunny.test:id/es_activity_system_setting_tv_voice")
    screen_on_switch = ('resourceId', "esunny.test:id/es_activity_system_setting_switch_keep_screen_on")
    clear_favorite_list = ('resourceId', "esunny.test:id/es_activity_system_setting_rl_clear_favorites")
    clear_account_info = ('resourceId', "esunny.test:id/es_activity_system_setting_rl_clear_account_info")

    def selfCheck(self):
        assert_that(self.check_element_exist(self.title)).is_true()

    def getCurLang(self):
        return self.get_text(self.language)

    def getCurRingBell(self):
        return self.get_text(self.price_ring)

    def goToLangChoose(self):
        self.click(self.language)

    def goToRingBellSetting(self):
        self.click(self.price_ring)


if __name__ == '__main__':
    debugPage1 = CommonSetting()
    print(debugPage1)
    debugPage1 = CommonSetting()
    print(debugPage1)
    debugPage1 = CommonSetting()
    print(debugPage1)
    debugPage = CommonSetting()
    print(debugPage)
    res = debugPage.getCurRingBell()
    print(res)
    # debugPage.goToRingBellSetting()
    debugPage.getDriver().sleep(2)
    print(debugPage.findElement(debugPage.quit_btn).exists)
    # debugPage.quitPage()

    # debugPage.quitPage()
    # debugPage.goToLangChoose().pageBack()
