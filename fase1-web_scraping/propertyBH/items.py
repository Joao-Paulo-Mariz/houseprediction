# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class propertyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    area_m2 = scrapy.Field()
    bedrooms = scrapy.Field()
    suites = scrapy.Field()
    vacancies = scrapy.Field()
    bathrooms = scrapy.Field()
    neighborhoods = scrapy.Field()
    description = scrapy.Field()
