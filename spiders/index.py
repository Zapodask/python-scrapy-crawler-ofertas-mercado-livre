import scrapy


class IndexSpider(scrapy.Spider):
    name = "index"

    start_urls = ["https://www.mercadolivre.com.br/ofertas"]

    def parse(self, response):
        for i in response.xpath('//li[@class="promotion-item"]'):
            title = i.xpath('.//p[@class="promotion-item__title"]/text()').get()
            price = i.xpath('.//span[@class="promotion-item__price"]//text()').getall()
            link = i.xpath("./a/@href").get()

            yield {
                "title": title,
                "price": price,
                "link": link,
            }

        next_page = response.xpath('//a[contains(@title, "Próxima")]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
