from src.test.scripts.framework.BasePage import Page
from src.test.scripts.framework.Driver_atx import Driver


class LangChoose(Page, Driver):
    # 左侧返回键、title
    title = ('text', '切换语言')

    # 详细信息
    defaultBand = ("resourceId", "esunny.test:id/es_activity_switch_language_default")
    defaultChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_default")
    englishChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_english")
    chinaChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_china")
    hoKongChoose = ("resourceId", "esunny.test:id/es_activity_switch_language_etv_hongkong")

    def __init__(self):
        super().__init__()
        self.selfCheck()

    def selfCheck(self):
        assert self.check_element_exist(self.defaultBand) is True

    def getCurrentLang(self):
        for loc in [self.defaultChoose, self.englishChoose, self.chinaChoose, self.hoKongChoose]:
            elem = self.findElemWithoutException(loc)
            if elem.exists:
                break
        return elem.sibling().info['text']


if __name__ == '__main__':
    debugPage = LangChoose()
    res = debugPage.getCurrentLang()
    print(res)
    debugPage.pageBack()
