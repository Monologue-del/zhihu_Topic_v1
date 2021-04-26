# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuestionItem(scrapy.Item):
    """
    问题Item
    """
    question_id = scrapy.Field()
    type = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    detail = scrapy.Field()
    topics = scrapy.Field()
    media_link = scrapy.Field()
    browse_count = scrapy.Field()
    follow_count = scrapy.Field()
    star_count = scrapy.Field()
    author_id = scrapy.Field()
    isMuted = scrapy.Field()
    isVisible = scrapy.Field()
    isNormal = scrapy.Field()
    isEditable = scrapy.Field()
    create_time = scrapy.Field()
    update_time = scrapy.Field()
    crawl_time = scrapy.Field()


class AnswerItem(scrapy.Item):
    """
    答案Item
    """
    answer_id = scrapy.Field()
    answer_url = scrapy.Field()
    question_id = scrapy.Field()
    question_title = scrapy.Field()
    author_id = scrapy.Field()
    author_name = scrapy.Field()
    content = scrapy.Field()
    praise_num = scrapy.Field()
    comments_num = scrapy.Field()
    create_time = scrapy.Field()
    crawl_time = scrapy.Field()
    update_time = scrapy.Field()
