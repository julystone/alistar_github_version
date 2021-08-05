from src.test.scripts.page.BasePage.BasePageNoBottom import BasePageNoBottom
from src.test.scripts.page.navigate._NavigateBasePage import NavigateBasePage


class NewsPage(NavigateBasePage):
    # 资讯列表
    news_list = ("resourceId", "esunny.test:id/es_news_item_tv_title")
    # 校验项
    block_choose = '资讯'

    def getNewsList(self):
        news_list = []
        elem_list = self.findElemWithoutException(self.news_list)
        if elem_list is None:
            return elem_list
        for elem in elem_list:
            news_list.append(elem.info['text'])
        return news_list

    def getIntoOneNews(self):
        self.click(self.news_list)
        return self.OneNews()

    class OneNews(BasePageNoBottom):
        title_text = "详情"


if __name__ == '__main__':
    debugPage = NewsPage.OneNews()
    debugPage.quitPage()
