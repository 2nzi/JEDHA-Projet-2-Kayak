import os
import logging

import scrapy
from scrapy.crawler import CrawlerProcess

import scrapy
import scrapy

class BookingSpider(scrapy.Spider):
    
    name = "booking"
    start_urls = ['https://www.booking.com/hotel']
    start_urls = ['https://www.booking.com']

    def parse(self, response):

        return scrapy.FormRequest.from_response(
            response,
            # formdata={':re:':'paris'},
            formdata={'ss':'paris'},
            callback=self.after_search
        )
    
    # def after_search(self, response):
    #     # Handle the response after search
    #     # For example, you can extract data from the search results page
    #     property_cards = response.xpath('//div[@data-testid="property-card"]')

    #     for card in property_cards:
    #         # Yielding the raw HTML content of each property card
    #         yield {
    #             'html_content': card.extract()
    #         }

    # def after_search(self, response):
    #     # Extracting HTML content from response
    #     html_content = response.xpath('//div[@data-testid="property-card"]')

    #     for card in html_content:
    #         # Extracting URL using XPath
    #         url = card.xpath('.//a/@href').get()

    #         # Yielding the URL
    #         yield {
    #             'url': url
    #         }


    def after_search(self, response):
        # Extracting HTML content from response
        html_content = response.xpath('//div[@data-testid="property-card"]')

        for card in html_content:
            # Extracting review score link using XPath
            review_score = card.xpath('.//div[@data-testid="review-score"]/div[1]/div[1]/text()').get()

            # Yielding the review score link
            yield {
                'review_score_link': review_score.replace("Scored", "").strip()
            }

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