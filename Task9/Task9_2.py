import requests
import scrapy
from scrapy import crawler


class RedditSpider(scrapy.Spider):
    name = __name__
    __btn_next_selector = '.next-button'
    __btn_comment_selector = '.bylink .comments .may-blank'

    def __init__(self):
        self.start_urls = ['https://www.reddit.com/r/Python/']

    def parse(self, response):
        print(response)
        # with open('response.html','wb') as fs:
        #     fs.write(response.body)
        thread_buttons = response.css(RedditSpider.__btn_comment_selector).extract()
        for item in thread_buttons:
            print(item)
        next_button = response.css(RedditSpider.__btn_next_selector).extract()
        for item in next_button:
            print(item)


process = crawler.CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(RedditSpider)
process.start()
# C_TARGET_URL = 'http://ya.ru'
# response = requests.get(C_TARGET_URL)
# html = response.content
# print(html)
