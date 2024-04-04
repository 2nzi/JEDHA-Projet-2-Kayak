import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
# from ....config import AllPath
# all_paths = AllPath()
# save_data_path = all_paths.save_data_path
save_data_path = 'C:\\Users\\antoi\\Documents\\Work&Learn\\JEDHA\\M03-DataCollection_Managment\\JEDHA-Projet-2-Kayak\\datas\\'

df = pd.read_json(save_data_path+'hotel_url.json')

class BookingHotelSpider(scrapy.Spider):
    
    start_urls = df['url'].tolist()[:]
    name = "my_booking_hotel"

    def parse(self, response):

        logging.info('url:'+response.url)
        name = response.xpath('//div[@id="hp_hotel_name"]/div/h2/text()').get()
        description = response.xpath('//*[@id="property_description_content"]/div/p/text()').get()
        review_score = response.xpath('//div[@data-testid="review-score-right-component"]/div[1]/text()').get()
        lat_lon = response.css('a#hotel_address::attr(data-atlas-latlng)').get()
                
        url = response.url
        city = df[df['url'] == url]['city'].iloc[0]

        yield {
            'city' : city,
            'lat' : lat_lon.split(',')[0],             
            'lon' : lat_lon.split(',')[1],
            'name' : name,
            'review_score' : review_score,
            'url' : response.url,
            'description': description.replace("\n", "<br>"),
        }





filename = f"hotel.json"

if filename in os.listdir(save_data_path):
        os.remove(save_data_path + filename)

process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        save_data_path + filename: {"format": "json", 'encoding' : 'utf8'},
    }
})

process.crawl(BookingHotelSpider)
process.start()