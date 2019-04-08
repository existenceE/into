
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.autohome.com.cn/news/')
response.encoding = response.apparent_encoding
# print(response.text)


soup = BeautifulSoup(response.text, 'html.parser')  #将文本转化为对象  内置的引擎。 生产中lxml性能更好
target = soup.find(id='auto-channel-lazyload-article')
li_list = target.find_all('li')  #是列表类型，没有find方法，可以按照索引获取
for i in li_list:
    a = i.find('a')
    if a:
        print(a.attrs.get('href'))
        txt = a.find('h3').text  #字符串类型 去对象里拿文本
        print(txt)
        img_url = a.find('img').attrs.get('src')[2:]
        img_url = 'http://' + img_url
        img_response = requests.get(img_url)
        import uuid
        file_name = str(uuid.uuid4()) + '.jpg'

        with open(file_name, 'wb') as f:
            f.write(img_response.content)











# import requests
#
# url = 'https://m.weibo.cn/'
# response = requests.get(url)
# # print(response)
# # print(type(response))  # <class 'requests.models.Response'>
# # # print(response.text)
# # print('response.content: ', response.content)
# # print('response.encoding: ', response.encoding)
# # print('response.apparent_encoding: ', response.apparent_encoding)
# # print('response.status_code: ', response.status_code)
#
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(response.text, features='html.parser')  字符串，处理引擎  soup为对象，嵌套层级 用点
# #target = soup.find(name='f')  # 无法查找？？？？？？
# target = soup.find('div')
# print('soup: ',soup)
# print('type of soup', type(soup))
# print("target: ", target)
#
# v1 = target.find('div')
# v2 = target.find_all('a')
# print('find(): ', v1)
# print('find() type : ', type(v1))
# print('find_all(): ', v2)
# print('find_all() type : ', type(v2))  #是列表，哪怕只有一个结果也是列表形式
#
# print('v1.text', v1.text)
# for i in v2:
#     print('i.text', i.text)
#
# print('v1.attrs', v1.attrs)
# for i in v2:
#     print('i.attrs', i.attrs)
#     print(i.attrs.get('href'))











