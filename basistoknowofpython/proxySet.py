#
#
# #urllib
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# # proxy = '104.160.40.40:10388' 'username:password@ip:port'
# proxy = '1.196.160.90:9999'
# proxy_handler = ProxyHandler({
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('http://httpbin.org/get')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)



#requests

# import requests
# proxy = '1.196.160.90:9999'
# proxies = {
#     'http': 'http://' + proxy,
#     'https': 'https://' + proxy,
# }
# try:
#     response = requests.get('http://httpbin.org/get', proxies=proxies)
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print('Error', e.args)


# selenium + chrome
from selenium import webdriver

proxy = '1.196.160.90:9999'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://' + proxy)
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://httpbin.org/get')









