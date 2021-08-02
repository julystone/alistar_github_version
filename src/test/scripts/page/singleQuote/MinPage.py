from src.test.scripts.page.singleQuote._SingleQuoteBasePage import SingleQuoteBasePage


class MinPage(SingleQuoteBasePage):
    # 校验项
    block_choose = '分时'


if __name__ == '__main__':
    debugPage = MinPage()
    debugPage.goToThudTradeMode().setLots(123)
