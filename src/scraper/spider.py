# kelas untuk scraping

from typing import Any
from httpx import Client

class Spider(object):
    def __init__(self, query: str) -> None:
        self.base_url: str = "https://www.ebay.com/"
        self.client: Client = Client()
        self.query: str = query

    def get_response(self):
        params: dict[str, str] = {
            "_from": "R40",
            "_trksid": "p2380057.m570.l1313",
            "_nkw": self.query,
            "_sacat": "0",
        }
        headers: dict[str, Any] = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

        url: str = self.base_url + "sch/i.html?"
        response = self.client.get(url=url, params=params, headers=headers)



