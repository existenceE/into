import requests

# 模拟自动登录
# 点登录看页面是否刷新，没刷新是ajax提交

post_dict = {
    'phone': '8618305185915',
    'password': '111111',
    'oneMonth': 1
}

response = requests.post(
    url='https://dig.chouti.com/login',
    data=post_dict,   #Form Data
    headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

)

print(response.text)  #文本信息
print(response.cookies) #对象
cookie_dict = response.cookies.get_dict()


response = requests.get(
    url='http://dig.chouti.com/profile',
    cookies = cookie_dict,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
)
print(response.text)