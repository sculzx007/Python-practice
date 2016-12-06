import urllib.request
import re
import ssl
import random
import os


def open_url(url):
    
# 获取子网页的ip地址列表
    for i in range(20):
        
        # 使用的IP地址列表
        ip_list = ['124.128.221.27:8080', '125.45.87.12:9999', '188.113.138.238:3128', '219.132.232.129:9797']

        proxy_support = urllib.request.ProxyHandler({'http':random.choice(ip_list)})

        opener = urllib.request.build_opener(proxy_support)

        #给opener加上headers，防止网站检测为爬虫
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')]

        urllib.request.install_opener(opener)

        page = urllib.request.urlopen(url)

        html = page.read().decode('utf-8')

        url += str(i)
    
    return html

def get_iplist(html):
    ip = r'(?:(?:[0-1]?\d?\d|[2[0-4]]\d|[25[0-5]])\.){3}(?:[0-1]?\d?\d|[2[0-4]]\d|[25[0-5]])'
    iplist = re.findall(ip, html)  

# 将获取的IP代理地址保存到txt文件中
    try:
        with open('IP代理地址列表.txt', 'wb') as f:
            for each in iplist:
                f.wirte(each)
    except IOError as reason:
        print("Don't get IP proxy list!")



if __name__ == '__main__':
      
    url = 'http://www.xicidaili.com/nn/'
    get_iplist(open_url(url))
    
