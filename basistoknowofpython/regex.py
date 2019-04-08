import re
content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
print(result.group())  #匹配到的内容
print(result.span())    #匹配到的位置范围


res2 = re.match('^Hello\s(\d+)\s(\d+)\sWorld', content)
print(res2)
print(res2.group())
print(res2.group(0))
print(res2.group(2))
print(res2.span())


#.* 匹配任意字符（除换行符）无限次，不用挨个字符匹配

res3 = re.match('^Hello.*Demo$', content)
print(res3)
print(res3.group())
print(res3.span())

#.*? 懒惰匹配 匹配尽可能少的字符，与.*相对应
res4 = re.match('^He.*?(\d+).*Demo$', content)
print(res4)
print(res4.group(1))





content1 = '''Hello 1234567 World_This
is a Regex
 Demo
'''

#.匹配除了换行符意外的任何字符，遇到换行符就无法匹配。加修饰符re.S可以修正错误
# re.I 使匹配对于大小写不敏感
# re.L 本地化识别
# re.M 多行匹配，影响^$
res5 = re.match('^He.*?(\d+).*?Demo$', content1, re.S)
print(res5.group(1))

#转义匹配
content2 = '(百度)www.baidu.com'
res6 = re.match('\(百度\)www\.baidu\.com', content2)
print(res6)

#match()是从字符串开头开始匹配的，一旦开头不匹配，那么整个匹配就会失败
#对应的是search(),返回匹配的第一个内容

html = '''<div id="songs-list">
 <h2 class="title">经典老歌</h2>
 <p class="introduction">
 经典老歌列表
 </p>
 <ul id="list" class="list-group">
 <li data-view="2">一路上有你</li>
 <li data-view="7">
 <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
 </li>
 <li data-view="4" class="active">
 <a href="/3.mp3" singer="齐秦">往事随风</a>
 </li>
 <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
 <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
 <li data-view="5">
 <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
 </li>
 </ul>
</div>'''

res7 = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# 有代码换行，第三个参数需要传入re.S
if res7:
    print(res7.group(1), res7.group(2))


#findall()返回匹配的所有内容,如果有返回结果会是列表内容
res8 = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(res8)
print(type(res8))
for r in res8:
    print(r)
    print(r[0], r[1], r[2])

#sub()修改文本
content3 = '54aKS4yrsoiRS4ixSL2g'
content3 = re.sub('\d+', '',  content3)
print(content3)

print("*****************************8")
html2 = re.sub('<a.*?>|</a>', '', html)
print(html2)
res9 = re.findall('<li.*?>(.*?)</li>', html2, re.S)
for r in res9:
    print(r)
    print(r.strip())


# compile将正则字符串编译成正则表达式对象，以便在后面的匹配中复用
content4 = '2016-12-15 12:00'
content5 = '2016-12-17 12:55'
content6 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
res10 = re.sub(pattern, '', content4)
res11 = re.sub(pattern, '', content5)
res12 = re.sub(pattern, '', content6)
print(res10, res11, res12)




















