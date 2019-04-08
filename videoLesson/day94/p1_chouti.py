# 自动登录
import requests
from bs4 import BeautifulSoup

# 抽屉  WAY 1

# get_headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
# }
#
# r1 = requests.get(
#     url='http://dig.chouti.com/help/service',
#     headers=get_headers,
# )
# c1 = r1.cookies.get_dict()
# # print(r1.text)
# # print(r1.cookies)
# print(c1)

# post_headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
# }
#
# post_data = {
#     'phone': '8618305185915',
#     'password': '111111',
#     'oneMonth': 1
# }
#
# r2 = requests.post(
#     url='https://dig.chouti.com/login',
#     data=post_data,
#     headers=post_headers,
#     cookies=c1,
# )
#
# c2 = r2.cookies.get_dict()
# # print(r2.text)
# # print(c2)
#
# gpsd = c1['gpsd']
#
# r3 = requests.post(
#     url='https://dig.chouti.com/link/vote?linksId=25109751',
#     cookies={'gpsd':gpsd},
#     headers=post_headers,
# )
#
# print(r3.text)



post_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}
post_data = {
    'phone': '8618305185915',
    'password': '111111',
    'oneMonth': 1
}

# 抽屉 WAY2

import requests
session = requests.Session()
i1 = session.get(url='http://dig.chouti.com/help/service', headers=post_headers,)
i2 = session.post(
    url='https://dig.chouti.com/login',
    data = post_data,
    headers=post_headers,
)

i3 = session.post(
    url='https://dig.chouti.com/link/vote?linksId=25109751',
    headers=post_headers,
)
print(i3.text)


















