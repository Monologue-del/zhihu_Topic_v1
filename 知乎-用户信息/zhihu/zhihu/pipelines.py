# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient
from zhihu.items import UserInfoItem

class ZhihuPipeline:
    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI')
        )

    def open_spider(self, spider):
        # 连接到数据库
        self.client = MongoClient(self.mongo_uri)
        # 连接到指定的数据库
        zhihu_DB = self.client['zhihu_Topic2']
        # 连接到指定表
        self.info_collection = zhihu_DB['user_info']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # 存储用户基本信息到MongoDB
        if isinstance(item, UserInfoItem):
            self.info_collection.update({'id': item['id']}, {'$set': item}, True)
            print('user_info', item['id'], '爬取成功')
