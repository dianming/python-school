import scrapy


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
        content = response.xpath('tr')
        print "---"
        print content
