# -*- coding: utf-8 -*-

# Scrapy settings for kuzovnoyru project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'madeleine'

SPIDER_MODULES = ['src.spiders']
NEWSPIDER_MODULE = 'src.spiders'

ITEM_PIPELINES = {
   'src.pipelines.MadeleinePipeline': 1000,
}

#DUPEFILTER_CLASS = 'src.duplicatefilter.DupeFilter'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 YaBrowser/15.2.2214.2616 (beta) Safari/537.36'

#DOWNLOAD_DELAY = 0.5

POST_URL = ""

#LOG_FILE = "log.txt"
