import os
import requests
from bs4 import BeautifulSoup

"""
将代码进行整理和封装
"""
class Mzitu():
 #  将因为需要重复多次利用requests，故将其封装成函数
    def request(self, url):
    #  浏览器请求头
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
        content = requests.get(url, headers=headers)
        return content

    def all_url(self, url):
        # 调研request函数，把套图的地址传进去，会返回一个response
        html = self.request(url)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存：', title)
            path = str(title).replace('?', '_')    # 注意到有个标题带有 ？  这个符号Windows系统是不能创建文件夹的所以要替换掉
            self.mkdir(path)    # 调用mkdir函数创建文件夹！这儿path代表的是标题title
            os.chdir('F:/Administrator/Desktop/Python-practice/小甲鱼/mzitu/' + path)   #切换到目录

            href = a['href']
            self.html(href)    #调用html函数把href参数(套图的地址)传递过去！

# html函数的作用是出来套图的地址，以获得图片页面的地址
    def html(self, href):
        html = self.request(href)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()

        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)   # 调用img()函数

# img函数的作用是处理图片页面地址，获得图片实际的地址
    def img(self, page_url):
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

# save 函数用于保存图片
    def save(self, img_url):
        name = img_url[-9:-4]
        img = self.request(img_url)

        # 将图片保存到文件中，注意：写入多媒体文件一定需要 'b' 这个参数
        with open(name + '.jpg', 'ab') as f:
            f.write(img.content)  # 多媒体文件要使用content存储


    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(os.path.join('F:/Administrator/Desktop/Python-practice/小甲鱼/mzitu', path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹')
            os.makedirs(os.path.join('F:/Administrator/Desktop/Python-practice/小甲鱼/mzitu/', path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已存在！')
            return False

mzitu = Mzitu()   # 实例化
mzitu.all_url('http://www.mzitu.com/all')









"""
原始代码：

#  将因为需要重复多次利用requests，故将其封装成函数
def request(url):
    #  浏览器请求头
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    content = requests.get(url, headers=headers)
    return content

# 创建文件
def mkdir(self, path):
    path = path.strip()
    isExists = os.path.exists(os.path.join('.\mzitu', path))
    if not isExists:
        print(u'建了一个名字叫做', path, u'的文件夹')
        os.makedirs(os.path.join('.\mzitu', path))
        return True
    else:
        print(u'名字叫做', path, u'的文件夹已存在！')
        return False

#开始爬取的URL地址
all_url = 'http://www.mzitu.com/all'
start_html = requests.get(all_url, headers = headers)

# 使用BeautifulSoup来解析我们获取到的网页， lxml是指定的解析器
Soup = BeautifulSoup(start_html.text, 'lxml')
'''
# 使用BeautifulSoup解析网页后，使用find_all查找网页中所有的li标签，它返回的是一个列表。
li_list = Soup.find_all('li')
for li in li_list:
    print(li)
'''

def all_url(self, url):

# 先查找class为 all 的 div 标签，然后查找所有的 a 标签
all_a = Soup.find('div', class_='all').find_all('a')
for a in all_a:
    # print(a)

    title = a.get_text()  # 取出 a 标签的文本
    href = a['href']   # 取出 a 标签的 href 属性
   # print(title, href)

    html = requests.get(href, headers = headers)
    html_soup = BeautifulSoup(html.text, 'lxml')

    # 查找所有的<span>标签，获取第十个<span>标签的文本，也就是最后一个界面
    max_span = html_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()

    for page in range(1, int(max_span)+1):
        page_url = href + '/' + str(page)
       # print(page_url)

        img_html = requests.get(page_url, headers=headers)
        img_soup = BeautifulSoup(img_html.text, 'lxml')
        img_url = img_soup.find('div', class_='main-image').find('img')['src']
    #   print(img_url)

        name = img_url[-9:-4]   # 取 URL 的倒数第四位至第九位 作为图片的名字
        img = requests.get(img_url, headers=headers)

        # 将图片保存到文件中，注意：写入多媒体文件一定需要 'b' 这个参数
        with open(name+'.jpg', 'ab') as f:
            f.write(img.content)   # 多媒体文件要使用content存储

"""