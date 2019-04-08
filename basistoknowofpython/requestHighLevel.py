# import requests
#
# # 文件上传
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)
#
# r1 = requests.get('https://www.baidu.com')
# print(r1.cookies)
# for key, value in r1.cookies.items():
#     print(key + '=' + value)
#
# headers = {
#     'cookie': '_ga=GA1.2.1271772458.1494503606; _zap=a5bd5b8f-1679-4f59-acef-f4f83240c921; d_c0="AEACm5Dv6QuPTh21xQygArT9JCTB4ulNahQ=|1497457726"; q_c1=f70363e440be4753bdd743b41629f986|1506138057000|1492611214000; __DAYU_PP=QYY6j6VQi7eAiURuVyiJ69732d8ba556; __utmz=51854390.1538470801.17.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _xsrf=796b8ca1-4ae7-41b9-a28a-ba82eb542054; l_n_c=1; q_c1=f70363e440be4753bdd743b41629f986|1550830838000|1492611214000; r_cap_id="MmExNGE1ZmEzYTU3NDY2YjlhNzkzMzU4YTE1OGVkOTQ=|1550830838|84e1614b43d1b0b9e4d9abb20afe94f2fef6f05d"; cap_id="MzY2NTI3MDg0ODEyNGI3YjkxMzQ2Y2Q4YTE0ZDc4MGE=|1550830837|c102779c6aa38e58f56f3a6729a87a3e3d7d10bf"; l_cap_id="Nzc5Y2I5N2FhNTM2NDBmZDk5ODg1ZGRjYjRkYjNhNWY=|1550830838|3c6b26edffa3c9180ec129251d9600934c1b151a"; n_c=1; __utma=51854390.1271772458.1494503606.1538470801.1550830841.18; __utmc=51854390; tst=r; __utmv=51854390.100--|2=registration_date=20130122=1^3=entry_date=20130122=1; tgw_l7_route=8ffa4a0b7ecd9bdb5ad19b8c1037b063; capsion_ticket="2|1:0|10:1550880831|14:capsion_ticket|44:ZjI0NmUwMDI5MzRlNGI1OTllYTljNmM4MzEzNDdlNzE=|e244d175e9f7a3cf763b5e729008641c45f1ccbb8e44a591f9395af073323bc6"; z_c0="2|1:0|10:1550880838|4:z_c0|92:Mi4xRExjSEFBQUFBQUFBUUFLYmtPX3BDeVlBQUFCZ0FsVk5SdDVkWFFDNEstN0lwSnBRQ3huT2dxVlk0YkhXb254bGN3|6bdc96af693978dab5dc3e52ac1348573b92d5b3eada7cfbc22fcbf20351ca5c"',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
# }
#
# r3 = requests.get('https://www.zhihu.com', headers = headers)
# print(r3.text)
#
#
# cookies = '_ga=GA1.2.1271772458.1494503606; _zap=a5bd5b8f-1679-4f59-acef-f4f83240c921; d_c0="AEACm5Dv6QuPTh21xQygArT9JCTB4ulNahQ=|1497457726"; q_c1=f70363e440be4753bdd743b41629f986|1506138057000|1492611214000; __DAYU_PP=QYY6j6VQi7eAiURuVyiJ69732d8ba556; __utmz=51854390.1538470801.17.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _xsrf=796b8ca1-4ae7-41b9-a28a-ba82eb542054; l_n_c=1; q_c1=f70363e440be4753bdd743b41629f986|1550830838000|1492611214000; r_cap_id="MmExNGE1ZmEzYTU3NDY2YjlhNzkzMzU4YTE1OGVkOTQ=|1550830838|84e1614b43d1b0b9e4d9abb20afe94f2fef6f05d"; cap_id="MzY2NTI3MDg0ODEyNGI3YjkxMzQ2Y2Q4YTE0ZDc4MGE=|1550830837|c102779c6aa38e58f56f3a6729a87a3e3d7d10bf"; l_cap_id="Nzc5Y2I5N2FhNTM2NDBmZDk5ODg1ZGRjYjRkYjNhNWY=|1550830838|3c6b26edffa3c9180ec129251d9600934c1b151a"; n_c=1; __utma=51854390.1271772458.1494503606.1538470801.1550830841.18; __utmc=51854390; tst=r; __utmv=51854390.100--|2=registration_date=20130122=1^3=entry_date=20130122=1; tgw_l7_route=8ffa4a0b7ecd9bdb5ad19b8c1037b063; capsion_ticket="2|1:0|10:1550880831|14:capsion_ticket|44:ZjI0NmUwMDI5MzRlNGI1OTllYTljNmM4MzEzNDdlNzE=|e244d175e9f7a3cf763b5e729008641c45f1ccbb8e44a591f9395af073323bc6"; z_c0="2|1:0|10:1550880838|4:z_c0|92:Mi4xRExjSEFBQUFBQUFBUUFLYmtPX3BDeVlBQUFCZ0FsVk5SdDVkWFFDNEstN0lwSnBRQ3huT2dxVlk0YkhXb254bGN3|6bdc96af693978dab5dc3e52ac1348573b92d5b3eada7cfbc22fcbf20351ca5c"'
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
# }
#
# for c in cookies.split(';'):
#     key, value = c.split('=', 1)
#     jar.set(key, value)
# r4 = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)
# print(r4.text)
#
#
# import requests
# # about session
# requests.get("http://httpbin.org/cookies/set/number/123456789")
# r5 = requests.get("http://httpbin.org/cookies")
# print(r5.text)
#
#
# import requests
# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456789")
# r6 = s.get("http://httpbin.org/cookies")
# print(r6.text)
#
# #about ssl
# import requests
# from requests.packages import urllib3
#
# urllib3.disable_warnings() #忽略警告来屏蔽警告
# import logging
# logging.captureWarnings(True) # 捕获警告到日志的方式来忽略警告
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)


import requests
from requests.auth import HTTPBasicAuth

r7 = requests.get('http://www.douban.com', auth=HTTPBasicAuth('86081398@qq.com',\
                                                              'ningAImama123'))
print(r7.status_code)

#还有OAuth1认证 P137


#将请求表示为数据结构，各个参数可以通过一个Request对象来表示
#将请求当做独立的对象来看待，在进行队列调度的时候会非常方便
from requests import Request, Session
url = 'http://httpbin.org/post'
data = {
    'name': 'germey'
}
headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r8 = s.send(prepped)
print(r8.text)

















