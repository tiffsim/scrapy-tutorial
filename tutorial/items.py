# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose


def remove_quotes(text):
    # strip the unicode quotes
    text = text.strip(u'\u201c'u'\u201d')
    return text




class QuoteItem(Item):
    quote_content = Field(input_processor=MapCompose(remove_quotes))
    author_name = Field(input_processor=MapCompose(str.strip))
    author_bio = Field(input_processor=MapCompose(str.strip))
    tags = Field()
