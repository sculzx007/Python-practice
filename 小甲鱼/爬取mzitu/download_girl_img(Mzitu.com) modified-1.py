import os
from Download import request
from bs4 import BeautifulSoup
from pymongo import MongoClient


class Mzitu():
    def all_url(self, url):
        html = request.get(url, 3)  # 导入了反爬虫模块后，这里修改了
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print(u'开始保存：', title)
            path = str(title).replace('?', '_')
            self.mkdir(path)
            os.chdir('F:/Administrator/Desktop/Python-practice/小甲鱼/mzitu/' + path)

            href = a['href']
            self.html(href)


    def html(self, href):
        html = request.get(href, 3)   # # 导入了反爬虫模块后，这里修改了
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()

        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)


    def img(self, page_url):
        img_html = request.get(page_url, 3)   # 导入了反爬虫模块后，这里修改了
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
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








