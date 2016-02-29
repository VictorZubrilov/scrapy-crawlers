#!/bin/bash

cd /var/lib/jenkins/jobs/scrapy-crawlers/workspace/madeleine
/usr/local/bin/scrapy crawl madeleinespider --logfile app.log
