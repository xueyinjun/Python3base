#encoding=utf-8
# 抓取猫眼电影排行 提取出猫眼电影TOP100的电影名称、时间、评分、图片等信息

#Eaxmple1 抓取首页  先实现get_one_page方法,传入url参数，然后抓取到的页面结果返回,再通过main()方法调用

# import requests

# def get_one_page(url):
#     headers = {
#         'User-Agent':
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.text

#     return None

# def main():
#     url = 'https://maoyan.com/board/4'
#     html = get_one_page(url)
#     print(html)

# main()

#Example2 正则表达式提取电影信息
#提取i节点内的信息 它的排名信息
# <dd>.*?board-index.*?>(.*?)</i>
#需要提取电影的图片
#<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"
#需要提取电影的名称
#<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>
#再提取主演、发布时间、评分等内容同理
#<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?><p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)fraction.*?>(.*?)</i>.*?</dd>

#Eaxmple2
# def parse_one_page(html):
#     pattern = re.compile(
#         '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?><p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)fraction.*?>(.*?)</i>.*?</dd>'
#     ,re.S)
#     items = re.findall(pattern,html)
#     print(items)
#数据太乱匹配结果处理一下,遍历提取生成字典，形成结构化数据
# for item in items:
#     yield {
#         'index': item[0],
#         'image': item[1],
#         'title': item[2].strip(),
#         'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
#         'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
#         'score': item[5].strip() + item[6].strip()
#     }

#写入文件
#通过JSON库的dumps()方法实现字典的序列化，这样可以保证输出结果是中文形式而不是Unicode编码，
# def write_to_file(content):
#     with open('result.txt', 'a', encoding='utf-8') as f:
#         print(type(json.dumps(content)))
#         f.write(json.dumps(content, ensure_ascii=False) + '\n')

#整合代码,将单页结果写入
# def main():
#     url = 'http://maoyan.com/board/4'
#     html = get_one_page(url)
#     for item in parse_one_page(html):
#         write_to_file(item)

#分页爬取
# if __name__ == '__main__':
#     for i in range(10):
#         main(offset=i * 10)

# #修改main()方法,接收一个offset值作为偏移量,然后构造URL进行爬取
# def main(offset):
#     url = 'https://maoyan.com/board/4?offset=' + str(offset)
#     html = get_one_page(url)
#     for item in parse_one_page(html):
#         print(item)
#         write_to_file(item)

import requests
import json
import re
from requests.exceptions import RequestException
import time


def get_one_page(url):
    try:
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except RequestException:
        return None


def parser_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'https://www.maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parser_one_page(html):       
        write_to_file(item)
        print(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)