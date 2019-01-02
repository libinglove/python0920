# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
import json
import codecs
from openpyxl import Workbook

class LgPipeline(object):
    def __init__(self):
        self.workbook = Workbook()
        self.ws = self.workbook.active
        self.ws.append(['公司名称', '工作地点', '职位名称', '经验要求', '薪资待遇'])  # 设置表头
        # self.file = codecs.open('lagou2.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = [item['name'], item['location'], item['position'], item['exprience'], item['money']]  # 把数据中每一项整理出来
        self.ws.append(line)
        self.workbook.save('lagou2.xlsx')  # 保存xlsx文件
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.file.write(line)

        return item

    def spider_closed(self, spider):
        self.file.close()