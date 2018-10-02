# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GithubCodeItem(scrapy.Item):
    name = scrapy.Field()
    repo_clone_url = scrapy.Field()
    repo_download_link = scrapy.Field()
    repo_download_status = scrapy.Field()
    authentication_status = scrapy.Field()
    pass


