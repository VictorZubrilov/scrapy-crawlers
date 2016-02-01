# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ProductItem(scrapy.Item):
    path = scrapy.Field()
    name = scrapy.Field()
    colors = scrapy.Field()
    sizes = scrapy.Field()
    price = scrapy.Field()
    care = scrapy.Field()
    consist = scrapy.Field()
    description = scrapy.Field()
    brand = scrapy.Field()
    images = scrapy.Field()
    images360 = scrapy.Field()
    video_url = scrapy.Field()
    path_upsell = scrapy.Field()
    path_related = scrapy.Field()
    breadcrumbs = scrapy.Field()
    id_supplier = scrapy.Field()
    themes = scrapy.Field()
