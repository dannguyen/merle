# import requests
from merle.extractor import extract_element_from_doc
from datetime import datetime
from slugify import slugify_url
from urllib.parse import urlparse
from newspaper import fulltext, Article
from newspaper.article import ArticleException
import re

from lxml import html as htmlparser

EXCERPT_WORD_COUNT = 60
WS_RX = re.compile(r'\s+')

class FetchedResource:
    def __init__(self, url):
        self.fetched_url = url
        self.fetched_at = datetime.now()
        # need to better use newspaper egg
        self.article = self._articlize() # this needs to be killed
        self.returned_url = self.article.url

        self.html = self.article.html
        try:
            self.fulltext = re.sub('\s+', ' ', fulltext(self.html)).strip()
        except AttributeError:
            self.fulltext = ""

        # resp = self._fetch(self.fetched_url)
        try:
            self.doc = self.article.doc
        except ArticleException:
            self.doc = htmlparser.fromstring(self.html)

        # self.headers = resp.headers
        # self.encoding = resp.encoding
        # self.status_code = resp.status_code
        # self.history = resp.history

        # elements
        _c = self._extract_element('canonical_url')
        self.canonical_url = _c[0] if _c else self.returned_url

        self.titles = self._extract_element('title')
        self.title = self.titles[0]
        self.descriptions = self._extract_element('description')
        self.description = self.descriptions[0] if self.descriptions else ""
        self.description = WS_RX.sub(' ', self.description).strip()
        # necessary to do an extractor for authors, to present different candidates?
        self.authors = self.article.authors
        self.words = re.split(r' ', self.fulltext)
        self.word_count = len(self.words)
        self.excerpt = ' '.join(self.words if self.word_count < EXCERPT_WORD_COUNT else self.words[:EXCERPT_WORD_COUNT] + ['...'])
        self.published_at = self.article.publish_date.strftime('%Y-%m-%d') if self.article.publish_date else ''
        _url = urlparse(self.returned_url)
        # stuff
        self.url_scheme = _url.scheme
        self.url_domain = re.sub('^www\.', '', _url.netloc)
        self.url_path = _url.path
        self.url_fragment = _url.fragment
        self.url_query_string = _url.query
        self.slug = slugify_url(' '.join([self.title, self.url_domain,
                                self.url_fragment]))



    def _extract_element(self, element_name):
        return list(extract_element_from_doc(element_name, self.doc).values())


    # def _fetch(self, url):
    #     return requests.get(url)

    # def _parse(self):
    #     return htmlparser.fromstring(self.html)

    def _articlize(self):
        # todo, make less redundant
        article = Article(self.fetched_url)
        article.download()
        article.parse()
        return article
