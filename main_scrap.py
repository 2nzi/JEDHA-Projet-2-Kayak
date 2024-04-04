#%%

import os
from config import AllPath
all_paths = AllPath()

os.chdir('C:\\Users\\antoi\\Documents\\Work&Learn\\JEDHA\\M03-DataCollection_Managment\\JEDHA-Projet-2-Kayak\\')
print(os.getcwd())

scrapy_url_path = all_paths.scrapy_url_path
scrapy_hotel_path = all_paths.scrapy_hotel_path
project_path = all_paths.scrapy_hotel_path

# scrapy_url_path = 'C:\\Users\\antoi\\Documents\\Work&Learn\\JEDHA\\M03-DataCollection_Managment\\JEDHA-Projet-2-Kayak\\hotel_crawler\\hotel_crawler\\'
# scrapy_hotel_path = 'C:\\Users\\antoi\\Documents\\Work&Learn\\JEDHA\\M03-DataCollection_Managment\\JEDHA-Projet-2-Kayak\\url_crawler\\url_crawler\\'
# project_path = 'C:\\Users\\antoi\\Documents\\Work&Learn\\JEDHA\\M03-DataCollection_Managment\\JEDHA-Projet-2-Kayak\\'


os.chdir(scrapy_url_path)
print(os.getcwd())


os.system("scrapy crawl my_booking_url")



os.chdir(scrapy_hotel_path)
print(os.getcwd())


os.system("scrapy crawl my_booking_hotel")



print('end')


# %%
