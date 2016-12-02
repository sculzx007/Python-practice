import urllib.request
import urllib.parse
import time
import random

# https://www.whatismyip.com/是一个检测当前IP的网站

url = 'https://www.whatismyip.com/'

#IP地址列表
ip_list = ['124.128.221.27:8080', '125.45.87.12:9999', '188.113.138.238:3128', '219.132.232.129:9797']

'''
使用代理的步骤：
1.使用urllib.request内置的方法ProxyHandler({'协议类型（如http，https）':'代理IP（包括端口号）'})
2.定制、创建一个opener，使用opener = urllib.request.build_opener(proxy_support)
3.安装opener，使用urllib.request.build_opener
'''


proxy_support = urllib.request.ProxyHandler({'http':random.choice(ip_list)})

opener = urllib.request.build_opener(proxy_support)

#给opener加上headers，防止网站检测为爬虫
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)
