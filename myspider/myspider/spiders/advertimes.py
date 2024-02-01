import scrapy


class AdvertimesSpider(scrapy.Spider):
    name = "advertimes"
    allowed_domains = ["www.advertimes.com"]
    start_urls = ["https://www.advertimes.com"]

    def parse(self, response):
        articles = response.xpath('//ul[@class="col-article-list"]/li')
        for article in articles:
            title = article.xpath('.//a/h3/text()').get()
            # content = article.xpath('.//a/div/p/text()').get()
            link = article.xpath(".//a/@href").get()
            update_date = article.xpath('.//a/div[@class="meta-bottom"]//span[@class="update-date"]/text()').get()
            # print(title, link, update_date)
            yield response.follow(url=link, callback=self.parse_page,
                                  meta={'title': title,  'update_date': update_date, 'link': link},
                                  )
            # yield {
            #      'link': link,
            #      'title': title,
            #      'update_date': update_date
            # }
        pagination = response.xpath('//div[@class="page-links"]')
        next_page_url = pagination.xpath('.//a[@class="nextpostslink"]/@href').get()
        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse)
    def parse_page(self, response):
        title = response.request.meta['title']
        link = response.request.meta['link']
        update_date = response.request.meta['update_date']
        articles = response.xpath('//div[@class="entry-txt"]')
        for article in articles:
            # lead = article.xpath('.//div[@class="hp_article_pdlr1rem"]/p/text()').getall()
            paragraph = article.xpath('.//div[@class="hp_article_pdlr1rem"]/p/text()').getall()
            yield {
                'title': title,
                'link': link,
                'update_date': update_date,
                #'lead': lead,
                'paragraph': paragraph
            }
