from Scrapy.items import DmozItem

import scrapy

'''
使用Scrapy抓取网站的步骤：
1. 创建一个Scrapy项目
2. 定义Item容器
3. 编写爬虫
4. 存储内容
'''

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['dmoz.org']
    start_urls = [
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
        'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/'
        ]

    def parse(self, response):
        sel = scrapy.selector.Selector(response)  
        items = []

        path_list = []
        for i in range(1, 19):

#通过分析网页，可以知道，title等信息的xpath地址为//*[@id="site-list-content"]/div[i]/div[3]，i的范围为1-18
            path = '//*[@id="site-list-content"]/div[' + str(i) + ']/div[3]'
            sites = sel.xpath(path)
            
            for sel in sites:
                item = DmozItem()
                
                item['title'] = sel.xpath('a/div/text()').extract()
                item['link'] = sel.xpath('a/@href').extract()
                item['desc'] = sel.xpath('div/text()').extract()

                items.append(item)

        return items
      
           

