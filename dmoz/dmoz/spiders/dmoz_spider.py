#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
import mysql.connector
import hashlib
import logging
from Gxdb import Gxdb
import Gxinfo
from Gxinfo import Gxinfo
from Gxline import Gxline

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

    # 详情
    def gx_info(self,response):
        uuid = response.meta['uuid']
        log.info('- gx_info md5 %s',uuid)
        div = response.css('div.college_msg')
        lis = div.xpath('.//li')
        brs = div.xpath('.//p/text()')
        v1 = lis[0].xpath('string(.)').extract()[0]
        v2 = lis[1].xpath('string(.)').extract()[0]
        v3 = lis[2].xpath('string(.)').extract()[0]
        v4 = lis[3].xpath('string(.)').extract()[0]
        v5 = brs.extract()[0]
        v6 = brs.extract()[1]
        v7 = brs.extract()[2]
        v8 = brs.extract()[3]
        log.info('%s - %s - %s - %s - %s - %s - %s - %s',v1,v2,v3,v4,v5,v6,v7,v8)
        info = Gxinfo(uuid,v1,v2,v3,v4,v5,v6,v7,v8)
        db = Gxdb()
        db.addInfo(info)


    def gx_line(self,response):
        uuid = response.meta['uuid']
        log.info('- gx_line %s',uuid)
        type = response.css('p.btnFsxBox')
        tname = type.xpath('.//font/text()').extract()[2]
        div = response.xpath('.//div[@id="pointbyarea"]')
        trs = div.xpath('.//tr')
        print '---------'
        for tr in trs:
            tds = tr.xpath('.//td')
            # print '========='
            # print tds
            if len(tds) <= 0:
                continue
            v1 = tds[0].xpath('string(.)').extract()[0]
            v2 = tds[1].xpath('string(.)').extract()[0]
            v3 = tds[2].xpath('string(.)').extract()[0]
            v4 = tds[3].xpath('string(.)').extract()[0]
            v5 = tds[4].xpath('string(.)').extract()[0]
            v6 = tds[5].xpath('string(.)').extract()[0]
            line = Gxline(uuid,v1,v2,v3,v4,v5,v6,tname)
            db = Gxdb()
            db.addLine(line)


    # MD5
    def uuid(self,url):
        hash_md5 = hashlib.md5(url)
        m1 = hash_md5.hexdigest()
        return m1

