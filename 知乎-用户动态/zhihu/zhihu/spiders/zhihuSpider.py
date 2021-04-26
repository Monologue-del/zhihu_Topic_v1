import scrapy
import pandas as pd
import json
from zhihu.items import UserActionItem
import datetime
from zhihu.settings import DATETIME_FORMAT


class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuSpider'
    allowed_domains = ['www.zhihu.com', 'api.zhihu.com']
    # 从数据库获取用户id列表
    user_id_list = pd.read_csv('answers_movies.csv', usecols=['author_id'])
    user_id_list = user_id_list.iloc[:, 0].to_list()
    # print(user_id_list)
    # 用户动态的url
    user_action_url = "https://www.zhihu.com/api/v3/moments/{user}/activities?"

    def start_requests(self):
        for user_id in self.user_id_list:
            # 排除匿名用户
            if user_id != '0':
                yield scrapy.Request(self.user_action_url.format(user=user_id), headers={
                    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'},
                                     callback=self.parse_action)

    def parse_action(self, response):
        """
        爬取用户动态
        :param response:
        :return:
        """
        action_json = json.loads(response.text)
        is_end = action_json['paging']['is_end']
        # 判断用户是否有动态
        if not is_end:
            next_url = action_json['paging']['next']

            # 提取用户动态
            for action in action_json['data']:
                useraction_item = UserActionItem()

                useraction_item['action_id'] = action['id']
                useraction_item['actor_id'] = action['actor']['id']
                useraction_item['actor_name'] = action['actor']['name']
                useraction_item['actor_url'] = action['actor']['url']
                useraction_item['action_text'] = action['action_text']
                useraction_item['verb'] = action['verb']

                # 只爬取“赞同回答”、“回答问题”、“添加问题”、“关注问题”和“关注话题”五种情形，其余情形跳过循环
                if useraction_item['verb'] == "ANSWER_VOTE_UP" or useraction_item['verb'] == "ANSWER_CREATE":
                    # “赞同回答”与“回答问题”的数据解析方式相同，“问题提出者信息”+“问题信息”
                    # 内容的创作时间
                    useraction_item['target_created_time'] = datetime.datetime.fromtimestamp(
                        action['target']['created_time']).strftime(DATETIME_FORMAT)
                    useraction_item['target_excerpt'] = action['target']['excerpt']
                    useraction_item['target_author_id'] = action['target']['author']['id']
                    useraction_item['target_author_name'] = action['target']['author']['name']
                    useraction_item['target_author_url'] = action['target']['author']['url']
                    useraction_item['target_question_author_id'] = action['target']['question']['author']['id']
                    useraction_item['target_question_author_name'] = action['target']['question']['author']['name']
                    useraction_item['target_question_author_url'] = action['target']['question']['author']['url']
                    useraction_item['target_question_id'] = action['target']['question']['id']
                    useraction_item['target_question_title'] = action['target']['question']['title']
                    useraction_item['target_question_url'] = action['target']['question']['url']
                elif useraction_item['verb'] == "QUESTION_FOLLOW" or useraction_item['verb'] == "QUESTION_CREATE":
                    # “添加问题”与“关注问题”的数据解析方式相同，target_question的信息=target本身
                    # 内容的创作时间
                    useraction_item['target_created_time'] = datetime.datetime.fromtimestamp(
                        action['target']['created']).strftime(DATETIME_FORMAT)
                    # target（问题）的信息就是target_question的信息
                    useraction_item['target_excerpt'] = action['target']['excerpt']
                    useraction_item['target_author_id'] = action['target']['author']['id']
                    useraction_item['target_author_name'] = action['target']['author']['name']
                    useraction_item['target_author_url'] = action['target']['author']['url']
                    useraction_item['target_question_author_id'] = action['target']['author']['id']
                    useraction_item['target_question_author_name'] = action['target']['author']['name']
                    useraction_item['target_question_author_url'] = action['target']['author']['url']
                    useraction_item['target_question_id'] = action['target']['id']
                    useraction_item['target_question_title'] = action['target']['title']
                    useraction_item['target_question_url'] = action['target']['url']
                elif useraction_item['verb'] == "TOPIC_FOLLOW":
                    # “关注we”的数据解析
                    useraction_item['target_excerpt'] = action['target']['name']
                    useraction_item['target_created_time'] = None
                    # “关注话题”行为没有target信息
                    useraction_item['target_author_name'] = None
                    useraction_item['target_author_url'] = None
                    useraction_item['target_question_author_id'] = None
                    useraction_item['target_question_author_name'] = None
                    useraction_item['target_question_author_url'] = None
                    useraction_item['target_question_id'] = None
                    useraction_item['target_question_title'] = None
                    useraction_item['target_question_url'] = None
                else:
                    continue

                useraction_item['target_url'] = action['target']['url']
                useraction_item['target_id'] = action['target']['id']
                # 用户动态的时间
                useraction_item['action_time'] = datetime.datetime.fromtimestamp(action['created_time']).strftime(
                    DATETIME_FORMAT)
                useraction_item['crawl_time'] = datetime.datetime.now().strftime(DATETIME_FORMAT)

                yield useraction_item

            if not is_end:
                yield scrapy.Request(next_url, callback=self.parse_action)
