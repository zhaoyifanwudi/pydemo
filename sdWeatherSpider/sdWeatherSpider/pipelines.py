# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SdweatherspiderPipeline(object):
    def process_item(self, item, spider):
        with open('weather.txt','a',encoding='utf8') as fp:
            fp.write(item['city']+'\n')
            fp.write(item['weather']+'\n\n')
        return item
