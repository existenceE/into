import requests

r1 = requests.get('http://dig.chouti.com/', headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})
r1_cookies = r1.cookies.get_dict()
print(r1.cookies.get_dict())

post_dict = {
    'phone': '8618305185915',
    'password': '111111',
    'oneMonth': 1
}
r2 = requests.post(
    url='https://dig.chouti.com/login',
    data=post_dict,  # Form Data
    cookies =r1_cookies,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
)
r2_cookies = r2.cookies.get_dict()
print(r2.cookies.get_dict())


r3 = requests.post(
    url='https://dig.chouti.com/link/vote?linksId=25104426',
    cookies={'gpsd': r1_cookies['gpsd']},
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
)
print(r3.text)


session = requests.Session()
#首先登陆任何页面 获取cookie
i1 = session.get(url='http://dig.chouti.com/help/service')
#### 2、用户登陆，携带上一次的cookie，后台对cookie中的 gpsd 进行授权
i2 = session.post(
    url='http://dig.chouti.com/login',
    data={
        'phone': '',
        'password': '',
        'oneMonth': ''
    }
)

i3 = session.post(
    url='http://dig.chouti.com/link/vote?linksId=3123213',
)

print(i3.text)




