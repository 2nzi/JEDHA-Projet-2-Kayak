from pydantic import BaseModel

class AllPath(BaseModel):
    project_path: str = 'C:\\Users\\antoi\\Documents\\Work&Learn\\JEDHA\\M03-DataCollection_Managment\\JEDHA-Projet-2-Kayak\\'
    save_data_path: str = 'C:\\Users\\antoi\\Documents\\Work&Learn\\JEDHA\\M03-DataCollection_Managment\\JEDHA-Projet-2-Kayak\\datas\\'
    scrapy_hotel_path: str = 'C:\\Users\\antoi\\Documents\\Work&Learn\\JEDHA\\M03-DataCollection_Managment\\JEDHA-Projet-2-Kayak\\hotel_crawler\\hotel_crawler'
    scrapy_url_path: str = 'C:\\Users\\antoi\\Documents\\Work&Learn\\JEDHA\\M03-DataCollection_Managment\\JEDHA-Projet-2-Kayak\\url_crawler\\url_crawler'


# all_paths = AllPath()
# all_paths.project_path
