from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.rightTool.LangChoose import LangChoose


# TODO  how to distinguish switch status between Open with Close?
class CommonSetting(Page, Driver):
    # title
    title = ('text', '系统设置')

    # 详细信息
    language = ('resourceId', "esunny.test:id/es_activity_system_setting_tv_language")
    disconnect_ring = ('resourceId', "esunny.test:id/es_activity_system_setting_switch_is_use_rington")
    trade_ring = ('resourceId', "esunny.test:id/es_activity_system_setting_switch_is_trade_use_rington")
    notify_ring = ('resourceId', "esunny.test:id/es_activity_system_setting_switch_is_message_use_rington")
    price_ring = ('resourceId', "esunny.test:id/es_activity_system_setting_tv_voice")
    screen_on_switch = ('resourceId', "esunny.test:id/es_activity_system_setting_switch_keep_screen_on")
    clear_favorite_list = ('resourceId', "esunny.test:id/es_activity_system_setting_rl_clear_favorites")
    clear_account_info = ('resourceId', "esunny.test:id/es_activity_system_setting_rl_clear_account_info")

    def __init__(self):
        super().__init__()
        assert self.check_element_exist(self.clear_account_info) is True

    def getCurLang(self):
        return self.get_text(self.language)

    def goToLangChoose(self):
        self.click(self.language)
        return LangChoose()

    def getCurRingBell(self):
        return self.get_text(self.price_ring)

    def goToRingBellSetting(self):
        self.click(self.price_ring)


if __name__ == '__main__':
    debugPage = CommonSetting()
    res = debugPage.getCurRingBell()
    print(res)
    debugPage.goToLangChoose().pageBack()
