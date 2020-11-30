from selenium.common.exceptions import NoSuchElementException


def isElementPresent(driver, loc):
    try:
        element = driver._find_element(*loc)
    except NoSuchElementException as e:
        print(e)
        raise AssertionError