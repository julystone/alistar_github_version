from src.test.scripts.page.navigate._NavigateBasePage import NavigateBasePage


class NewsPage(NavigateBasePage):
    # 资讯列表
    news_list = ("resourceId", "esunny.test:id/es_news_item_tv_title")
    # 校验项
    block_choose = '资讯'

    def getNewsList(self):
        news_list = []
        elem_list = self.find_elements(self.news_list)
        for elem in elem_list:
            news_list.append(elem.info['text'])
        return news_list


if __name__ == '__main__':
    debugPage = NewsPage()
    res = debugPage.getNewsList()
    print(res)
