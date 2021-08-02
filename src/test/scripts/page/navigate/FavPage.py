from src.test.scripts.page.navigate._NavigateBasePage import NavigateBasePage


class FavPage(NavigateBasePage):
    # 顶部栏
    multi_quote_btn = ("resourceId", "esunny.test:id/toolbar_left_first")
    sort_btn = ("resourceId", "esunny.test:id/toolbar_left_second")
    more_btn = ("resourceId", "esunny.test:id/toolbar_right_second")

    # 授权弹框
    auth_dialog = ('resourceId', "esunny.test:id/es_base_custom_dialog_title")
    auth_cancel_btn = ('text', '取消')

    # 行情列表
    quote_list = ("resourceId", "esunny.test:id/tv_quote_contractName")

    # 校验项
    block_choose = "自选"

    def goToSingleQuotePage(self, pageName):
        loc = ('textContains', pageName.upper())
        self.click(loc)

    def getQuoteList(self):
        quote_list = []
        elem_list = self.find_elements(self.quote_list)
        for elem in elem_list:
            quote_list.append(elem.info['text'])
        return quote_list

    def goToQuoteSearch(self):
        self.click(self.more_btn).clickText("搜索添加")
        from src.test.scripts.page.interface.QuoteSearch import QuoteSearch
        return QuoteSearch()


if __name__ == '__main__':
    debugPage = FavPage()
    res = debugPage.getQuoteList()

    print(res[0], res[1])
