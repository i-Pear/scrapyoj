# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ojlistItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    runid = scrapy.Field()
    title = scrapy.Field()
    similar = scrapy.Field()
    date = scrapy.Field()
    language = scrapy.Field()
