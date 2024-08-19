import scrapy


class LaptopNeweggSpider(scrapy.Spider):
    name = "laptop_newegg"
    allowed_domains = ["newegg.com"]
    start_urls = ["https://www.newegg.com/Laptops-Notebooks/SubCategory/ID-32/Page-1"]

    def parse(self, response):
        laptop_links = response.xpath('//div[@class="item-info"]/a//@href').getall()

        for link in laptop_links:
            yield response.follow(link, self.parse_detail)

        next_page = response.xpath('//a[@title="Next"]//@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_detail(self, response):
        price_prime = response.xpath('//div[@class="price-current"]//strong//text()').get()
        price_small = response.xpath('//div[@class="price-current"]//sup//text()').get()

        current_price = 0
        try:
            current_price = price_prime + price_small
        except Exception:
            current_price = 0

        detail = response.xpath('//table[@class="table-horizontal"]//td//text()').getall()

        if len(detail) > 0:
            preprocess_detail = " ".join(detail)

        yield {
            "name": response.xpath('//h1[@class="product-title"]/text()').get(),
            "about": response.xpath(
                '//div[contains(@class, "product-features-list")]//li//text()'
            ).getall(),
            "detail": preprocess_detail,
            "price": current_price,
            "url": response.url,
            "domain": "newegg.com",
        }
