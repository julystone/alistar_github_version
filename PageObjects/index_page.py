from selenium.webdriver.common.by import By


class TopLane:
    # 首页、常见问题、注册/登录
    homeBtn = (By.XPATH, '//li[contains(text(),"首页")]')
    issuesBtn = (By.XPATH, '//li[contains(text(),"常见问题")]')
    loginBtn = (By.XPATH, '//li[contains(text(),"注册/登录")]')


class LeftMenu:
    # 行情授权、插件授权、套餐优惠
    quoteMenu = (By.XPATH, '//li[contains(text(),"行情授权")]')
    pluginMenu = (By.XPATH, '//li[contains(text(),"插件授权")]')
    package = (By.XPATH, '//li[contains(text(),"套餐优惠")]')


# 行情授权相关
class QuoteMenu:
    class FirstQuote:
        pos = '//div[@class="childWrap"]/div[1]'
        quotoName = (By.XPATH, pos + '//div[@class="goodsDetail"]/p[1]')
        quotoPrice = (By.XPATH, pos + '//div[@class="goodsDetail"]//span[@class="goodsPrice"]')

    price = (By.XPATH, '//span[@class="totalPrice"]')
    payBtn = (By.XPATH, '//button[text()="立即购买"]')


