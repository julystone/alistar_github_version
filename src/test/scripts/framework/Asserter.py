from src.test.scripts.framework.Driver_atx import Driver


def shouldElemExist(elem):
    assert Driver().check_element_exist(elem) is True


def notElemExist(elem):
    # 深层次设置页面跳转，而且是线性设置，需要用到notExist
    assert Driver().check_element_exist(elem) is False


def shouldHaveText(text):
    assert Driver().check_element_exist(('part-text', text)) is True


def shouldTextEqual(res, text):
    assert res == text


def notHaveText(text):
    assert Driver().check_element_exist(('part-text', text)) is False


def waitUntilText(text):
    assert Driver().getDriver().wai
