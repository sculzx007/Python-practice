import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request   # 一个单独的Request模块，需要跟进URL的时候，需要用到它
from Dingdian.items import DingdianItem  # 自定义需要保存的字段。（导入dingdian项目中，items文件中的DingdianItem类）
from Dingdian.items import DcontentItem

class Dingdian(scrapy.Spider):
    name = 'Dingdian'  # 此name名字在整个项目中有且只能有一个

# allowed_domain 的作用是只会跟进存在于allowed_domain中的URL
    allowed_domain = ['http://www.23wx.com/']
    bash_url = 'http://www.23wx.com/class/'
    end_url = '.html'

    def start_requests(self):
        for each in range(1, 11):
            url = self.bash_url + str(each) + self.end_url
            yield Request(url, self.parse)
        yield Request('http://www.23wx.com/quanben/1', self.parse)

    def parse(self, response):  # 接受19行返回的Request中的response，并处理

        # 使用bs4从response中获取最大页码
        max_num = BeautifulSoup(response.text, 'lxml').find('div', class_ = 'pagelink').find_all('a')[-1].get_text()

        # 使用for循环，将完整的URL拼接出来
        for each in range(1, 11):
            for num in range(1, int(max_num) + 1):
                url = self.bash_url + str(each) + '_'+ str(num) + self.end_url
                yield Request(url, callback=self.get_name)

    '''
    yield Request，请求新的URL，后面跟的是回调函数，需要哪一个函数来处理这个返回值，就调用哪一个函数，返回值会以参数的形式传递给我们所调用的函数。
    '''

    def get_name(self, response):
# 获取小说的名字和URL
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        for td in tds:
# 使用循环的原因是find_all取出来的标签是以列表形式存在的，不然没有办法继续使用find
            novel_name = td.find('a').get_text()
            novel_url = td.find('a')['href']
            yield Request(novel_url, callback=self.get_chapter_url, meta={'name':novel_name, 'url': novel_url})

    def get_chapter_url(self, response):
        item = DingdianItem()    # 将我们导入的item文件实例化，用来存储数据
        item['name'] = str(response.meta['name']).replace('\xa0', '')
        item['novel_url'] = response.meta['url']

        category = BeautifulSoup(response.text, 'lxml').find('table').find('a').get_text()

        author = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].get_text()

        bash_url = BeautifulSoup(response.text, 'lxml').find('p', class_='btnlinks').find('a', class_='read')['href']

        name_id = str(bash_url)[-6:-1].replace('/','')


        item['category'] = str(category).replace('\xa0', '')
        item['author'] = str(author).replace('\xa0', '')
        item['name_id'] = name_id

        yield item
        yield Request(url=bash_url, callback=self.get_chapter, meta={'name_id':name_id})

    def get_chapter(self, response):
        urls = re.findall(r'<td class="L"><a href="(.*?)">(.*?)</a></td>', response.text)

        num = 0
        for url in urls:
            num += 1
            chapter_url = response.url + url[0]
            chapter_name = url[1]
            yield Request(chapter_url, callback=self.get_chapter_content, meta={'num':num, 'name_id':response.meta['name_id'], 'chapter_name':chapter_name, 'chapter_url':chapter_url})

    def get_chapter_content(self, response):
        
        item = DcontentItem()

        item['num'] = response.meta['num']
        item['id_name'] = response.meta['name_id']
        item['chapter_name'] = str(response.meta['chapter_name']).replace('\xa0', '')
        item['chapter_url'] = response.meta['chapter_url']

        content = BeautifulSoup(response.text, 'lxml').find('dd', id='contents').get_text()
        item['chapter_content'] = str(content).replace('\xa0', '')

        return item
