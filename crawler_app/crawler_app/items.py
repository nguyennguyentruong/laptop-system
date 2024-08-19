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

class LaptopItem(scrapy.Item):
    price = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    detail = scrapy.Field()
    about = scrapy.Field()

import scrapy
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


def strip_spaces(value):
    return value.strip().replace("$", "")


class AmzScraperItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_spaces),
        output_processor=TakeFirst(),
    )
    asin = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_spaces),
        output_processor=TakeFirst(),
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_spaces),
        output_processor=TakeFirst(),
    )
    discounted = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_spaces),
        output_processor=TakeFirst(),
    )
    totalreviews = scrapy.Field(
        input_processor=MapCompose(remove_tags, strip_spaces),
        output_processor=TakeFirst(),
    )
