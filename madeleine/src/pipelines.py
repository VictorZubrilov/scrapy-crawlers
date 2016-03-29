# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy.contrib.exporter import CsvItemExporter
from datetime import datetime
import csv
import urllib2

class MadeleinePipeline(object):
    def __init__(self, settings):
        self.post_url = settings['POST_URL']
        self.files = {}

    @classmethod
    def from_crawler(cls, crawler):
         settings = crawler.settings
         pipeline = cls(settings)
         crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
         crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
         return pipeline

    def spider_opened(self, spider):
        file = open('data/data%s.csv' % datetime.today().strftime('%y%m%d%H%M%S'), 'w+b')
        self.files[spider] = file
        self.exporter = CsvItemExporter(file, quoting=csv.QUOTE_ALL, encoding='utf8');
        self.exporter.fields_to_export = ['masterID', 'path', 'name', 'colors', 'sizes', 'price', 'care', 'consist', 'description', 'brand', 'images', 'images360', 'video_url', 'path_upsell', 'path_related', 'breadcrumbs', 'id_supplier', 'themes']
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)

        if self.post_url:
            file.seek(0)

            data = file.read()
            request = urllib2.Request(self.post_url)
            request.add_header("Content-Type","text/csv")
            urllib2.urlopen(request, data)

        file.close()


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
