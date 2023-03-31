import requests
import csv
from io import StringIO
#API_KEY = "edc6617a-ae5a-4820-8ef9-c0038e709bd9" KOCHUNG'S API KEY

class Site(object):
    def __init__(self, name, county, aqi):
        super().__init__()
        self.site_name = name
        self.county = county
        try:
            self.aqi = int(aqi)
        except:
            self.aqi = 999

class Sort():
    pass

    def __repr__(self):
        return f"監測站點：{self.site_name}，所在縣市：{self.county}，aqi={self.aqi}"

class Taiwan_AQI():
    # API_KEY = "**edc6617a*ae5a*4820*8ef9*c0038e709bd9**" 建立password.py
    @classmethod
    def download_aqi(cls) -> list:

        response=requests.get(f'https://data.epa.gov.tw/api/v2/aqx_p_432?api_key={cls.API_KEY}&sort=ImportDate%20desc&format=CSV')

        if response.ok:
            print(response.text)
            #file = open('./aqi.csv', mode='w', encoding='utf-8')
            #file.write(response.text)
            #file.close()
            file = StringIO(response.text,newline='')
            csvReader = csv.reader(file)
            next(csvReader)
            dataList = []
            for item in csvReader:
                site = Site(item[0],item[1],item[2])
                dataList.append(site)
            return dataList
            
        else:
            raise Exception("下載失敗")
    