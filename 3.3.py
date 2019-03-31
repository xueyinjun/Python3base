#encoding=utf-8
#正则表达式

# \w 匹配字母，数字及下划线
# match()用法 向它传入要匹配的字符串以及正则表达式，就可以检测这个正则表达式是否匹配字符串
# match()第一个参数传入正则表达式，第二个参数传入了要匹配的字符串
# match()尝试从字符串起始位置匹配正则表达式

#Example1

# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# print(len(content))
# result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
# print(result)
# print(result.group())
# print(result.span())

#SRE_Match对象有两个方法
#group()方法可以输出匹配到的内容
#span()方法可以输出匹配的范围

#匹配目标，使用()括号将想提取的子字符串括起来，调用group()方法传入分组的索引即可获取提取的结果
#Example2

# import re
# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())

#通用匹配  .*
#Example3

# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello.*Demo$', content)
# print(result)
# print(result.group())
# print(result.span())

#贪婪非贪婪
#Example4 贪婪  .*会匹配尽可能多的字符
# import re
# content = 'Hello 1234567 World_This is Regex Demo'
# result = re.match('^He.*(\d+).*Demo$', content)
# print(result)
# print(result.group(1))

#非贪婪模式  写法.*?尽可能匹配较少的字符
# import re
# content = 'Hello 1234567 World This is a Regex Demo'
# result = re.match('^He.*?(\d+).*Demo$',content)
# print(result)
# print(result.group(1))

#Example4
#注意，如果匹配的结果在字符串结尾,.*? 就有可能匹配不到任何内容了，因为它会匹配尽可能少的字符

# import re
# content = 'http://weibo.com/comment/kEraCN'
# result1 = re.match('http.*?comment/(.*?)',content)
# result2 = re.match('http.*?comment/(.*)',content)
# print('result1',result1.group(1))
# print('result2',result2.group(1))

#修饰符
#Example5  修饰符re.S 作用是使.匹配包括换行符在内的所有字符
# import re
# content = '''Hello 1234567 World_This
# is a Regex Demo'''
# result = re.match('^He.*?(\d+).*?Demo$', content, re.S)
# print(result.group(1))

#转义匹配 \反斜线
#Example6
# import re
# content = '(百度)www.baidu.com'
# result = re.match('\(百度\)www\.baidu\.com', content)
# print(result)
# print(result.span())
# print(result.group())

#search() 它在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果
#Example6
# import re
# content = 'Extra stings Hello 12345567 World_This is a Regex Demo Extra stings'
# result = re.search('Hello.*?(\d+).*?Demo', content)
# print(result)
# print(result.span())
# print(result.group())

#Examle7 search()方法应用
# import re
# html = '''<div id="songs-list" >
# <h2 class="title"〉经典老歌</h2>
# <p class="introduction">
# 经典老歌列表
# </p>
# <ul id="list" class="list-group">
# <li data-view="2"〉一路上有你</li>
# <li data-view="7">
# <a href="/2.mp3" singer="任贤">沧海一声笑</a>
# </li>
# <li data-view="4" class="active">
# <a href="/3 .mp3" singer="齐秦">往事随风</a>
# </li>
# <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月 </a></li>
# <li data-view="5"><a href="/5.mp3" singer=“陈慧琳“>记事本</a></li>
# <li data-view="5">
# <a href="/6.mp3" singer="邓丽君、但愿人长久" </a>
# </li>
# </ul>
# </div>'''
#Version1 有active定位
# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# if result:
#     print(result.group(1),result.group(2))

#Version2  没有active 定位
# result = re.search('<li.*?singer=“(.*?)“>(.*?)</a>', html, re.S)
# if result:
#     print(result.group(1), result.group(2))

#Example8
#findall()用法,会搜索整个字符串，然后返回匹配正则表达式的所有内容
# 获取所有a节点的超链接，歌手和歌名
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">*(.*?)</a>', html,
#                      re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result)
#     print(result[0], result[1], result[2])

#sub() 修改文本,第一个参数是要匹配的正则，第二个参数是要替换的字符串，第三个是原有字符串
#Example9
# import re
# content = '5a46KDSF0FK3WEYk7dfj6dkf9sd'
# content = re.sub('\d+', '', content)
# print(content)

#Example10 获取所有li节点的歌名 version1
# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
# for result in results:
#     print(result[1])

#Example11  version2 用sub()去除<a>
# html = re.sub('<a.*?>|</a>', '', html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>', html, re.S)
# for result in results:
#     print(result.strip())

#compile()方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用
#Example12
# import re
# content1 = '2016-12-15 12:00'
# content2 = '2016-12-17 12:55'
# content3 = '2016-12-22 13:21'
# pattern = re.compile('\d{2};\d{2}')
# result1 = re.sub(pattern, '', content1)
# result2 = re.sub(pattern, '', content2)
# result3 = re.sub(pattern, '', content3)
# print(result1, result2, result3)
