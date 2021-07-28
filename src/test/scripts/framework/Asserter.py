from assertpy import assert_that


class Asserter:
    @staticmethod
    def PageHasElem(Page, elem):
        assert_that(Page.findElemWithoutException(elem)).is_not_none()

    @staticmethod
    def PageNotHasElem(Page, elem):
        assert_that(Page.findElemWithoutException(elem)).is_none()

    @staticmethod
    def PageHasText(Page, text):
        elem = Page.findElement(('part-text', str(text)))
        assert_that(elem).is_not_none()
        assert_that(Page.findElement(('part-text', str(text)))).is_not_none()

    @staticmethod
    def PageNotHasText(Page, text):
        assert_that(Page.findElement(('part-text', str(text)))).is_none()

    @staticmethod
    def TextEqualText(res, text):
        assert_that(res).is_equal_to(str(text))

    @staticmethod
    def TextContainsText(res, text):
        assert_that(res).contains(str(text))

    @staticmethod
    def _boolAdaptor(bool_str):
        if isinstance(bool_str, str):
            bool_str = eval(bool_str)
        return bool_str

    @staticmethod
    def BoolEqualBool(first, second):
        assert_that(Asserter._boolAdaptor(first) is Asserter._boolAdaptor(second)).is_true()

    @staticmethod
    def BoolNotEqualBool(first, second):
        assert_that(Asserter._boolAdaptor(first) is Asserter._boolAdaptor(second)).is_false()

    @staticmethod
    def BoolTrue(expr):
        assert_that(expr).is_true()