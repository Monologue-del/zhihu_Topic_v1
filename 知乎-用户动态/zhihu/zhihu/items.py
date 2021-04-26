# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UserActionItem(scrapy.Item):
    """
    用户动态
    """
    action_id = scrapy.Field()
    actor_id = scrapy.Field()
    actor_name = scrapy.Field()
    actor_url = scrapy.Field()
    action_text = scrapy.Field()
    verb = scrapy.Field()
    action_time = scrapy.Field()
    target_excerpt = scrapy.Field()
    target_created_time = scrapy.Field()
    target_id = scrapy.Field()
    target_url = scrapy.Field()
    target_author_id = scrapy.Field()
    target_author_name = scrapy.Field()
    target_author_url = scrapy.Field()
    target_question_author_id = scrapy.Field()
    target_question_author_name = scrapy.Field()
    target_question_author_url = scrapy.Field()
    target_question_id = scrapy.Field()
    target_question_title = scrapy.Field()
    target_question_url = scrapy.Field()
    crawl_time = scrapy.Field()
