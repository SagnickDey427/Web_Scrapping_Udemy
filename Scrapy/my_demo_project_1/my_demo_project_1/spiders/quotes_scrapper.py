import scrapy # type: ignore


class QuotesScrapperSpider(scrapy.Spider):
    name = "quotes_scrapper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        
        #Exploring the response object
        # print("Response :",response)
        # print(" Response Status :",response.status)
        # print(" Response Headers :",response.headers)
        # print("Response content :",response.text[:500])

        #Extracting page title
        # page_title = response.css("title::text").get()
        # print(f"Page Title: {page_title}") 

        # #Extracting quotes, authors and tags
        quotes = response.css("div.quote")
        for quote in quotes:
            quote_text = quote.css("span.text::text").get()
            author = quote.css("small.author::text").get()
            tags = quote.css("div.tags a.tag::text").getall()
            yield {
                "quote": quote_text,
                "author": author,
                "tags": tags
            }
        #Navigate to next page
        relative_url = response.css("li.next a::attr(href)").get()
        nextpage_url = response.urljoin(relative_url)
        if nextpage_url:
            yield response.follow(nextpage_url, callback=self.parse)
