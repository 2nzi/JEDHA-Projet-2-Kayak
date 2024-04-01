import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd

chemin_fichier_csv = "./city.csv"
df = pd.read_csv(chemin_fichier_csv, header=None, names=['city','nan'])
places = df['city'].str.replace(' ', '-').tolist()

class BookingUrlSpider(scrapy.Spider):
    
    name = "my_booking"

    nb_hotel = 25
    order = 'review_score_and_price'
    start_urls = []
    for place in places:
        start_urls.append(f'https://www.booking.com/searchresults.html?ss={place}&ac_suggestion_list_length={nb_hotel}&nflt=ht_id%3D204&shw_aparth=0')

    def parse(self, response):
        # logging.info('Mon url: ' + response.url)
        html_content = response.xpath('//div[@data-testid="property-card"]')        

        for card in html_content:              
            url = card.xpath('.//a/@href').get()
            city = response.url.split('ss=')[1].split('&')[0]
            yield {
                'city' : city,
                'url': url.split("?")[0],                
            }


filename = f"hotel_url.json"

if filename in os.listdir('.'):
        os.remove('' + filename)

process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        '' + filename: {"format": "json", 'encoding' : 'utf8'},
    }
})

process.crawl(BookingUrlSpider)
process.start()