import urllib.request
import os
import re
import sys



def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()

    return html


def get_page(url):
    return 0


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    back = 0
    reg = r'http://.*.jpg'
    for each in re.findall(reg,html):
        url = each
        urllib.parse.quote(url)
        img_addrs.append(url)
    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        os.popen("\"C:\Program Files (x86)\Thunder Network\Thunder\Program\Thunder.exe\" -StartType:DesktopIcon "+each)

def download_mm(folder='OOXX', pages=10):
    try:
        os.mkdir(folder)
        os.chdir(folder)
    except:None

    url = "http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1471336398482_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1471336398482%5E00_1622X861&word=%E6%80%A7%E6%84%9F+%E7%BE%8E%E5%A5%B3#z=0&pn=&ic=0&st=-1&face=0&s=0&lm=-1"
    page_num = int(get_page(url))
    img_addrs = find_imgs(url)
    save_imgs(folder, img_addrs)

if __name__ == '__main__':
    download_mm()
