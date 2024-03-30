import os
import logging

import scrapy
from scrapy.crawler import CrawlerProcess

import pandas as pd
# df = pd.read_json('./booking/result/hotel_url.json')
df = pd.read_json('hotel_url_first_data.json')

class BookingSpider(scrapy.Spider):
    
    name = "my_booking"
    # start_urls = ['https://www.booking.com/hotel/fr/a-l-ombre-du-mont-st-michel.en-gb.html']
    # start_urls = df['url'].tolist()[:3]
    # start_urls = df['url'].tolist()[100:400]
    start_urls = df['url'].tolist()[:]
    


    def parse(self, response):

        logging.info('url:'+response.url)
        name = response.xpath('//div[@id="hp_hotel_name"]/div/h2/text()').get()
        description = response.xpath('//*[@id="property_description_content"]/div/p/text()').get()
        review_score = response.xpath('//div[@data-testid="review-score-right-component"]/div[1]/text()').get()
        lon_lat = response.css('a#hotel_address::attr(data-atlas-latlng)').get()
                
        url = response.url
        city = df[df['url'] == url]['city'].iloc[0]

        yield {
            'city' : city,
            'lon_lat' : lon_lat,             
            'name' : name,
            'review_score' : review_score,
            'url' : response.url,
            'description': description.replace("\n", ""),
        }





filename = f"hotel.json"
# logging.info('path:' + os.getcwd())

if filename in os.listdir('.'):
        os.remove('' + filename)

process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        '' + filename: {"format": "json", 'encoding' : 'utf8'},
    }
})

process.crawl(BookingSpider)
process.start()