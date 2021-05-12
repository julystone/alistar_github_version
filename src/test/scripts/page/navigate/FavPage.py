from NavigateBasePage import NavigateBasePage


class FavPage(NavigateBasePage):
    # 顶部栏
    multi_quote_btn = ("resourceId", "esunny.test:id/toolbar_left_first")
    sort_btn = ("resourceId", "esunny.test:id/toolbar_left_second")
    add_fav_btn = ("resourceId", "esunny.test:id/toolbar_right_second")

    # 授权弹框
    auth_dialog = ('resourceId', "esunny.test:id/es_base_custom_dialog_title")
    auth_cancel_btn = ('text', '取消')

    # 行情列表
    quote_list = ("resourceId", "esunny.test:id/tv_quote_contractName")

    def __init__(self):
        super().__init__()
        self.goToFavPage()
        elem = self.findElemWithoutException(self.auth_dialog)
        if elem is not None:
            self.click(self.auth_cancel_btn)
        assert self.getCurTitle() == '自选'

    def goToSingleQuotePage(self, pageName):
        loc = ('textContains', pageName.upper())
        self.click(loc)

    def getQuoteList(self):
        return self.findElement(self.quote_list)


if __name__ == '__main__':
    debugPage = FavPage()
    res = debugPage.getQuoteList()
    temp_list = []
    for _ in res:
        temp_list.append(_.get_text())
        # print(_.get_text())
    print(temp_list)
    print(res[1].get_text())
    # Rt.click(Rt.menu_button)
    # Rt.goToAbout()
