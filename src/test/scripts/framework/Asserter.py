from src.test.scripts.framework.Driver import Driver


def shouldElemExist(driver, elem):
    assert Driver.check_element_exist(driver, elem) is True


def notElemExist(driver, elem):
    # 深层次设置页面跳转，而且是线性设置，需要用到notExist
    assert Driver.check_element_exist(driver, elem) is False


def shouldHaveText(driver, text):
    assert Driver.check_element_exist(driver, ('part-text', text)) is True


def notHaveText(driver, text):
    assert Driver.check_element_exist(driver, ('part-text', text)) is False
