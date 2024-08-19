# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class JobItem(scrapy.Item):
    company = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    location = scrapy.Field()
    experience = scrapy.Field()
    deadline = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    requirements = scrapy.Field()
    benefits = scrapy.Field()
    location = scrapy.Field()
    how_to_apply = scrapy.Field()