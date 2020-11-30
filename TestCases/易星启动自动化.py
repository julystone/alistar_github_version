from time import sleep

from appium import webdriver

sleep(5)
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0.0'
desired_caps['appPackage'] = 'esunny.test'
desired_caps['appActivity'] = 'com.esunny.estar.StartActivity'
desired_caps['noReset'] = 'true'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


# driver.set_page_load_timeout(5)


if __name__ == "__main__":
    sleep(5)
    driver.find_element_by_id("esunny.test:id/toolbar_right_first")._click()
    driver.find_element_by_accessibility_id("交易登录").click()
    driver.find_element_by_name("text:交易登录")._click()
    driver.find_element_by_id("esunny.test:id/toolbar_left_first")._click()

    driver.find_element_by_partial_link_text("图标设置")._click()
    driver.find_element_by_id("esunny.test:id/toolbar_left_first")._click()

    driver.find_element_by_partial_link_text("交易设置")._click()
    driver.find_element_by_id("esunny.test:id/toolbar_left_first")._click()

    driver.find_element_by_partial_link_text("价格预警")._click()
    driver.find_element_by_id("esunny.test:id/toolbar_left_first")._click()

    driver.find_element_by_partial_link_text("行情登录")._click()
    driver.find_element_by_id("esunny.test:id/toolbar_left_first")._click()
