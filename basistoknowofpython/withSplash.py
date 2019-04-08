import requests
# url = 'http://localhost:8050/render.png?url=https://www.jd.com&wait=5&width=1000&height=700'
# response = requests.get(url)
# with open('taobao.png', 'wb') as f:
#     f.write(response.content)

from urllib.parse import quote
# lua = '''
# function main(splash)
#     return 'hello'
# end
# '''
#
# url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
# response = requests.get(url)
# print(response.text)


lua = '''
function main(splash, args)
    local treat = require("treat")
    local response = splash:http_get("http://httpbin.org/get")
        return {
            html = treat.as_string(response.body),
            url = response.url,
            status = response.status
        }
end
'''
url = 'http://localhost:8050/execute?lua_source=' + quote(lua)
response = requests.get(url)
print(response.text)

#负载均衡
























