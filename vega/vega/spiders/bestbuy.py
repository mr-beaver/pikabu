import scrapy


class QuotesSpider(scrapy.Spider):
    name = "bestbuy"

    def start_requests(self):
        urls = [
            'https://www.bestbuy.com/site/searchpage.jsp?st=rx+vega&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for price in response.css('.list-item'):
            yield {
                'condition': price.css('.list-item').re('data-condition="(.[^"]*)')[0],
                'name': price.css('.list-item').re('data-name="(.[^"]*)')[0],
                'price': price.css('.list-item').re('data-price="(.[^"]*)')[0],
                'model': price.css('[itemprop="model"]::text').extract()[0],
            }

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)