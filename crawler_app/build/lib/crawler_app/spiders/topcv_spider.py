from scrapy import Spider, Request
from crawler_app.items import JobItem

class TopCVCrawlerSpider(Spider):
    name = "topcv"
    allowed_domains = ["topcv.vn"]
    start_urls = [
        "https://www.topcv.vn/viec-lam-it?sort=&skill_id=&skill_id_other=&keyword=&company_field=1&position=&salary=",
    ]

    def parse(self, response):
        # Check for forbidden status
        if response.status == 403:
            self.logger.warning(f"Got 403 Forbidden for {response.url}")
            return
        
        # Extracting job listings
        job_items = response.xpath('//div[@class="job-list-2"]/div')

        for job in job_items:
            item = JobItem()
            
            # Extracting data
            item['title'] = job.xpath('.//h3/a/span/text()').get().strip() if job.xpath('.//h3/a/span/text()').get() else None
            item['company'] = job.xpath('.//a[@class="company"]/text()').get()
            item['location'] = job.xpath('.//label[@class="address"]/text()').get()
            item['link'] = job.xpath('.//h3/a/@href').get()

            # Requesting job details page to extract more information
            job_link = item['link']
            if job_link:
                yield Request(url=job_link, callback=self.parse_job_details, meta={'item': item})
            else:
                yield item

        # Pagination: follow next page link if available
        next_page = response.xpath('//ul[@class="pagination"]/li[@class="active"]/following-sibling::li/a/@href').get()
        if next_page:
            yield Request(url=response.urljoin(next_page), callback=self.parse)

    def parse_job_details(self, response):
        item = response.meta['item']

        # Extracting additional details from job detail page
        item['salary'] = response.xpath('//div[@class="job-detail__info--section-content-value" and preceding-sibling::div[@class="job-detail__info--section-content-title"][text()="Mức lương"]]/text()').get().strip() if response.xpath('//div[@class="job-detail__info--section-content-value" and preceding-sibling::div[@class="job-detail__info--section-content-title"][text()="Mức lương"]]/text()').get() else None
        item['location'] = response.xpath('//div[@class="job-detail__info--section-content-value" and preceding-sibling::div[@class="job-detail__info--section-content-title"][text()="Địa điểm"]]/text()').get().strip() if response.xpath('//div[@class="job-detail__info--section-content-value" and preceding-sibling::div[@class="job-detail__info--section-content-title"][text()="Địa điểm"]]/text()').get() else None
        item['experience'] = response.xpath('//div[@class="job-detail__info--section-content-value" and preceding-sibling::div[@class="job-detail__info--section-content-title"][text()="Kinh nghiệm"]]/text()').get().strip() if response.xpath('//div[@class="job-detail__info--section-content-value" and preceding-sibling::div[@class="job-detail__info--section-content-title"][text()="Kinh nghiệm"]]/text()').get() else None
        item['deadline'] = response.xpath('//div[@class="job-detail__info--deadline"]/text()').get().strip() if response.xpath('//div[@class="job-detail__info--deadline"]/text()').get() else None

        # Extracting job detail section information
        item['description'] = '\n'.join(response.xpath('//h3[text()="Mô tả công việc"]/following-sibling::div[@class="job-description__item--content"]/p/text()').getall()).strip()
        item['requirements'] = '\n'.join(response.xpath('//h3[text()="Yêu cầu ứng viên"]/following-sibling::div[@class="job-description__item--content"]/p/b/text()').getall()).strip()
        item['benefits'] = '\n'.join(response.xpath('//h3[text()="Quyền lợi"]/following-sibling::div[@class="job-description__item--content"]/p/text() | //h3[text()="Quyền lợi"]/following-sibling::div[@class="job-description__item--content"]/p/b/text()').getall()).strip()
        item['how_to_apply'] = response.xpath('//h3[text()="Cách thức ứng tuyển"]/following-sibling::div[@class="job-description__item--content"]/strong/text()').get().strip() if response.xpath('//h3[text()="Cách thức ứng tuyển"]/following-sibling::div[@class="job-description__item--content"]/strong/text()').get() else None

        yield item
