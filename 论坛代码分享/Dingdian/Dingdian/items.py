# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DingdianItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 小说名字
    name = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 小说地址
    novel_url = scrapy.Field()
    # 小说状态
    serial_status = scrapy.Field()
    # 连载字数
    serial_number = scrapy.Field()
    # 小说类别
    category = scrapy.Field()
    # 小说编号
    name_id = scrapy.Field()

class DcontentItem(scrapy.Item):
    # 小说编号
    id_name = scrapy.Field()
    # 章节内容
    chapter_content = scrapy.Field()
    # 章节编号，用于绑定章节的顺序
    num = scrapy.Field()
    # 章节地址
    chapter_url = scrapy.Field()
    #章节名字
    chapter_name = scrapy.Field()

