from datetime import datetime

from src.test.scripts.framework.Driver import Driver
from src.test.scripts.page.navigate.QuotePage import QuotePage
from src.test.scripts.page.common.LoginPage import LoginPage


class Keyboard:
    """
    封装两种键盘，手数键盘、价格键盘
    以相对坐标轴封装，提高自动化效率
    """
    lots_keys = {
        '1': {'x': 135 / 1080, 'y': 1740 / 2201}, '2': {'x': 405 / 1080, 'y': 1740 / 2201},
        '3': {'x': 675 / 1080, 'y': 1740 / 2201},

        '4': {'x': 135 / 1080, 'y': 1895 / 2201}, '5': {'x': 405 / 1080, 'y': 1895 / 2201},
        '6': {'x': 675 / 1080, 'y': 1895 / 2201},

        '7': {'x': 135 / 1080, 'y': 2050 / 2201}, '8': {'x': 405 / 1080, 'y': 2050 / 2201},
        '9': {'x': 675 / 1080, 'y': 2050 / 2201},

        '00': {'x': 135 / 1080, 'y': 2165 / 2201}, '0': {'x': 405 / 1080, 'y': 2165 / 2201},
        '<-': {'x': 675 / 1080, 'y': 2165 / 2201},

        'plus': {'x': 945 / 1080, 'y': 1820 / 2201}, 'minus': {'x': 945 / 1080, 'y': 2128 / 2201},
        'hide': {'x': 945 / 1080, 'y': 1594 / 2201},
    }

    price_keys = {
        '市价': {'x': 107 / 1080, 'y': 1594 / 2201}, 'FOK': {'x': 323 / 1080, 'y': 1594 / 2201},
        'FAK': {'x': 539 / 1080, 'y': 1594 / 2201}, 'hide': {'x': 975 / 1080, 'y': 1594 / 2201},

        '对手价': {'x': 107 / 1080, 'y': 1740 / 2201}, '1': {'x': 323 / 1080, 'y': 1740 / 2201},
        '2': {'x': 539 / 1080, 'y': 1740 / 2201}, '3': {'x': 755 / 1080, 'y': 1740 / 2201},

        '最新价': {'x': 107 / 1080, 'y': 1895 / 2201}, '4': {'x': 323 / 1080, 'y': 1895 / 2201},
        '5': {'x': 539 / 1080, 'y': 1895 / 2201}, '6': {'x': 755 / 1080, 'y': 1895 / 2201},

        '排队价': {'x': 107 / 1080, 'y': 2050 / 2201}, '7': {'x': 323 / 1080, 'y': 2050 / 2201},
        '8': {'x': 539 / 1080, 'y': 2050 / 2201}, '9': {'x': 755 / 1080, 'y': 2050 / 2201},

        '超价': {'x': 107 / 1080, 'y': 2165 / 2201}, '.': {'x': 323 / 1080, 'y': 2165 / 2201},
        '0': {'x': 539 / 1080, 'y': 2165 / 2201}, '<-': {'x': 755 / 1080, 'y': 2165 / 2201},

        'plus': {'x': 975 / 1080, 'y': 1820 / 2201}, 'minus': {'x': 975 / 1080, 'y': 2128 / 2201},
        # 'buy': {'x': 480 / 1080, 'y': 1460 / 2201}, 'sell': {'x': 720 / 1080, 'y': 1460 / 2201},
    }

    @staticmethod
    def price_input(driver, price):
        print(price)
        if price in ['市价', '对手价', '最新价', '排队价', '超价']:
            Driver.click(driver, Keyboard.price_keys[price])
        for num in str(price):
            Driver.click(driver, Keyboard.price_keys[num])
        Driver.click(driver, Keyboard.price_keys['hide'])

    @staticmethod
    def lots_input(driver, slots):
        print(slots)
        for num in str(slots):
            Driver.click(driver, Keyboard.lots_keys[num])
        Driver.click(driver, Keyboard.lots_keys['hide'])


if __name__ == '__main__':
    pass
