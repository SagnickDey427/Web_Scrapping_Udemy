import scrapy # type: ignore
from my_demo_project_1.items import ApiScraperItem


class PostScraperSpider(scrapy.Spider):
    name = "post_scraper"
    allowed_domains = ["jsonplaceholder.typicode.com"]
    # start_urls = ["https://jsonplaceholder.typicode.com/posts"]

    def start_requests(self): #Sends the initial request to the API
        yield scrapy.Request(
            url='https://jsonplaceholder.typicode.com/posts',
            headers={'User-Agent': 'Mozilla/5.0'},
            callback=self.parse
        )

    def parse(self, response): # Parses the response from the API
        data = response.json()
        for post in data:
            item = ApiScraperItem()
            item['userId'] = post['userId']
            item['id'] = post['id']
            item['title'] = post['title']
            item['body'] = post['body']
            yield item