import requests
from bs4 import BeautifulSoup
import lxml

'''访问登录页面，获取authentication'''

r1 = requests.get(
    url='https://github.com/login',
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
)

c1 = r1.cookies.get_dict()
# print(r1.text)
# print(c1)
soup1 = BeautifulSoup(r1.text, features='lxml')
tag = soup1.find(name='input', attrs={'name': 'authenticity_token'})
authentication = tag.get('value')
# print(authentication)

r1.close()

form_data = {
    'commit': 'Sign in',
    'utf8': '',
    'authenticity_token': authentication,
    'login': 'mxn2013@gmail.com',
    'password': 'ningAImama123'

}
r2 = requests.post(
    url='https://github.com/session',
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
    data=form_data,
    cookies=c1
)

c2 = r2.cookies.get_dict()
c1.update(c2)

# print(r2.text)


i3 = requests.get(
    url='https://github.com/settings/repositories',
    cookies=c1,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
)
soup3 = BeautifulSoup(i3.text, features='lxml')

list_group = soup3.find(name='div', class_='listgroup')
#
# print(i3.text)

from bs4.element import Tag

if list_group:
    for child in list_group.children:
        if isinstance(child, Tag):
            project_tag = child.find(name='a', class_='mr-1')
            size_tag = child.find(name='span', class_='text-small')
            temp = "项目：%s(%s)， 项目路径：%s" % (
            project_tag.get('href'), size_tag.string, project_tag.string)
            # print(temp)



#way2

session = requests.Session()
r1 = session.get(
    url='https://github.com/login',
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
)
soup1 = BeautifulSoup(r1.text, features='lxml')
tag = soup1.find(name='input', attrs={'name': 'authenticity_token'})
authentication = tag.get('value')
form_data = {
    'commit': 'Sign in',
    'utf8': '',
    'authenticity_token': authentication,
    'login': 'mxn2013@gmail.com',
    'password': 'ningAImama123'

}
c1 = r1.cookies.get_dict()
# print(session.cookies.get_dict())

r2 = session.post(
    url='https://github.com/session',
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
    data=form_data,
)

# print(session.cookies.get_dict())
# # print(c1)
#
# c2 = r2.cookies.get_dict()
# # print(c2)
# c1.update(c2)
#
# # print(c1)
# # print(c2)



i3 = session.get(
    url='https://github.com/settings/repositories',
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'},
)

# print(i3.text)
soup3 = BeautifulSoup(i3.text, features='lxml')

list_group = soup3.find(name='div', class_='listgroup')
#
# print(i3.text)

from bs4.element import Tag

if list_group:
    for child in list_group.children:
        if isinstance(child, Tag):
            project_tag = child.find(name='a', class_='mr-1')
            size_tag = child.find(name='span', class_='text-small')
            temp = "项目：%s(%s)， 项目路径：%s" % (
            project_tag.get('href'), size_tag.string, project_tag.string)
            print(temp)