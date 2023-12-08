from scraper.spider import Spider

class EbaySpider(Spider):
    def __init__(self, query: str) -> None:
        self.headers = ""
        super().__init__(query)