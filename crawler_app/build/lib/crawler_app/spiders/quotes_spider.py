from pathlib import Path
from rq import Queue
from redis import Redis
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        # Connect to Redis server
        redis_conn = Redis()

        # Create a queue
        queue = Queue(connection=redis_conn)

        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            # Enqueue the URL to be processed asynchronously
            queue.enqueue(self.parse, url)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")