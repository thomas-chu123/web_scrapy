import scrapy


class YahooSpider(scrapy.Spider):
    name = "yahoo"
    allowed_domains = ["www.yahoo.com.tw"]
    start_urls = ["https://www.yahoo.com.tw"]

    def parse(self, response):
        print(response.text)
        pass
