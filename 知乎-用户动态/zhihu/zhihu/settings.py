# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

LOG_LEVEL = 'ERROR'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'cookie': '_zap=e19a3419-6fdd-4522-8e3c-5afad4aab04a; d_c0="AHDiT8OVkBCPTsOvxZyMXAL6I9aNRsucojU=|1577360842"; __utmv=51854390.100--|2=registration_date=20170128=1^3=entry_date=20170128=1; ISSW=1; _ga=GA1.2.200357884.1581345511; __utma=51854390.200357884.1581345511.1583659553.1585060195.14; _xsrf=ueRkGGzczB2fBpQCECcjnLrV3OwIUv3K; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1606711701,1606714223,1606785778,1608644701; __snaker__id=KntFMuU6Mh9qInw7; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=k2jSVLGX72NFEREAQVd7K125pxpouiNz; YD00517437729195%3AWM_NI=KiVb1VAHuF%2FuWphZS0up0ixUFQodzzxTE9Ssk06gj%2FifBBencWFc25cRgC97KtegvMixD4ysCm%2FSOByou%2FJVnWD4n0QRoIYWmgacBUHqLcqBHVB85LK2gjcMx0DJdRZtMWE%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee8dc95ca28ea883eb80f59a8fb7d55a869e8e84f445f3ecabb8c94d9bea8388d72af0fea7c3b92a89b79a83b45e8398bba7ae7f95b0a8bbd23cb7b0008afb5f868fa185f972bc8c8bdad279a9f0fa88e925abba8ea3e866a1898a84b13fa18ea9a4bc3d89acab88f547aba88cd5fc7981b3e1b4ce4abbb1bbd0c95eae898cd5ed3c938ea1aadc5dafb9af84c15f8caf8484f44a8c8a8ed9b84889eea98be247bcf08cabe75a9aac83b8c837e2a3; gdxidpyhxdE=KxST7J1Xbb0Juccb%2BYEWBpXg8qcvvHek1oPrKw0RDWMLyKyoVoWUT6%2F7ahu6X50xnjEXZdm77OD6I8bC2EIriUd2p8rnBJIGLHN%2Byx%2FaYgXQMihAuE%2F1Yj6zZHwiuEOo4d7Sqw1vMd%2Fc%5Cq4254IiHq1bIcU%2BHvch4Mq98VdfK2lVpqd6%3A1611473790861; tshl=; q_c1=83847eb57c5b47cd9c624e4fabaa93a7|1613901003000|1577377205000; capsion_ticket="2|1:0|10:1613976057|14:capsion_ticket|44:MmJlYzhlMWJlZWRlNDY4NmI0YzE1N2UyN2VjNTc5NGE=|905d50038453985f1e9b4a915eef1c2a15f1b18fd13b36c2256b027996e5db19"; r_cap_id="YjlmMWE5YjE0ODhjNDk2ZmI0MGMyMGIxYzg3MjBhNDQ=|1613976224|268cefe74b0c1f3820ad47068544262450454a38"; cap_id="NjdhNjg5M2I0NTQyNGFhZDk3M2Y2MmM2ZTRlODAwNGI=|1613976224|4b4e326e135ca822a90ad7bee141d1d09b7aeaf9"; l_cap_id="NDBjYjVkMTFiYmEzNDcwY2JlOWI5YmI1YzRlZDg5OGU=|1613976224|050708973c5e221753d4433928447752992bb6a0"; captcha_session_v2="2|1:0|10:1614740506|18:captcha_session_v2|88:N3N6ZThhNGFHZE9JOGl4VDBZOS9TcjJubkExU0RoRVZ0ZVNhQi84Z0JwMlQzTHVkTW1Cb29mbkVMMHBNRzRBdQ==|ff494fc3ab1dcab53fe3a68e56afcd46e3701c57fb84dc8696b3db4aa6c2c3dc"; captcha_ticket_v2="2|1:0|10:1614740516|17:captcha_ticket_v2|312:eyJhcHBpZCI6IjIwMTIwMzEzMTQiLCJyZXQiOjAsInRpY2tldCI6InQwMy0yMzgtanM4bFdiOUU5NGNEcmNIM0xETl94Vm44V3hRSUVpYWtUSTRFdWo2U04tMDJYb0JCOE9ZMjJVZ3BBWGlhTUVkTTgzSHphcmI5VFNES0doRzFSTVJkS19QZ1c0SkVBbElkMUNmUFRyV2tDMUxZM2ROS2xQZEtGbEdvOTVtUGdLOWJFdWF4S1B1Nkk2dmNyMXl2ZThPZVJzZ1ZGRXdfcEdkdk10alo3USoiLCJyYW5kc3RyIjoiQElmOCJ9|c10ee00e146f49a5ec7954410f34caae19e56356f678294797c31e1f40afed60"; z_c0="2|1:0|10:1614740517|4:z_c0|92:Mi4xWTdxcUdBQUFBQUFBY09KUHc1V1FFQ1lBQUFCZ0FsVk5KVW9zWVFBVGlzRzZnMFJPWGJoempFeEJGVFNDVHN1LUJn|aea452393f3309795134ee391b5c7757b7b9b9162eaab41a1baf4f4d23b01358"; tst=r; SESSIONID=3DTj6h1mmeDYwl6iggVsIKPJgbxrYBxuukzl3g1INZP; JOID=UVAQC0PCKkS7AussF8m6EKtm13UD-mMd0T-IEHekRA3vdYwRc5IfHdAC7SwaOzJ_llP3DkuVieGhzNwAeMlm-KE=; osd=V1wdAUvEJkmxCu0gGsOyFqdr3X0F9m4X2TmEHX2sQgHif4QXf58VFdYO4CYSPT5ynFvxAkafgeetwdYIfsVr8qk=; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12|1616133296|1616131411',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.ZhihuSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'zhihu.middlewares.ProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'zhihu.pipelines.ZhihuPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 设置日期格式
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"

# 开启MongoDB服务：mongod -dbpath D:\MongoDB\data\db
MONGO_URI = 'localhost:27017'
