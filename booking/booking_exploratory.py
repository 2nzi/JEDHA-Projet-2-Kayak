import os
import logging

import scrapy
from scrapy.crawler import CrawlerProcess
import time
import random


class BookingSpider(scrapy.Spider):
    
    name = "booking"
    start_urls = ['https://www.booking.com/hotel']
    start_urls = ['https://www.booking.com']

    def parse(self, response):

        return scrapy.FormRequest.from_response(
            response,

            formdata={'ss':'paris'},
            callback=self.after_search
        )


    def after_search(self, response):
        html_content = response.xpath('//div[@data-testid="property-card"]')
        
        yield_count = response.meta.get('yield_count', 0)

        for card in html_content:  
            
            if yield_count >= 13:
                break
            
            review_score = card.xpath('.//div[@data-testid="review-score"]/div[1]/div[1]/text()').get()

            if float(review_score.replace("Scored", "").strip()) > 8.5:
                yield {
                    'url': response.url,
                    'review_score_link': review_score.replace("Scored", "").strip(),
                    'i': yield_count
                }
                yield_count += 1

        yield scrapy.Request(response.url, callback=self.after_search, meta={'yield_count': yield_count})

filename = "booking.json"

if filename in os.listdir('booking/'):
        os.remove('booking/' + filename)

process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'booking/' + filename: {"format": "json", 'encoding' : 'utf8'},
    }
})

process.crawl(BookingSpider)
process.start()