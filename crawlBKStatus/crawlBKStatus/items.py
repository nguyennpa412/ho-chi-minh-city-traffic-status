# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item


class CrawlbkstatusItem(scrapy.Item):
  # define the fields for your item here like:
  # name = scrapy.Field()
  pass


class FileData(Item):
  file_urls = scrapy.Field()
  files = scrapy.Field()
