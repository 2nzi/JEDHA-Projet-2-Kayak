import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.reactor import install_reactor
import urllib.parse


places = ['Mont-Saint-Michel', 'St-Malo', 'Bayeux', 'Le-Havre', 'Rouen', 'Paris', 'Amiens', 'Lille', 'Strasbourg', 'Chateau-du-Haut-Koenigsbourg', 'Colmar', 'Eguisheim', 'Besancon', 'Dijon', 'Annecy', 'Grenoble', 'Lyon', 'Gorges-du-Verdon', 'Bormes-les-Mimosas', 'Cassis', 'Marseille', 'Aix-en-Provence', 'Avignon', 'Uzes', 'Nimes', 'Toulouse', 'Montauban', 'Biarritz', 'Bayonne', 'La-Rochelle']


class BookingSpider(scrapy.Spider):
    
    # name = "my_booking"

    nb_hotel = 25 
    order = 'review_score_and_price'
    start_urls = []
    for place in places:
        start_urls.append(f'https://www.booking.com/searchresults.html?ss={place}&ac_suggestion_list_length={nb_hotel}&nflt=ht_id%3D204&shw_aparth=0')

    def parse(self, response):
        logging.info('Mon url: ' + response.url)

        html_content = response.xpath('//div[@data-testid="property-card"]')        
        yield_count = response.meta.get('yield_count', 0)

        for card in html_content:  
            
            # if yield_count >=5:
            #     break
            
            url = card.xpath('.//a/@href').get()
            city = response.url.split('ss=')[1].split('&')[0]
            yield {
                'city' : city,
                'url': url.split("?")[0],                
            }

            yield_count += 1
            # logging.info(str(yield_count))
            logging.info(str(yield_count)+city)

        # yield scrapy.Request(response.url, callback=self.after_search, meta={'yield_count': yield_count})

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

process.crawl(BookingSpider)
process.start()