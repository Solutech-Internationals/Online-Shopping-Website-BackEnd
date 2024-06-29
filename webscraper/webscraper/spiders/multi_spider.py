import scrapy


class MultiSpider(scrapy.Spider):
    name = "multi_spider"
    start_urls = [
        'https://www.daraz.lk/',
        'https://www.aliexpress.com/',
        # Add more URLs up to 10
    ]

    def parse(self, response):
        page_content = response.xpath("//body//text()").getall()
        page_content = ' '.join(page_content).strip()
        yield {
            'url': response.url,
            'content': page_content
        }
