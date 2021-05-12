from NavigateBasePage import NavigateBasePage


class NewsPage(NavigateBasePage):
    # 顶部栏

    # 资讯列表
    news_list = ("resourceId", "esunny.test:id/es_news_item_tv_title")

    def __init__(self):
        super().__init__()
        self.goToNewsPage()
        assert self.getCurTitle() == '资讯'

    def getNewsList(self):
        return self.findElement(self.news_list)


if __name__ == '__main__':
    debugPage = NewsPage()
    res = debugPage.getNewsList()
    temp_list = []
    for _ in res:
        temp_list.append(_.get_text())
        # print(_.get_text())
    print(temp_list)
    print(res[1].get_text())
    # Rt.click(Rt.menu_button)
    # Rt.goToAbout()
