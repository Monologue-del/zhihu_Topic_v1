import scrapy
import json
import datetime
import time
from zhihu.items import AnswerItem, QuestionItem
from zhihu.settings import DATETIME_FORMAT
from lxml import etree


class ZhihuspiderSpider(scrapy.Spider):
    """
    通过话题页，爬取问题url，再分别爬取问题信息、回答信息，存储到MongoDB
    """
    name = 'zhihuSpider'
    allowed_domains = ['www.zhihu.com', 'api.zhihu.com']
    # 起始话题id
    start_topic = '19550429'
    # 话题页，起始url
    topic_url = 'http://www.zhihu.com/api/v4/topics/{topic_id}/feeds/top_question?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Canswer_type%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.paid_info%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10&offset=0'
    # 答案页url
    answer_url = 'https://www.zhihu.com/api/v4/questions/{question_id}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics%3Bdata%5B*%5D.settings.table_of_content.enabled&offset=&limit=10&sort_by=default&platform=desktop'
    # 问题页url
    question_url = 'https://www.zhihu.com/question/{question_id}'

    def start_requests(self):
        yield scrapy.Request(self.topic_url.format(topic_id=self.start_topic), headers={
            'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'},
                             callback=self.parse)

    def parse(self, response):
        """
        爬取话题页问题url和id
        :param response:
        :return:
        """
        # 处理翻页
        topic_json = json.loads(response.text)
        is_end = topic_json["paging"]["is_end"]
        next_url = topic_json["paging"]["next"]

        # 提取问题id
        for question in topic_json["data"]:
            question_id = question["target"]["id"]
            yield scrapy.Request(self.question_url.format(question_id=question_id),
                                 callback=self.parse_question)
            yield scrapy.Request(self.answer_url.format(question_id=question_id),
                                 callback=self.parse_answer)
        # 判断此话题下的问题是否爬取完毕
        if not is_end:
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_question(self, response):
        """
        解析问题页面，提取问题信息
        :param response:
        :return:
        """
        json_text_content = response.xpath("//script[@id='js-initialData']/text()").get()
        time.sleep(1)
        json_content = json.loads(json_text_content)
        question_id = response.url.split('/')[-1]
        question_item = QuestionItem()
        question = json_content['initialState']['entities']['questions'][str(question_id)]
        question_item['question_id'] = question['id']
        question_item['type'] = question['type']
        question_item['title'] = question['title']
        question_item['description'] = question['excerpt']
        question_item['detail'] = question['detail']
        question_item['topics'] = []
        for topic in question['topics']:
            question_item['topics'].append(topic['name'])
        if etree.HTML(question['detail']) is not None:
            question_item['media_link'] = ';'.join(etree.HTML(question['detail']).xpath("//img/@src"))
        else:
            question_item['media_link'] = ''
        question_item['browse_count'] = int(question['visitCount'])
        question_item['follow_count'] = int(question['followerCount'])
        question_item['star_count'] = int(question['relationship']['voting'])
        question_item['author_id'] = question['author']['id']
        question_item['isMuted'] = question['isMuted']
        question_item['isVisible'] = question['isVisible']
        question_item['isNormal'] = question['isNormal']
        question_item['isEditable'] = question['isEditable']
        question_item["create_time"] = datetime.datetime.fromtimestamp(question["created"]).strftime(
            DATETIME_FORMAT)
        question_item["update_time"] = datetime.datetime.fromtimestamp(question["updatedTime"]).strftime(
            DATETIME_FORMAT)
        question_item["crawl_time"] = datetime.datetime.now().strftime(DATETIME_FORMAT)
        return question_item

    def parse_answer(self, response):
        """
        解析答案页面，提取答案信息
        :param response:
        :return:
        """
        # 处理question的answer
        ans_json = json.loads(response.text)
        is_end = ans_json['paging']['is_end']
        next_url = ans_json['paging']['next']

        # 判断答案是否有回答
        if len(ans_json["data"]) == 0:
            pass
        # 提取answer的具体字段
        else:
            for answer in ans_json['data']:
                answer_item = AnswerItem()
                answer_item["answer_id"] = answer["id"]
                answer_item["answer_url"] = answer["url"]
                answer_item["question_id"] = answer["question"]["id"]
                answer_item["question_title"] = answer["question"]["title"]
                answer_item["author_id"] = answer["author"]["id"] if "id" in answer["author"] else None
                answer_item["author_name"] = answer["author"]["name"] if "name" in answer["author"] else None
                answer_item["content"] = answer["content"] if "content" in answer else None
                answer_item["praise_num"] = answer["voteup_count"]
                answer_item["comments_num"] = answer["comment_count"]
                answer_item["create_time"] = datetime.datetime.fromtimestamp(answer["created_time"]).strftime(
                    DATETIME_FORMAT)
                answer_item["update_time"] = datetime.datetime.fromtimestamp(answer["updated_time"]).strftime(
                    DATETIME_FORMAT)
                answer_item["crawl_time"] = datetime.datetime.now().strftime(DATETIME_FORMAT)

                yield answer_item

            if not is_end:
                yield scrapy.Request(next_url, callback=self.parse_answer)
