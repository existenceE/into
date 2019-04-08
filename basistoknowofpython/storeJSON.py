#通过对象和数组的组合来表示数据，构造简洁但是结构化程度非常高
#是一种轻量级的数据交换格式


import json
#json的数据需要用双引号包围，不能用单引号
str='''
[{
    "name": "Bob",
    "gender":"male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''

print(type(str)) #str
data = json.loads(str)
print(data)
print(type(data))  #list

#这样就可以用索引来获取对应的内容，索引，键名
print(data[0]['name'])
print(data[0].get('name')) #推荐 如果键名不存在，不会报错，返回None

# 从json文本中读取内容，先读出，再用loads转化
# with open('data.json', r) as f:
#     str = f.read()
#     data = json.loads(str)
#     print(data)


import json
data = [{
    'name': 'Bob哈哈哈',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
with open('data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, indent=2, ensure_ascii=False)) #indent代表缩进字符个数，格式清晰
































