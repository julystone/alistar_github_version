from NavigateBasePage import NavigateBasePage


class QuotePage(NavigateBasePage):
    # 顶部栏
    exchange_switch_btn = ("resourceId", "esunny.test:id/toolbar_left_first")

    # 授权弹框
    quote_main = ("resourceId", "esunny.test:id/es_quote_sort_main")

    # 行情授权弹框
    auth_dialog = ('resourceId', "esunny.test:id/es_base_custom_dialog_title")
    auth_cancel_btn = ('text', '取消')

    # 行情列表
    quote_list = ("resourceId", "esunny.test:id/tv_quote_contractName")

    def __init__(self):
        super().__init__()
        self.goToQuotePage()
        assert self.check_element_exist(self.quote_main)

    def goToOptionPage(self):
        self.changeExchange('OPTION')

    def goToSingleQuotePage(self, pageName):
        loc = ('textContains', pageName.upper())
        self.click(loc)

    def changeExchange(self, exchangeName):
        exchangeName = exchangeName.upper()
        loc = ('textContains', exchangeName)
        self.click(self.exchange_switch_btn) \
            .scroll_until_locDisplayed(loc) \
            .click(loc) \
            .dialog_handle(self.auth_dialog, self.auth_cancel_btn)
        assert exchangeName in self.getCurTitle()
        return self

    def getQuoteList(self):
        return self.findElement(self.quote_list)


if __name__ == '__main__':
    debugPage = QuotePage()
    # res = debugPage.changeExchange('FOREIGN')
    res = debugPage.goToSingleQuotePage('棉纱')
    # Rt.click(Rt.menu_button)
    # Rt.goToAbout()
