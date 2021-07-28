from src.test.scripts.framework.Driver_atx import Driver
from src.test.scripts.page.BasePage.BasePage import BasePage


class BaseKeyboard(BasePage, Driver):
    """
    封装两种键盘，手数键盘、价格键盘
    以相对坐标轴封装，提高自动化效率
    """
    key_down = None
    key_plus = None
    key_minus = None
    key_back = None

    def __init__(self):
        super(BaseKeyboard, self).__init__()

    def selfCheck(self):
        pass

    def numInput(self, num):
        for _ in str(num):
            self.clickText(_)
        self.keyboardDown()

    def numAddOne(self):
        self.click(self.key_plus)

    def numMinusOne(self):
        self.click(self.key_minus)

    def keyboardDown(self):
        self.click(self.key_down)


class PriceKeyBoard(BaseKeyboard):
    key_down = ("resourceId", "esunny.test:id/ImageView_trade_keyboard_keyDone")
    key_plus = ("resourceId", "esunny.test:id/button_trade_keyboard_keyPlus")
    key_minus = ("resourceId", "esunny.test:id/button_trade_keyboard_keyMinus")
    key_back = ("resourceId", "esunny.test:id/ImageView_trade_keyboard_keyBack")

    def __init__(self):
        super(PriceKeyBoard, self).__init__()
        print(self.key_down)
        assert self.check_element_exist(self.key_down)

    def priceInput(self, price):
        print(price)
        if price in ['市价', '对手价', '最新价', '排队价', '超价']:
            self.clickText(price)
        else:
            self.numInput(price)

    def chooseFak(self):
        self.clickText('FAK')

    def chooseFok(self):
        self.clickText('FOK')


class LotsKeyBoard(BaseKeyboard):
    key_down = ("resourceId", "esunny.test:id/ImageView_trade_keyboard_lots_keyDone")
    key_plus = ("resourceId", "esunny.test:id/button_trade_keyboard_lots_keyPlus")
    key_minus = ("resourceId", "esunny.test:id/button_trade_keyboard_lots_keyMinus")
    key_back = ("resourceId", "esunny.test:id/ImageView_trade_keyboard_lots_keyBack")

    def __init__(self):
        super(LotsKeyBoard, self).__init__()
        assert self.check_element_exist(self.key_down)

    def lotsInput(self, lots):
        print(lots)
        self.numInput(lots)


if __name__ == '__main__':
    # debugPage1 = LotsKeyBoard()
    # debugPage1.keyboardDown()
    # debugPage2 = PriceKeyBoard()
    # debugPage2.keyboardDown()
    # debugPage3 = BaseKeyboard()
    # debugPage3.keyboardDown()
    pass