import scrapy
from scrapy import crawler, signals
from scrapy.settings import Settings
from twisted.internet import reactor
import re

process = None
numeric_re = r'\d+'


class CommentCrawler(scrapy.Spider):
    name = 'CommentCrawler_' + __name__

    def parse(self, response):
        print('hello')


class RedditSpider(scrapy.Spider):
    name = __name__

    def __init__(self):
        self.start_urls = ['https://www.reddit.com/r/Python/']
        self.btn_next_selector = '.next-button a'
        self.btn_comment_selector = '.comments'

    def parse(self, response):
        thread_buttons = response.css(self.btn_comment_selector)
        print('---buttons-----')
        for item in thread_buttons:
            button_url = item.xpath('@href').extract()[0]
            button_comments = item.xpath('text()').extract()[0]
            button_comments_count = re.findall(numeric_re, button_comments)
            if len(button_comments_count) > 0:
                button_comments_count = int(button_comments_count.pop())
                if button_comments_count >= 5:
                    self.get_thread_text(button_url)
                    print('---------------------------\n')
        next_button = response.css(self.btn_next_selector).xpath('@href').extract()
        print('---navigation----')
        for item in next_button:
            print(item)

    def get_thread_text(self, thread_url):
        comment_crawler = CommentCrawler()
        comment_crawler.start_urls = [thread_url, ]
        process.crawl(comment_crawler)
        process.start()


process = crawler.CrawlerProcess({
    'USER-AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(RedditSpider)
process.start()
reactor.stop()
