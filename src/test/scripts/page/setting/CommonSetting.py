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
    # 校验项
    title_text = '系统设置'

    def getCurLang(self):
        return self.get_text(self.language)

    def goToLangChoose(self):
        self.click(self.language)
        return self.LangChoose()

    def getDisconnectRingStatus(self):
        return self.getCurSwitchStatus(self.disconnect_ring)

    def switchDisconnectRing(self, expect):
        self.changeOneSwitch(self.disconnect_ring, expect)
        return self

    def getTradeRingStatus(self):
        return self.getCurSwitchStatus(self.trade_ring)

    def switchTradeRing(self, expect):
        self.changeOneSwitch(self.trade_ring, expect)
        return self

    def getNotifyRingStatus(self):
        return self.getCurSwitchStatus(self.notify_ring)

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
        return self.RingBellSetting()

    class LangChoose(SettingBasePage):
        # 详细信息
        defaultBand = ("resourceId", "esunny.test:id/es_activity_switch_language_default")
        defaultChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_default")
        englishChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_english")
        chinaChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_china")
        hoKongChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_hongkong")
        # Alert
        alert_title = ("resourceId", "esunny.test:id/es_custom_toast_dialog_tv_title")
        confirm_btn = ("resourceId", "esunny.test:id/es_custom_toast_dialog_tv_confirm")
        # 校验项
        title_text = '切换语言'

        def getCurLang(self):
            for loc in [self.defaultChoose, self.englishChoose, self.chinaChoose, self.hoKongChoose]:
                elem = self.findElemWithoutException(loc)
                if elem:
                    break
            return elem.sibling().info['text']

        def changeLang(self, lang):
            self.clickText(lang)
            self.dialog_handle(self.alert_title, self.confirm_btn)
            return self

    class RingBellSetting(SettingBasePage):
        # title
        title = ('text', '价格预警音')
        # 详细信息
        bellList = ("resourceId", "esunny.test:id/es_activity_price_warning_rv")
        check = ("resourceId", "esunny.test:id/es_item_choose_default_price_tv_check")
        # 校验项
        title_text = '切换语言'

        def getCurrentBell(self):
            elem = self.findElemWithoutException(self.check)
            return elem.sibling().info['text']


if __name__ == '__main__':
    debugPage = CommonSetting()
    debugPage = CommonSetting().LangChoose()
    # debugPage.switchDisconnectRing(False).switchNotifyRing(True).switchKeepScreenOn(False)
    # debugPage.goToLangChoose().getCurLang()

    debugPage.getDriver().sleep(2)
