# -*- coding: utf-8 -*-
import scrapy
import os
import re
import codecs
import json
import sys
from scrapy import Spider
from scrapy.selector import Selector
from LG.items import LgItem
from scrapy.http import Request
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class LgpositionSpider(scrapy.Spider):
    name = 'LGPosition'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']

    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?px=default&city=%E5%85%A8%E5%9B%BD',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest'
        },
        "ITEM_PIPELINES": {
            'LG.pipelines.LgPipeline': 300,
        }
    }

    def start_requests(self):
        # 修改city参数更换城市
        url = "https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&city=全国"
        requests = []
        for i in range(1, 60):
            # 修改kd参数更换关键字
            formdata = {'first': 'false', 'pn': str(i), 'kd': '不限'}
            request = FormRequest(url, callback=self.parse, formdata=formdata)
            requests.append(request)
            print(request)
        return requests

    def parse(self, response):

        print(response.body.decode())
        jsonBody = json.loads(response.body.decode())
        results = jsonBody['content']['positionResult']['result']
        items = []
        for result in results:
            item = LgItem()
            item['name'] = result['companyFullName']
            item['location'] = result['city']
            item['position'] = result['positionName']
            item['exprience'] = result['workYear']
            item['money'] = result['salary']
            items.append(item)
        return items
