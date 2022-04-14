import logging
from requests_html import HTMLSession
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


class ParserLinks:
    links = set()

    def __init__(self, url_origin):
        self.url_origin = url_origin
        self.domain = urlparse(url_origin).netloc

    def get_html(self):
        if self.url_is_valid(self.url_origin):
            session = HTMLSession()
            try:
                response = session.get(self.url_origin)
                return response.html.html
            except Exception as er:
                logging.warning(er)
        return None

    @staticmethod
    def url_is_valid(url):
        tuple_url = urlparse(url)
        return bool(tuple_url.netloc) and bool(tuple_url.scheme)

    def clear_url(self, url):
        link = urljoin(self.url_origin, url)
        tuple_url = urlparse(link)
        return tuple_url.scheme + "://" + tuple_url.netloc + tuple_url.path

    def find_links(self):
        content = self.get_html()
        if content:
            soup = BeautifulSoup(content, "html.parser")
            for link in soup.findAll("a"):
                href = link.get("href")
                if href == "" or href is None:
                    continue
                link = self.clear_url(href)
                if not self.url_is_valid(link):
                    continue
                self.links.add(link)
        return self.links
