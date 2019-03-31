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

#响应 我们使用text和conten获取响应的内容
# import requests
# r = requests.get('http://www.jianshu.com')
# print(type(r.status_code), r.status_code)
# print(type(r.headers), r.headers)
# print(type(r.url), r.url)
# print(type(r.history), r.history)
#requests提供了一个内置状态查询码

# import requests
# r = requests.get('http://www.jianshu.com')
# if not r.status_code == requests.codes.ok else print(
#     'Rquests Successfully')

#requests高级用法,文件上传，Cookies设置，代理设置
#文件上传 模拟文件上传过程
# import requests

# files = {'file': open('favico.ico', 'rb')}
# r = requests.post('http://httpbin.org/post', files=files)
# print(r.text)

#requests 处理Cookies
# import requests
# r = requests.get('https://www.baidu.com')
# print(r.cookies)                          #RequestCookieJar类型
# for key, value in r.cookies.items():         #item()转换为元组组成的列表
#     print(key + '=' + value)

#用Cookie来维持登录状态
# import reuqests
# headers={
#     'Cookie':''
# }
# r=requests.get('https://zhihu.com',headers=headers)
# print(text)
#通过构造cookies参数来设置
# import requests
# cookies=''
# jar=requests.cookies.RequestsCookieJar()
# headers={
#     'Host':'www.zhihu.com',
#     'User-Agent':''
# }
# for cookie in cookies.split(';'):
#     key,value=cookie.split('=',1)
#     jar.set(key,value)
# r=reuqests.get('http://www.zhihu.com',cookies=jar,headers=headers)

#会话维持 Session对象
# import requests
# s=requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r=s.get('http://httpbin.org/cookies')
# print(r.text)

#证书验证 verify参数控制是否检查此证书，不假verify参数的话，默认是True,自动检测
# import requests

# response=requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)

#通过设置忽略警告的方式来屏蔽这个警告
# import requests
# from requests.packages import urllib3
# urllib3.disable_warnings()
# response=requests.get('https://www.12306.cn',verify=False)
# print(response.status_code)
# #通过捕获警告到日志的方式忽略警告
# import logging
# import requests
# logging.captureWarnings(True)
# response=requests.get('https://www,12306.cn',verify=False)
# print(response.status_code)

#代理设置 proxies参数  代理需要换成自己的
# import requests
# proxies={
#     'http':'http://10.10.1.10:3128',
#     'https':'http://10.10.1.10:1080',
# }
# requests.get('https://www.taobao.com',proxies=proxies)

#若代理需要HTTP Basic Auth
# import requests
# proxies = {
#     'http': 'http://user.password@10.10.1.10:3182/',
# }
# requests.get('https://www.taobao.com', proxies=proxies)

#requests还支持SOCKS协议的代理
# import requests
# proxies={
#     'http':'socks5://user:password@host:port',
#     'https':'socks5://user:password@host:port'
# }
# requests.get('https://www.taobao.com',proxies=proxies)

#超时设置
# import requests
# r = requests.get('https://www.taobao.com', timeout=1)
# print(r.status_code)

#身份认证  提供了一个HTTPBasicAuth类
# import requests
# from requests.auth import HTTPBasicAuth
# r= requests.get('http://',auth=HTTPBasicAuth('username','password'))
# print(r.status_code)
#更加优化
# import requests
# r=requests.get('http://www.',auth=('username','password'))
# print(r.status_code)
#OAuth认证

#Prepared Rquest
# from requests import Rquest,Session
# url='http://httpbin.org/post'
# data={
#     'name':'germey'
# }
# headers={
#     'User-agent':''
# }
# s=Session()
# req=Requests('POST',url,data=data,headers=headers)
# prepped=s.prepare_request(req)
# r=s.send(prepped)
# print(r.text)