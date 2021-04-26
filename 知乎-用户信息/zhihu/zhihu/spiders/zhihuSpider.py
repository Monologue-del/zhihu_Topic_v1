import scrapy
import pandas as pd
import json
from zhihu.items import UserInfoItem
import datetime
from zhihu.settings import DATETIME_FORMAT


class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuSpider'
    allowed_domains = ['www.zhihu.com', 'api.zhihu.com']
    # 从数据库获取用户id列表
    user_id_list = pd.read_csv('answers_movies.csv', usecols=['author_id'])
    user_id_list = user_id_list.iloc[:, 0].to_list()
    # print(user_id_list)
    # 用户信息的url
    user_url = 'https://api.zhihu.com/people/{user}'

    def start_requests(self):
        for user_id in self.user_id_list:
            # 排除匿名用户
            if user_id != '0':
                yield scrapy.Request(self.user_url.format(user=user_id), headers={
                    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'},
                                     callback=self.parse_user)

    def parse_user(self, response):
        """
        爬取用户基本信息；
        调用parse_followees和parse_followers爬取关注者和粉丝列表
        :param response:
        :return:
        """
        result = json.loads(response.text)
        # 提取用户基本信息
        userinfo_item = UserInfoItem()

        userinfo_item['id'] = result['id']
        userinfo_item['url_token'] = result['url_token']
        userinfo_item['url'] = result['url']
        userinfo_item['type'] = result['type']
        userinfo_item['name'] = result['name']
        userinfo_item['gender'] = result['gender']
        userinfo_item['headline'] = result['headline']
        try:
            userinfo_item['locations'] = []
            userinfo_item['locations'] = [location['name'] for location in result['location']]
        except:
            userinfo_item['locations'] = ""
        userinfo_item['business'] = []
        userinfo_item['business'] = result['business'].get('name')
        try:
            userinfo_item['employments'] = []
            userinfo_item['employments'] = [(employment[0]['name'] + employment[1]['name']) for employment in
                                            result['employment']]
        except:
            userinfo_item['employments'] = ""
        try:
            userinfo_item['educations'] = []
            userinfo_item['educations'] = [education['name'] for education in result['education']]
        except:
            userinfo_item['educations'] = ""
        userinfo_item['description'] = result['description']
        try:
            userinfo_item['exp'] = result['level_info']['exp']
            userinfo_item['level'] = result['level_info']['level']
        except:
            userinfo_item['exp'] = ['']
            userinfo_item['level'] = ['']
        try:
            userinfo_item['identity'] = []
            userinfo_item['best_answerer'] = []
            userinfo_item['best_topics'] = []
            for obj in result['badge']:
                if obj['type'] == "identity":
                    userinfo_item['identity'].append(obj['description'])
                if obj['type'] == "best_answerer":
                    userinfo_item['best_answerer'].append(obj['description'])
                    userinfo_item['best_topics'] = [topics['name'] for topics in obj['topics']]
        except:
            userinfo_item['identity'] = ""
            userinfo_item['best_answerer'] = ""
            userinfo_item['best_topics'] = ""
        userinfo_item['follower_count'] = result['follower_count']
        userinfo_item['following_count'] = result['following_count']
        userinfo_item['answer_count'] = result['answer_count']
        userinfo_item['question_count'] = result['question_count']
        userinfo_item['articles_count'] = result['articles_count']
        userinfo_item['columns_count'] = result['columns_count']
        userinfo_item['zvideo_count'] = result['zvideo_count']
        userinfo_item['favorite_count'] = result['favorite_count']
        userinfo_item['favorited_count'] = result['favorited_count']
        userinfo_item['voteup_count'] = result['voteup_count']
        userinfo_item['thanked_count'] = result['thanked_count']
        userinfo_item['live_count'] = result['live_count']
        userinfo_item['hosted_live_count'] = result['hosted_live_count']
        userinfo_item['participated_live_count'] = result['participated_live_count']
        userinfo_item['included_answers_count'] = result['included_answers_count']
        userinfo_item['included_articles_count'] = result['included_articles_count']
        userinfo_item['following_columns_count'] = result['following_columns_count']
        userinfo_item['following_topic_count'] = result['following_topic_count']
        userinfo_item['following_question_count'] = result['following_question_count']
        userinfo_item['following_favlists_count'] = result['following_favlists_count']
        userinfo_item['recognized_count'] = result['recognized_count']
        userinfo_item['crawl_time'] = datetime.datetime.now().strftime(DATETIME_FORMAT)

        yield userinfo_item
