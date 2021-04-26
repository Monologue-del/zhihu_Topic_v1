# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UserInfoItem(scrapy.Item):
    """
    用户基本信息
    """
    id = scrapy.Field()
    url_token = scrapy.Field()
    url = scrapy.Field()
    type = scrapy.Field()
    name = scrapy.Field()
    gender = scrapy.Field()
    headline = scrapy.Field()
    locations = scrapy.Field()
    business = scrapy.Field()
    employments = scrapy.Field()
    educations = scrapy.Field()
    description = scrapy.Field()
    exp = scrapy.Field()
    level = scrapy.Field()
    identity = scrapy.Field()
    best_answerer = scrapy.Field()
    best_topics = scrapy.Field()
    follower_count = scrapy.Field()
    following_count = scrapy.Field()
    answer_count = scrapy.Field()
    question_count = scrapy.Field()
    articles_count = scrapy.Field()
    columns_count = scrapy.Field()
    zvideo_count = scrapy.Field()
    favorite_count = scrapy.Field()
    favorited_count = scrapy.Field()
    voteup_count = scrapy.Field()
    thanked_count = scrapy.Field()
    live_count = scrapy.Field()
    hosted_live_count = scrapy.Field()
    participated_live_count = scrapy.Field()
    included_answers_count = scrapy.Field()
    included_articles_count = scrapy.Field()
    following_columns_count = scrapy.Field()
    following_topic_count = scrapy.Field()
    following_question_count = scrapy.Field()
    following_favlists_count = scrapy.Field()
    recognized_count = scrapy.Field()
    crawl_time = scrapy.Field()
