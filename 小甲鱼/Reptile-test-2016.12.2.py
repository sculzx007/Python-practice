'''
Time: 2016/12/02
Author: lzx
Purpose: Inorder to make a program for traslate the word which user input, and test
    the raptile of web
'''

import urllib.request
import urllib.parse
import json
import time

while True:
    content = input("请输入要翻译词语（输入'Q'退出程序）：")

    if content == 'Q':
        break
    
    head = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
    url = ("http://fanyi.youdao.com/translate?smartresult\
    =dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link")
    data = {
        'type':'AUTO',
        'i':content,
        'doctype':'json',
        'xmlVersion':'1.8',
        'keyfrom':'fanyi.web',
        'ue':'UTF-8',
        'action':'FY_BY_CLICKBUTTON',
        'typoResult':'true'
        }
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data, head)

    '''
    修改headed的方法有两种：
    1.通过Request的head来追加生成（在此之前先定义一个head的字典）
    2.通过Request.add_header(key, value)方法追加（在此之前不需要定义head）
    例如
    req = urllib.request.Request(url, data)
    req.add_header('User-Agent', ''Mozilla/5.0 (Windows NT 6.1) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'')
    '''
    respone = urllib.request.urlopen(req)
    html = respone.read().decode("utf-8")

    target = json.loads(html)
    translate_target = target['translateResult'][0][0]['tgt']

    print(translate_target)
    
# 使用time模块，是为了模拟人类的操作时间，防止网站检测为爬虫程序而将其封锁
    time.sleep(3000)


