import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

r1 = requests.post('http://httpbin.org/post')
r2 = requests.put('http://httpbin.org/put')
r3 = requests.delete('http://httpbin.org/delete')
r4 = requests.head('http://httpbin.org/get')
r5 = requests.options('http://httpbin.org/get')


r6 = requests.get('http://httpbin.org/get')
print(r6.text)


data = {
    'name': 'germey',
    'age': 22
}
r7 = requests.get('http://httpbin.org/get', params=data)
print(r7.text) #返回结果为json格式

r8 = requests.get('http://httpbin.org/get')
print(type(r8.text))
print(r8.json())
print(type(r8.json()))  #将返回结果是json格式的字符串转化为字典


import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/52.0.2743.116 Safari/537.36'
}
r9 = requests.get("https://www.zhihu.com/explore", headers = headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r9.text)
print(titles)


rA = requests.get('https://github.com/favicon.ico')
# print(rA.text)
# print(rA.content)

#wb代表以二进制写的形式打开，可以向文件里写入二进制数据
#图片、音频、视频文件都可以用这种方法获取
with open('favicon.ico', 'wb') as f:
    f.write(rA.content)

data1 = {'name': 'germey', 'age': '22'}
rB = requests.post('http://httpbin.org/post', data=data)
print(rB.text) #展现在form部分
print(rB.status_code, rB.headers, rB.cookies, rB.url, rB.history)
exit() if not rB.status_code == requests.codes.ok else print('Request Successfully')






























