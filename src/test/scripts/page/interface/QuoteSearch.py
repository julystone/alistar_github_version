from src.test.scripts.framework.Asserter import Asserter
from src.test.scripts.page.interface._Interface import Interface


class QuoteSearch(Interface):
    quit_btn = ('text', '关闭')
    search_input = ("resourceId", "esunny.estarandroid:id/et_activity_search_text")
    search_result = ("resource-id", "esunny.estarandroid:id/rl_search_main")

    def selfCheck(self):
        Asserter.PageHasElem(self, self.search_input)

    def quitPage(self):
        self.click(self.quit_btn)
        return self

    def getSearchText(self):
        return self.get_text(self.search_input)

    def searchQuote(self, quote_name):
        self.set_text(self.search_input, quote_name)
        self.wait_element(self.search_result, 20)
        return self

    def getSearchResult(self):
        res_list = self.find_elements(self.search_result)
        search_result_list = []
        for res in res_list:
            search_result_list.append(res.child().info["text"])
        return search_result_list


if __name__ == '__main__':
    debugPage = QuoteSearch()
    res = debugPage.searchQuote("AP111").getSearchResult()
    print(res)
