from src.test.scripts.page.interface.RightToolBar import RightToolBar
from src.test.scripts.page.navigate._NavigateBasePage import NavigateBasePage


def click_circle():
    NavigateBasePage().goToRightToolBar().goToQuoteLoginPage().quoteLoginCommon(user_no='JULY402', password='qqqq1111@')
    RightToolBar().goToCloudServicePage().logOut()


if __name__ == '__main__':
    time = 0
    try:
        for _ in range(100):
            click_circle()
            time += 1
    except:
        print(time)
