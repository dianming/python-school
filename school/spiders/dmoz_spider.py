import scrapy
from scrapy.selector import Selector
import mysql.connector


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["gotopku.cn"]
    start_urls = [
        "http://www.gotopku.cn/programa/admitline/7/2008.html"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-1]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # sel=Selector(response=response)
        # table = sel.xpath('//table')
        trs = response.xpath('//tr')
        db = mysql.connector.connect(host="localhost", user="root", passwd="123456",database="test")
        cursor = db.cursor()
        for tr in trs:
            tds = tr.xpath('.//td')
            sql = "INSERT INTO gkfs_school(source_student,batch,chinese_score,math_score,other_score) VALUES(%s,%s,%s,%s,%s)"
            v1 = tds[0].xpath('./text()').extract()[0]
            v2 = tds[1].xpath('./text()').extract()[0]
            v3 = tds[2].xpath('./text()').extract()[0]
            v4 = tds[3].xpath('./text()').extract()[0]
            v5 = tds[4].xpath('./text()').extract()[0]
            val = (v1,v2,v3,v4,v5)
            cursor.execute(sql,val)
            db.commit()
