import uiautomator2 as u2


# # d = u2.connect() # connect to device
# d = u2.connect_wifi('192.168.18.45')
# print(d.info)
#
# d.app_start(package_name='esunny.test', activity='com.esunny.estar.StartActivity', wait=True)
# # d.sleep(5)
# # d.watch_context().when('日志上传').when('否').click()
# print(d(text='小道指2107').exists())
# # d.app_stop(package_name='esunny.test')


class Driver:
    def __init__(self, addr, package_name, implicitly_time=20):
        self._d = u2.connect(addr)
        self._d.implicitly_wait(implicitly_time)
        self.windowSize = self._d.window_size()
        self.deviceInfo = self._d.device_info
        self._session = self._d.session(package_name=package_name, attach=True)

    # def __del__(self):
    #     self._session.close()

    def setDriver(self, newDriver):
        self._d = newDriver

    def getDriver(self):
        return self._d

    def appStart(self, package_name, activity, stop):
        self.getDriver().app_start(package_name=package_name, activity=activity, wait=True, stop=stop)

    def findElement(self, locator):
        via = locator[0].upper()
        if via == 'TEXT':
            return self.getDriver()(text=locator[1])
        elif via == 'PART-TEXT':
            return self.getDriver()(textContains=locator[1])
        elif via == 'RESOURCE-ID':
            return self.getDriver()(resourceId=locator[1])
        else:
            print("match rules not found")

    def click(self, locator):
        return self.findElement(locator).click()


# one = Driver('192.168.18.45')
one = Driver(addr='', package_name='esunny.test')

# one.getDriver().app_start(package_name='esunny.test', activity='com.esunny.estar.StartActivity', stop=True, wait=True)
one.getDriver().implicitly_wait(30.0)
# Driver.d
# d.watch_context().when('日志上传').when('否').click()
ttt = 'textContains'
# print(one.getDriver()(ttt='纯碱'))
# print(one.getDriver()(textContains='纯碱').click_exists(timeout=None))
print(one.getDriver().window_size())
# print(one.getDriver()(textContains='纯碱').child())
# print(one.getDriver().xpath)
# print(one.getDriver()(resourceId="esunny.test:id/es_kline_bottom_pager_view").long_click(duration=1, timeout=None))
# size = list(Driver.d.window_size())
# pattern = {"L": (3 / 4, 1 / 2, 1 / 4, 1 / 2),
#            "R": (1 / 4, 1 / 2, 3 / 4, 1 / 2),
#            "U": (1 / 2, 3 / 4, 1 / 2, 1 / 4),
#            "D": (1 / 2, 1 / 4, 1 / 2, 3 / 4)}
# params = [pattern['L'][i] * (size + size)[i] for i in range(4)]
# print(Driver.d.swipe(*params))
# print(one.getDriver().screenshot())
# print(one.getDriver().screenshot().save("./1.png"))
# print(one.getDriver().screenshot('./2.png'))
# print(one.getDriver().screenshot('./2.png').save())
