import scrapy
from scrapy import crawler, linkextractors
from time import sleep
from datetime import datetime
import re

process = None
numeric_re = r'\d+'


def add_to_file(contents):
    with open('spider_result.txt', 'a') as f:
        f.write(contents)


class CommentCrawler(scrapy.spiders.Spider):
    name = 'CommentCrawler_' + __name__
    rules = [scrapy.spiders.Rule(linkextractors.LinkExtractor(allow='/'),callback='parse')]

    def parse(self, response):
        add_to_file(CommentCrawler.start_urls)
        add_to_file(response)
        add_to_file('-----------END OF PAGE CRAWL---\n')
        yield scrapy.Item()


class RedditSpider(scrapy.spiders.Spider):
    name = __name__

    def __init__(self):
        self.start_urls = ['https://www.reddit.com/r/Python/']
        self.btn_next_selector = '.next-button a'
        self.btn_comment_selector = '.comments'

    def parse(self, response):
        thread_buttons = response.css(self.btn_comment_selector)
        add_to_file('---buttons-----')
        for item in thread_buttons:
            button_url = item.xpath('@href').extract()[0]
            button_comments = item.xpath('text()').extract()[0]
            button_comments_count = re.findall(numeric_re, button_comments)
            if len(button_comments_count) > 0:
                button_comments_count = int(button_comments_count.pop())
                if button_comments_count >= 5:
                    self.get_thread_text(button_url)
                    add_to_file('---------------------------\n')
                    sleep(2)
        next_button = response.css(self.btn_next_selector).xpath('@href').extract()
        add_to_file('---navigation----')
        for item in next_button:
            add_to_file(item)
        yield scrapy.Item()

    def get_thread_text(self, thread_url):
        CommentCrawler.start_urls = [thread_url]
        process.crawl(CommentCrawler)


process = crawler.CrawlerProcess({
    'USER-AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(RedditSpider)
add_to_file('-----STARTING PROCESS------------\n')
add_to_file(str(datetime.now()))
add_to_file('-----------\n')
process.start()
