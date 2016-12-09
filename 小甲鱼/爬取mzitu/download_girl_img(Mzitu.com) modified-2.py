import os
from Download import request
from bs4 import BeautifulSoup
from pymongo import MongoClient
import datetime


class Mzitu():
    def __init__(self):
        client = MongoClient()     # 与MongoDB建立链接（这是默认链接本地MongoDB数据库）
        db = client['Beautiful_girl_image'] #选择一个数据库
        self.meizitu_collection = db['meizitu']  # 在Beautiful_girl_image数据库中，选择一个集合
        self.title = ''  # 用于保存页面主题
        self.url = ''   #用于保存页面地址
        self.img_urls = []    #用于保存图片地址

    def all_url(self, url):
        html = request.get(url, 3)  # 导入了反爬虫模块后，这里修改了，3 是延迟时间
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存：', title)
            path = str(title).replace('?', '_')
            self.mkdir(path)
            os.chdir('F:/Administrator/Desktop/Python-practice/小甲鱼/mzitu/' + path)

            href = a['href']
            self.url = href  # 将页面地址保存到 self.url 中

            # 先判断这个主题是否已经在数据库中，如果存在，则忽略，否则爬取
            if self.meizitu_collection.find_one({'主题界面':href}):
                print(u'这个页面已经爬取过了')
            else:
                self.html(href)


    def html(self, href):
        html = request.get(href, 3)   # # 导入了反爬虫模块后，这里修改了
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()

        page_num = 0  #将其作为计数器，判断是否下载完毕
        for page in range(1, int(max_span) + 1):
            page_num += 1  # 当 page_num 等于 max_span 时，证明在下载最后一张照片

            page_url = href + '/' + str(page)
            self.img(page_url, max_span, page_num)


    def img(self, page_url, max_span, page_num):
        img_html = request.get(page_url, 3)   # 导入了反爬虫模块后，这里修改了
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']

        self.img_urls.append(img_url)  # html()函数中每一次for循环获取到的图片地址会添加到 img_urls 列表中

# 当max_span和Page_num相等时，就是最后一张图片了，最后一次下载图片并保存到数据库中
        if int(max_span) == page_num:
            self.save(img_url)

            # 构造一个字典post，定义相关的字段
            post = {
                '标题':self.title,
                '主题页面': self.url,
                '图片地址': self.img_urls,
                '获取时间': datetime.datetime.now(),
            }
            self.meizitu_collection.save(post)
            print(u'插入数据库成功')
        else:
            self.save(img_url)


    def save(self, img_url):
        name = img_url[-9:-4]
        img = request.get(img_url, 3) # 导入了反爬虫模块后，这里修改了


        with open(name + '.jpg', 'ab') as f:
            f.write(img.content)


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

mzitu = Mzitu()
mzitu.all_url('http://www.mzitu.com/all')








