# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
import json
import requests


class ProxyMiddleware(object):
    def __init__(self):
        self.get_url = "http://d.jghttp.alicloudecs.com/getip?num=10&type=2&pro=&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions="
        self.temp_url = "http://www.baidu.com/"
        self.ip_list = []
        # 用来记录使用ip的个数
        self.count = 0
        # 用来记录每个ip的使用次数
        self.evecount = 0

    def getIPData(self):
        temp_data = requests.get(url=self.get_url).text
        self.ip_list.clear()
        for eve_ip in json.loads(temp_data)["data"]:
            # print(eve_ip)
            self.ip_list.append({
                "ip": eve_ip["ip"],
                "port": eve_ip["port"]
            })
        print(self.ip_list)
        # time.sleep(10000)

    def changeProxy(self, request):
        temp_ip = str(self.ip_list[self.count - 1]["ip"])
        temp_port = str(self.ip_list[self.count - 1]["port"])
        print("changeProxy", "http://" + temp_ip + ":" + temp_port)
        # time.sleep(3)
        request.meta["proxy"] = "http://" + temp_ip + ":" + temp_port

    def yanzheng(self):
        temp_ip = str(self.ip_list[self.count - 1]["ip"])
        temp_port = str(self.ip_list[self.count - 1]["port"])
        proxyMeta = "http://%(host)s:%(port)s" % {
            "host": temp_ip,
            "port": temp_port,
        }
        proxies = {
            "http": proxyMeta,
            # "https" : proxyMeta
        }
        print("yanzheng", proxies)
        # time.sleep(3)
        s = requests.session()
        s.keep_alive = False
        resp = s.get(url=self.temp_url, proxies=proxies, timeout=3, verify=False)
        # time.sleep(3)
        print(resp.status_code)
        # print(resp.text)

    def ifUsed(self, request):
        try:
            self.changeProxy(request)
            self.yanzheng()
        except Exception as e:
            print("######################")
            print(e)
            if self.count == 0 or self.count == 10:
                self.getIPData()
                self.count = 1
            self.count = self.count + 1
            self.ifUsed(request)

    def process_request(self, request, spider):
        if self.count == 0 or self.count == 10:
            self.getIPData()
            self.count = 1

        if self.evecount == 500000:
            self.count = self.count + 1
            self.evecount = 0
        else:
            self.evecount = self.evecount + 1
        # print(self.count, self.evecount)
        self.ifUsed(request)
