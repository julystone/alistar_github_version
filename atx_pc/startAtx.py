import uiautomator2 as u2

d = u2.connect() # connect to device
print(d.info)

d.app_start(package_name='esunny.test', activity='com.esunny.estar.StartActivity')
d.sleep(5)
# d.watch_context().when('日志上传').when('否').click()
print(d(text='小道指2107').exists())
# d.app_stop(package_name='esunny.test')
