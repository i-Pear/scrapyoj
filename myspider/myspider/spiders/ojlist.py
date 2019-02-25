# -*- coding: utf-8 -*-
import scrapy
from myspider.items import ojlistItem
from scrapy.http import Request
from urllib.parse import urljoin


class OjlistSpider(scrapy.Spider):
    name = 'ojlist'
    allowed_domains = ['oj.neu.edu.cn']
    stuid = 20184444
    start_urls = []

    def __init__(self):
        for i in range(1, 11):
            self.start_urls.append('https://oj.neu.edu.cn/status/p/' + str(i) + '?username=' + str(
                self.stuid) + '&pid=&lang=All&result=Accepted')

    def cmp(self, cl):
        return cl.date

    dealtTitle = []

    # dealtPage = []

    def parse(self, response):
        if response.url.startswith("https://oj.neu.edu.cn/status/p"):
            items = []
            # if response.url in self.dealtPage:
            #     return []
            # self.dealtPage.append(response.url)
            # for li in response.xpath("/html/body/div/ul"):
            #     link = urljoin("https://oj.neu.edu.cn", li.xpath('//@href').extract()[-1])
            #     if link not in self.dealtPage:
            #         yield Request(link, callback=self.parse)
            for each in response.xpath("//tr[@class='front-table-row']"):
                item = ojlistItem()
                runid = int(each.xpath("td[1]/text()").extract()[0])
                date = (each.xpath("td[2]/text()").extract()[0]).strip()
                title = each.xpath("td[6]/paper-button/a/text()").extract()[0]
                if title in self.dealtTitle:
                    continue
                self.dealtTitle.append(title)
                similartxt = "0%"
                language = (each.xpath("td[8]/text()").extract()[0]).strip()
                if (language != "C++" and language != "C" and language != "C++11"):
                    continue
                if len(each.xpath("//label[@class='label label-primary']").extract()) == 1:
                    similartxt = each.xpath("//label[@class='label label-primary']").extract()[0].strip()
                # similar = int(similartxt[0:-1])

                # if similar > 95:
                #    continue
                item['runid'] = runid
                item['title'] = title
                item['date'] = date
                item['similar'] = similartxt
                item['language'] = language

                items.append(item)
            return items
        else:
            items = []
            return items
