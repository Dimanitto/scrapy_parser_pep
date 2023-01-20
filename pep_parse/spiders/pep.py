import re
import scrapy
from pep_parse.items import PepParseItem
from collections import namedtuple


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Метод собирающие ссылки на документы PEP"""
        pages_links = response.css('td a::attr(href)')
        # Т.к в таблице для одного pep две одинаковые ссылки, то шаг +2
        for page_link in pages_links[::2]:
            yield response.follow(page_link.get(), callback=self.parse_pep)

    def parse_pep(self, response):
        cols = ['number', 'name']
        Pep = namedtuple('Pep', cols)
        title = response.xpath(
            '//*[@id="pep-content"]/h1/text()'
        ).get().split(' – ')
        pep_title = Pep(*title)
        status = response.xpath(
            '//dt[contains(., "Status")]/following::dd/abbr/text()'
        ).get()
        data = {
            'number': int(re.findall(r'\d+', pep_title.number)[0]),
            'name': pep_title.name,
            'status': status,
        }
        yield PepParseItem(data)
