#encoding=utf-8

#requests以GET方法请求网页，相应的方法get()方法 get()方法实现与urlopen()相同的操作，得到一个Response对象

# import requests
# r = requests.get('http://www.baidu.com/')
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)r
# import requests
# r=requests.post('http://httpbin.org/post') 实现了POST请求
# r=requests.put('http://httpbin.org/put') 实现了PUT请求
# r=requests.delete('http://httpbin.org.delete') 实现了DELETE请求
# r=requests.head('http://httpbin.org/get')
# r=requests.options('http://httpbin.org/get')

#GET请求
# import requests
# r=requests.get('http://httpbin.org/get')
# print(r.text)
#GET请求附加额外的信息
#方式一 直接写入参数
# import requests
# re=requests.get('http://httpbin.org/get?name=germey&age=22')
# print(re.text)
#方式二 这种信息数据用字典来存储
# import requests
# data={
#     'name':'germey',
#     'age':22
# }
# r=requests.get('http://httpbin.org/get',params=data)
# print(r.text)
# 网页返回类型实际上是str类型，但是它是JSON格式的，如果想直接解析返回结果，得到一个字典格式用json()方法
#json()方法,就可以将返回结果是JSON格式的字符串转化为字典
# import requests
# r = requests.get('http://httpbin.org/get')
# print(type(r.text))
# print(r.json())
# print(type(r.json()))

# Requests.get()方法加入headers 包好User-agent字段信息，也就是浏览器标识信息，
# import requests
# import re
# headers = {
#     'User-Agent':
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'
# }
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles = re.findall(pattern, r.text)
# print(titles)
#学习正则表达式

#抓取二进制数据  图像、音频、视频这些文件本质上都是由二进制码组成的，由于有特定的保存格式和对应的解析方式
# import requests
# r = requests.get('https://github.com/favicon.ico')
# print(r.text) #转化为str类型会乱码
# print(r.content) #bytes类型的数据

#将提取到的图片保存下来 用了open()方法 第一个参数是文件名，第二个参数代表二进制写的形式，音频和视频文件也可以用这种方法获取
# import requests
# r = requests.get('https://github.com/favicon.ico')
# with open('favico.ico', 'wb') as f:
#     f.write(r.content)

#POST请求方式
# import requests
# data={'name':'germey','age':'22'}
# r=requests.post('http://httpbin.org/post',data=data)
# print(r.text)