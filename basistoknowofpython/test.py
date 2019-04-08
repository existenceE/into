import re

# match从开头匹配，一旦开头不匹配，整个匹配失败
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# print(result)
# print(result.group())
# print(result.span())

#
# #
# # # 从字符串提取一部分内容，用括号
# # content = 'Hello 1234567 World_This is a Regex Demo'
# # result = re.match('^Hello\s(\d+)\sWorld', content)
# # print(result)
# # print(result.group())
# # print(result.group(0))
# # print(result.group(1))
# # print(result.span())
#
# # 改写
#
# content = 'Hello 123 4567 World_This is a Regex Demo'
# # print(len(content))
# # result = re.match('^Hello.*Demo$', content)
# # print(result)
# # print(result.group())
# # print(result.span())
#
#
# result = re.match('^He.*?(\d+).*Demo$', content)
# print(result)
# print(result.group(1))
#
# result = re.match('^He.*?\d+(.*?)Demo$', content)
#
# print(result)
# print(result.group(1))
#
#
# # 加上re.S 使得匹配换行符在内的所有字符
# # re.I re.L re.M re.S re.U re.X
#
#
# # search() 扫描整个字符串，返回第一个成功匹配的结果。
#
#
#



s
















