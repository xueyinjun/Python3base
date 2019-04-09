#encoding=utf-8
#5.1.1 文件存储,TXT文本储存,JSON文件储存，CSV文件储存
#TXT文本储存，1目标，2实例，3打开方式，4简化写法
# 特点，兼容任何平台，但是不利于检索，如果对检索和数据结构要求不高可以采用TXT存储
#1.目标：保存知乎上“发现”页面的"热门话题"部分，将其问题和答案同一保存成文本形式
#可以用requests将网页源代码获取，然后使用pyquery解析库解析，接下来提取，标题,回答者，回答保存到文本
#为了现实requests异常处理部分在此省去，用requests提取知乎的发现页面，将今日最热内容将想要的目标提取出来，然后利用Python提供的open()方法打开一个文本文件，获取一个文件操作对象，这里赋值file,接着利用file对象的write()方法将提取的内容写入文件，最后调用close()方法将其关闭
# 2 Example实例
# import requests
# from pyquery import PyQuery as pq
# url = "https://zhihu.com/explore"
# headers = {
#     'User-Agent':
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
# }
# html = requests.get(url, headers=headers).text
# doc = pq(html)
# items = doc('.explore-tab .feed-item').items()#提取目标调用items()方法变成生成器，进行遍历，注意用选择器时class属性书写的正确格式
# for item in items:
#     question = item.find('h2').text() #
#     author = item.find('.author-link-line').text()
#     answer = pq(item.find('.content').html()).text()
#     file = open('Python3cui/explore.txt','a', encoding='utf-8')#第一个参数要保存目标名，第二个参数是a，代表以追加方式写入到文本,指定编码格式
#     file.write('\n'.join([question, author, answer]))
#     file.write('\n' + '=' * 50 + '\n')
#     file.close()# 关闭文件对象
#3.打开方式
#像实例中open()方法的第二个参数设置成a,这样在每次写入文本时不会清空源文件，而是在文件末尾写入新的内容，这是一种文件打开方式
# r:以只读方式打开文件，文件的指针将会放在文件的开头，这是默认模式
# rb: 以二进制只读方式打开一个文件，文件指针将会放在文件的开头
# r+:以读写方式打开一个文件，文件指针将会放在文件的开头
# rb+ 以二进制读写方式打开一个文件，文件指针将会放在文件的开头
# w:以写入方式打开一个文件，如果该文件已存在，则将其覆盖，如果该文件不存在，则创建新文件
# wb:以二进制写入方式打开一个文件，如果该文件已存在，则将其覆盖，如果该文件不存在，则创建新文件
# w+以读写方式打开一个文件，如果该文件已存在，则将其覆盖，如果该文件不存在，则创建新文件
# wb+ 以二进制读写方式打开一个文件，如果该文件已存在，则将其覆盖，如果该文件不存在，则创建新文件
# a 以追加方式打开一个文件，如果该文件存在，文件指针将会放在文件的结尾，也就是说新的内容将会被写入已有内容之后，如果文件不存在，则创建新文件来写入
# ab 以二级制追加方式打开一个文件，如果该文件已存在，文件指针将会放在文件结尾，也就是说，新的内容将会被写入已有内容之后，如果该文件不存在，则创建新文件来写入
# a+ 以读写方式打开一个文件，如果该文件已存在，文件指针会放在文件的结尾，文件打开时会是追加模式，如果该文件不存在，则创建新文件来读写
# ab+ 以二进制追加方式打开一个文件，如果该文件已存在，则文件指针会放在文件结尾，如果该文件不存在，则创新文件用于读写
#4.简化写法
# with as 语法 在 with控制块结束时，文件会自动关闭，所以不需要再调用close()方法
#version 1
# with open('Python3cui/explore.txt','a',encoding='utf-8') as file:
#     file.write('\n'.join([question,author,answer]))
#     file.write('\n'+'='*50+'\n')
#version 2 保存时将原文清空
# with open('Python3cui/explore.txt','w',encoding='utf-8') as file:
#     file.write('\n'.join([question,author,answer]))
#     file.write('\n'+'='*50 + '\n')
#5.1.2.JSON文件存储，对象和数组，读取JSON，输出JSON
#JSON JavaScript对象标记，他通过象和数组对的组合来表示数据，构造简洁但是结构化程度非常高，是一种轻量级的数据交换格式
#1.对象和数组
#对象：使用花括号{}包裹起来的内容，数据结构为{key1:value1}键值对结构,key为对象的属性，value为对应的值，键名可以使用整数和字符串表示，值的类型可以是任意类型
#数组：方括号[]包裹起来的内容，数据结构为["java","javascript"]的索引结构，数组是一个比较特殊的数据类型，它可以像对象那样使用键值对，但是还是索引用的多，同样值得类型可以是任意类型
#Example 1 JSON对象由两种形式自由组合而成，可以无限次嵌套，结构清晰，是数据交换的极佳方式
# import json
# str = '''
# [{
#     "name": "Bob",
#     "gender": "male",
#     "birthday": "1992-10-18"
# }, {
#     "name": "Selina",
#     "gender": "female",
#     "birthday": "1995-10-18"
# }]
# '''
#2.读取JSON
#JSON库中loads()方法将JSON文本字符串转为JSON对象，可以通过dumps()方法将JSON对象转为文字字符串
#用loads()方法将字符串转为JSON对象，最外层是[]所以是列表形式
# print(type(str))
# data = json.loads(str)
# print(data)
# print(type(data))
#可以用索引来获取对应的内容
# print(data[0]['name'])
# print(data[0].get('name'))
#通过中括号加索引，得到字典元素，然后再调用其键名可得到相应的键值，获取键值的方式有两种，一种是中括号加键名，另一种是通过get()方法传入键名，推荐get()方法，如果键名不存在，则不会报错会返回None，get()方法可以传入第二个参数(即默认值)，
#注意JSON的数据需要用双引号来包围，不能使用单引号,JSON字符串表示需要双引号
#如果从JSON文本中读取内容，先将文本文件内容读出，然后再利用loads()方法转化
# import json
# with open('Python3cui/data.json', 'r') as file:
#     str = file.read()
#     data = json.loads(str)
#     print(data)
#3.输出JSON
#可以调用dumps()方法将JSON对象转化为字符串
# import json
# data = [
#     {
#         'name':'Bob',
#         'gender':'male',
#         'birthday':'1992-10-18'
#     }
# ]
# data = [{'name': '王伟', 'gender': '男', 'birthday': '1992-10-18'}]
# with open('Python3cui/data.json', 'w') as file:
#     file.write(json.dumps(data))
#保存JSON的格式，加一个参数indent,缩进字符个数
# file.write(json.dumps(data, indent=2))
#JSON中包含中文字符，指定参数ensure_ascii为False,规定文件输出的编码
# with open('Python3cui/data.json', 'w', encoding='utf-8') as file:
#     file.write(json.dumps(data, indent=2, ensure_ascii=False))
#5.1.3 CSV存储（写入，读取）
#其文件以纯文本形式储存表格数据，该文件是一个字符序列，可以由任意数目的记录组成，记录间以某种换行符间隔
#1.写入，首先打开data.csv文件，然后指定打开的模式为W(写入)，获得文件句柄，随后调用csv的writer()方法初始化写入对象，传入该句柄，然后调用writerow()方法传入每行的数据即可完成写入
#writerow()方法即可写入一行数据
#Example1
# import csv
# with open('Python3cui/data.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', '20'])
#     writer.writerow(['10002', 'Bob', '22'])
#     writer.writerow(['10003', 'Jordan', '21'])
#初始化写入对象时传入参数 delimiter为空格分隔
# import csv
# with open('Python3cui/data.csv','w')as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ')
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', '20'])
#     writer.writerow(['10002', 'Bob', '22'])
#     writer.writerow(['10003', 'Jordan', '21'])
# writerows()方法同时写入多行，此时参数需要为二维列表
# import csv

# with open('Python3cui/data2.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile,delimiter=' ')
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22],
#                       ['10003', 'Jordan', 21]])
#爬虫爬取的都是结构化数据，我们一般都会用字典来表示，提供了字典写入方式
#DictWriter来初始化一个字典写入对象
#追加写入，可以修改文件的打开模式，即将open()函数的第二个参数修改成a
#如果写入中文内容，遇到字符编码问题，open()参数指定编码格式
#用pandas库可以调用DataFrame对象的to_csv()方法来将数据写入csv文件中
# import csv
# with open('Python3cui/data3.csv', 'w') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
#     writer.writerow({'id': '10002', 'name': 'Bok', 'age': 22})
#     writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
#读取 构造Reader对象，通过遍历输出每行的内容,每一行都是列表，注意包含中文时，还需要指定文件编码
# import csv
# with open('Python3cui/data2.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)
