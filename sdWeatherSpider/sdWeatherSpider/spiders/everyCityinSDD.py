# -*- coding: utf-8 -*-
import scrapy


class EverycityinsddSpider(scrapy.Spider):
    name = 'everyCityinSDD'
    allowed_domains = ['www.weather.com.cn']
    start_urls = ['http://www.weather.com.cn/']
    url = r'http://www.weather.com.cn/shandong/index.shtml'
    with urlopen(url) as fp:
        contents = fp.read().decode()
    pattern = '<a title=".*?" href="(.?)" target="_blank">(.+?)</a>'
    for url in findall(pattern,contents):
        start_urls.append(url[0])
    
    def parse(self, response):
        item = SdweatherspiderItem()
        city = response.xpath('//div[@class="crumbs fl"]//a[2]//text()').extract()[0]
        item['city'] = city

        selector = response.xpath('//ul[@class="t clearfix"]')[0]
        weather = ''
        for li in selector.xpath('./li'):
            date = li.xpath('./h1//text()').extract()[0]
            cloud = li.xpath('./p[@title]//text()').extract()[0]
            high = li.xpath('./[@class="tem"]//span//text()').extract()[0]
            low = li.xpath('./[@class="tem"]//i//text()').extract()[0]
            wind = li.xpath('./p[@class="win"]//em//span[1]/@title').extract()[0] 
            wind = wind + li.xpath('./p[@class="win"]//i//text()').extract()[0]
            weather = weather + date + ':' + cloud + ',' + hight + r'/' + low + ',' + wind + '\n'
        item[weather] = weather
        return [item]

        pass
