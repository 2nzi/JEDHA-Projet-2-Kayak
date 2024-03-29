import os
import logging

import scrapy
from scrapy.crawler import CrawlerProcess
import time
import random

places = ['Mont-Saint-Michel', 'St-Malo', 'Bayeux', 'Le-Havre', 'Rouen', 'Paris', 'Amiens', 'Lille', 'Strasbourg', 'Chateau-du-Haut-Koenigsbourg', 'Colmar', 'Eguisheim', 'Besancon', 'Dijon', 'Annecy', 'Grenoble', 'Lyon', 'Gorges-du-Verdon', 'Bormes-les-Mimosas', 'Cassis', 'Marseille', 'Aix-en-Provence', 'Avignon', 'Uzes', 'Nimes', 'Toulouse', 'Montauban', 'Biarritz', 'Bayonne', 'La-Rochelle']
random_city = random.choice(places) 

class BookingSpider(scrapy.Spider):
    
    name = "booking"
    start_urls = ['https://www.booking.com/hotel']
    start_urls = ['https://www.booking.com']

    def parse(self, response):

        return scrapy.FormRequest.from_response(
            response,

            formdata={'ss':f'{random_city}'},
            callback=self.after_search
        )


    def after_search(self, response):
        html_content = response.xpath('//div[@data-testid="property-card"]')
        
        yield_count = response.meta.get('yield_count', 0)

        for card in html_content:  
            
            # if yield_count >= 7:
            #     break
            
            review_score = card.xpath('.//div[@data-testid="review-score"]/div[1]/div[1]/text()').get()
            url = card.xpath('.//a/@href').get()
            title = card.xpath('.//div[@data-testid="title"]/text()').get()
            if float(review_score.replace("Scored", "").strip()) >= 8:
                yield {
                    'name' : title,
                    'url': url,
                    'review_score': review_score.replace("Scored", "").strip(),
                    
                }
                yield_count += 1
                logging.info(str(yield_count))

        yield scrapy.Request(response.url, callback=self.after_search, meta={'yield_count': yield_count})

filename = f"{random_city}.json"





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