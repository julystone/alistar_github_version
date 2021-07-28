from src.test.scripts.page.navigate._NavigateBasePage import NavigateBasePage
# file_path = DATA_DIR + r"/TestData.xlsx"
# sheet_name = 'Login'
# wb = ReadExcel(file_path, sheet_name)
# cases = wb.read_data_obj()
from src.test.scripts.page.interface.RightToolBar import RightToolBar


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
