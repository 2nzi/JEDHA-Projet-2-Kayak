import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
# from ....config import AllPath
# all_paths = AllPath()
# save_path = all_paths.save_data_path
save_path = "C:\\Users\\antoi\\Documents\\Work&Learn\\JEDHA\\M03-DataCollection_Managment\\JEDHA-Projet-2-Kayak\\datas\\"


filename = "hotel_url.json"
chemin_fichier_csv = save_path  + "./city.csv"
df = pd.read_csv(chemin_fichier_csv, header=None, names=['city','nan'])

places = df['city'].str.replace(' ', '-').tolist()



class BookingUrlSpider(scrapy.Spider):

    name = "my_booking_url"

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


if filename in os.listdir(save_path):
        os.remove(save_path + filename)

process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        save_path + filename: {"format": "json", 'encoding' : 'utf8'},
    }
})

process.crawl(BookingUrlSpider)
process.start()