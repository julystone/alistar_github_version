import requests
from requests.sessions import Session

from src.test.scripts.framework.MyLogger import my_log


class HttpRequestNoCookie:
    def __init__(self):
        pass

    def request(self, method, url, data=None, params=None, json=None, headers=None, cookies=None, timeout=None):
        if method.lower() == 'get':
            my_log.info(f'Sending {method}:{url} {params}')
            res = requests.get(url=url, params=params, headers=headers, cookies=cookies, timeout=timeout)
        elif method.lower() == 'post':
            if json:
                my_log.info(f'Sending {method}:{url} {json}')
                res = requests.post(url=url, json=json, headers=headers, cookies=cookies, timeout=timeout)
            else:
                my_log.info(f'Sending {method}:{url} {data}')
                res = requests.post(url=url, data=data, headers=headers, cookies=cookies, timeout=timeout)
        else:
            res = None
        if res.status_code == 404:
            my_log.error(f'404 not found!')
            raise RuntimeError
        return res.text


class HttpRequest:
    def __init__(self):
        self.session = Session()

    def __del__(self):
        self.session.close()

    def request(self, method, url, data=None, params=None, json=None, headers=None, cookies=None, files=None,
                timeout=None):
        if method.lower() == 'get':
            my_log.info(f'Sending {method}:{url} {params}')
            res = self.session.get(url=url, params=params, headers=headers, cookies=cookies, files=files,
                                   timeout=timeout)
        elif method.lower() == 'post':
            if json:
                my_log.info(f'Sending {method}:{url} {json}')
                res = self.session.post(url=url, json=json, headers=headers, cookies=cookies, files=files,
                                        timeout=timeout)
            else:
                my_log.info(f'Sending {method}:{url} {data}')
                res = self.session.post(url=url, data=data, headers=headers, cookies=cookies, files=files,
                                        timeout=timeout)
        else:
            res = None
        if res.status_code == 404:
            my_log.error(f'404 not found!')
            print('404 not found!')
            raise RuntimeError
        return res.text

    def close(self):
        self.session.close()


http_request = HttpRequest()
http_request_no_cookie = HttpRequestNoCookie()

if __name__ == '__main__':
    r = HttpRequest()
    login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"

    login_data = {"mobilephone": "15567678989", "pwd": "123qwe"}
    # 登录
    r.request(method='post', url=login_url, data=login_data)
    # 充值
    rech_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
    # 构建充值的参数
    data = {"mobilephone": "15567678989", "amount": 100}
    response = r.request(method='post', url=rech_url, data=data)
    print(response.text)
