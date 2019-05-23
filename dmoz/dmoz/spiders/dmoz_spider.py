#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
import mysql.connector
import hashlib
import logging
import gxdb

log = logging.getLogger('DmozSpider')
log.setLevel(logging.DEBUG)

class DmozSpider(scrapy.Spider):
    name = "dmoz1"
    allowed_domains = ["gotopku.cn"]
    start_urls = [
        "http://college.gaokao.com/schpoint/a1/p1/"
    ]

    # start
    def parse(self, response):
        db = gxdb.Gxdb()
        db.addInfo()

        dls = response.xpath('//dl')
        for dl in dls:
            # 详情
            gx_info = dl.xpath('./dt/strong/a/@href')
            # 分数线
            gx_line = dl.xpath('./dd/ul/li/span/a/@href')

            a_1 = gx_info.extract()
            a_2 = gx_line.extract()
            if len(a_1) > 0:
                url = a_1[0]
                uuid_1 = self.uuid(url)

                log.info('- info_url %s _md5 %s',url,uuid_1)
                yield scrapy.Request(url=url,callback=self.gx_info,meta={'uuid':uuid_1},dont_filter=True)
                if len(a_2) > 0:
                    url = a_2[0]
                    log.info('- line_url %s',url)
                    yield scrapy.Request(url=url,callback=self.gx_line,meta={'uuid':uuid_1},dont_filter=True)
            # uls = dl.xpath('./dd/ul')
            # for ul in uls:
            #     lis = ul.xpath('.//li')
            #     a_1 = lis[3].xpath('./span/a/@href')
            #     log.info('- %s',a_1.extract()[0])

    # 详情
    def gx_info(self,response):
        uuid = response.meta['uuid']
        log.info('- gx_info md5 %s',uuid)
        div = response.css('div.college_msg')
        lis = div.xpath('.//li/text()')
        log.info(lis.extract()[3])

    #
    def gx_line(self,response):
        uuid = response.meta['uuid']
        log.info('- gx_line %s',uuid)
    # MD5
    def uuid(self,url):
        hash_md5 = hashlib.md5(url)
        m1 = hash_md5.hexdigest()
        return m1

