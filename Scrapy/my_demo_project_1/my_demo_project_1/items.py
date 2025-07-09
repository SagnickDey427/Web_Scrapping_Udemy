# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy # type: ignore


class ApiScraperItem(scrapy.Item):
    userId = scrapy.Field()
    id = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()

class BookScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()