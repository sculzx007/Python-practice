
import urllib.request
import re
import os

if not os.path.exists('Picture'):
    os.mkdir('Picture')
os.chdir('Picture')

#获取网页内容
def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36') #伪装成浏览器访问
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return html

def imge_mm(content):
    rul = r'<img class="BDE_Image" src="([^"]+\.jpg)'
    rull = re.compile(rul)
    imglist = rull.findall(content) #获取图片链接


    #下载图片
    for each in imglist:
        filename = each.split('/')[-1]
        urllib.request.urlretrieve(each, filename)

    
reg = r'<a href="/p/([^/]+)" title' 
regl = re.compile(reg)
page_num = regl.findall(open_url('http://tieba.baidu.com/f?kw=%C3%C0%C5%AE&fr=ala0&tpl=5')) #获取主页所有帖子的网页地址序号

for each in page_num:
    url = 'http://tieba.baidu.com/p/' + str(each)
    content = open_url(url)
    imge_mm(content)
