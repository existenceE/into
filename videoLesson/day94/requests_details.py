# #
# #
# # #https://www.cnblogs.com/wupeiqi/articles/6283017.html
# #
# # import requests
# #
# # requests.get()
# # requests.post()
# # requests.put()
# # requests.delete()
# #
# #
# # requests.request(
# #     'POST'...
# # )
# #
# #
# # requests.request()
# # - method: 提交方式
# # - url:   提交地址
# # -params:  在URL中传递的参数，GET http://www.oldboyedu.com
# #     params = {'k1': 'v1', 'k2': 'v2'}
# #
# # -data: 请求体里传递的数据，可以是字典 字节 文件对象
# #
# # requests.request(
# #     method='POST',
# #     url='http://www.oldboyedu.com',
# #     params={'k1':'v1','k2':'v2'},
# #     data={'user':'alex', 'pwd':123, 'x':[1,2,3,4]} #不能是字典，不处理字典value
# # )
# #
# # requests.request(
# #     method='POST',
# #     url='http://www.oldboyedu.com',
# #     params={'k1':'v1','k2':'v2'},
# #     data="user=elex&pwd=123321"
# # )
# #
# # - json 也是在请求体内传递数据，变成整体字符串 会dumps
# #
# # requests.request(
# #     method='POST',
# #     url='http://www.oldboyedu.com',
# #     params={'k1':'v1','k2':'v2'},
# #     json={'user':'alex', 'pwd':123} #"{'user':'alex', 'pwd':123}" 字典嵌套字典
# # )
# #
# #
# # - headers 请求头
# # #上次访问的网址是我的地址，才允许你登录 referer
# # requests.request(
# #     method='POST',
# #     url='http://www.oldboyedu.com',
# #     params={'k1':'v1','k2':'v2'},
# #     json={'user':'alex', 'pwd':123}, #"{'user':'alex', 'pwd':123}" 字典嵌套字典
# #     headers = {
# #         'Referer': 'http://dig.chouti.com',
# #         'User-Agent': 'https://dig.chouti.com/',
# #     },
# #     files = {
# #         'f1': open('s1.py', 'rb'),
# #         'f2': ('11111.py', open('s1.py', 'rb')),
# #     },
# #     proxies = {
# #         'http': 'http://2.3.4.1:8099'
# #     }
# # )
# #
# # - cookies Cookies
# # #放在Header里发过去的 请求头
# # #以上必须背会
# #
# # -files 上传文件
# # -auth 基本认知（headers中加密的用户名和密码
# # -timeout 请求和响应超时时间
# # - allow_redirects 是否允许重定向
# # -proxies 代理
# #
# # - stream 流，发送文件后是否立即拿回结果。一点点下载 一点点保存。如果False 一点点下载。如果True，立即下载
# #
# # - cert='***.pem'
# # - cert=('fuck.crt', 'xxx.key') 证书文件
# # - verify=False 忽略证书存在
# #
# # -session 用户保存客户端历史访问信息
# #
# #
# #
# #
# # - beautifulsoup 将html结构化
# #
# #
# # soup.select("#link2")
# from bs4 import BeautifulSoup
#
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
#     <a href="http://www.aaa.com">ddsdsad</a>
#     <a id='i1'>ddsdsad</a>
# </body>
# </html>
# """
#
# soup = BeautifulSoup(html_doc, features="lxml")
# tag = soup.find('a')
# print(tag)
# tag.name
# tag.attrs  #字典类型 包含标签所有属性
# print(tag.attrs)
# tag.attrs['lover'] = 'Physics'  #给标签增加属性 该的知识对象
# print(soup)
# del tag.attrs['href']
#
# print(soup)
#
# tags = soup.find('body').children #也拿到换行 换行是字符串类型 标签和内容不一样的类型
# print(tags)
# print(list(tags)) #内部迭代
#
# #过滤标签
# from bs4.element import Tag
# for tag in tags:
#     if type(tag) == Tag:
#         print(tag, type(tag))
#     else:
#         print('文本')
#
# print('aaaaaaaaaaaaaaaaaaaaa')
# #descendants 后代
# soup.find('body').clear() #将所有子标签全部清空，保留标签名
# print(soup)
#
# tag.encode()  把对象转成字节类型
# tag.decode()  把对象转成字符串类型
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
