#%%
import os
from pathlib import Path
from config import *

booking_project_path = r'C:\Users\antoi\Documents\Work&Learn\JEDHA\M03-DataCollection_Managment\JEDHA-Projet-2-Kayak'
os.chdir(booking_project_path)


s_path = scrapy_url_path(Path('config.yaml'))
os.chdir(s_path)

print(os.getcwd())


# os.system("scrapy crawl my_booking_url")
os.chdir(booking_project_path)
print(os.getcwd())

s_path = scrapy_hotel_path(Path('config.yaml'))
os.chdir(s_path)
os.system("scrapy crawl my_booking_hotel")
print('end')
# %%
