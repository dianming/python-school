import scrapy
from scrapy.selector import Selector
import mysql.connector


class DmozSpider(scrapy.Spider):
    name = "dmoz1"
    allowed_domains = ["gotopku.cn"]
    start_urls = [
        "http://college.gaokao.com/schpoint/a1/"
    ]

    def parse(self, response):
        dls = response.xpath('//dl')
        for dl in dls:
            gx_info = dl.xpath('./dt/strong/a/@href')
            uls = dl.xpath('./dd/ul')
            for ul in uls:
                lis = ul.xpath('.//li')
                a_1 = lis[3].xpath('./span/a/@href')
                print '- %s' %(a_1.extract()[0])


        # filename = response.url.split("/")[-1]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # sel=Selector(response=response)
        # table = sel.xpath('//table')
        # trs = response.xpath('//dl')
        # db = mysql.connector.connect(host="localhost", user="root", passwd="123456",database="test")
        # cursor = db.cursor()
        # for tr in trs:
        #     tds = tr.xpath('.//td')
        #     sql = "INSERT INTO gkfs_school(source_student,batch,chinese_score,math_score,other_score) VALUES(%s,%s,%s,%s,%s)"
        #     v1 = tds[0].xpath('./text()').extract()[0]
        #     v2 = tds[1].xpath('./text()').extract()[0]
        #     v3 = tds[2].xpath('./text()').extract()[0]
        #     v4 = tds[3].xpath('./text()').extract()[0]
        #     v5 = tds[4].xpath('./text()').extract()[0]
        #     val = (v1,v2,v3,v4,v5)
        #     cursor.execute(sql,val)
        #     db.commit()
