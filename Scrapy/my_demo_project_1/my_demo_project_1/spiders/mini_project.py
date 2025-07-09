import scrapy # type: ignore
from my_demo_project_1.items import BookScraperItem

class MiniProjectSpider(scrapy.Spider):
    name = "mini_project"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            item = BookScraperItem()
            item['title'] = book.css('h3 a::attr(title)').get()
            item['price'] = book.css('p.price_color::text').get()
            item['rating'] = book.css('p.star-rating::attr(class)').get()
            yield item

        # Follow the next page link, if available
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            # Handle relative URLs correctly
            next_page_url = response.urljoin(next_page)
            yield response.follow(url=next_page_url, callback=self.parse)