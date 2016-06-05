import requests
from datetime import datetime
from lxml import html as htmlparser


class FetchedResource:
    def __init__(self, url):
        self.fetched_url = url
        resp = self._fetch(self.fetched_url)
        self.returned_url = resp.url
        self.headers = resp.headers
        self.html = resp.text
        self.encoding = resp.encoding
        self.status_code = resp.status_code
        self.history = resp.history
        self.doc = self._parse(self.html)
        self.fetched_at = datetime.now()


    def _fetch(self, url):
        return requests.get(url)

    def _parse(self, text):
        return htmlparser.fromstring(text)
