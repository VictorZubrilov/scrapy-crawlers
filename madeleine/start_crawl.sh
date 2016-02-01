#!/bin/bash

cd /var/lib/jenkins/jobs/scrapy-crawlers/workspace/madeleine
scrapy crawl madeleinespider --logfile app.log

