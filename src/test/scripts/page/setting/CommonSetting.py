from assertpy import assert_that

from src.test.scripts.page.setting.SettingBasePage import SettingBasePage


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

    def goToLangChoose(self):
        self.click(self.language)

    def switchDisconnectRing(self, expect):
        self.changeOneSwitch(self.disconnect_ring, expect)
        return self

    def switchTradeRing(self, expect):
        self.changeOneSwitch(self.trade_ring, expect)
        return self

    def switchNotifyRing(self, expect):
        self.changeOneSwitch(self.notify_ring, expect)
        return self

    def switchKeepScreenOn(self, expect):
        self.changeOneSwitch(self.screen_on_switch, expect)
        return self

    def getCurRingBell(self):
        return self.get_text(self.price_ring)

    def goToRingBellSetting(self):
        self.click(self.price_ring)


class LangChoose(SettingBasePage):
    # 左侧返回键、title
    title = ('text', '切换语言')

    # 详细信息
    defaultBand = ("resourceId", "esunny.test:id/es_activity_switch_language_default")
    defaultChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_default")
    englishChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_english")
    chinaChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_china")
    hoKongChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_hongkong")

    def selfCheck(self):
        assert_that(self.check_element_exist(self.defaultBand)).is_true()

    def getCurrentLang(self):
        for loc in [self.defaultChoose, self.englishChoose, self.chinaChoose, self.hoKongChoose]:
            elem = self.findElemWithoutException(loc)
            if elem:
                break
        return elem.sibling().info['text']


class RingBellSetting(SettingBasePage):
    # title
    title = ('text', '价格预警音')

    # 详细信息
    bellList = ("resourceId", "esunny.test:id/es_activity_price_warning_rv")
    check = ("resourceId", "esunny.test:id/es_item_choose_default_price_tv_check")

    def selfCheck(self):
        assert_that(self.check_element_exist(self.bellList)).is_true()

    def getCurrentBell(self):
        elem = self.findElemWithoutException(self.check)
        return elem.sibling().info['text']


if __name__ == '__main__':
    debugPage = CommonSetting()
    debugPage.switchDisconnectRing(False).switchNotifyRing(True).switchKeepScreenOn(False)
    debugPage.getDriver().sleep(2)
