import json
import urllib.request

API_LINK = json.load(open(".env"))["weather"]

class WeatherReport(object):
    def __init__(self, time, temperature, precipitation, max_temp, min_temp, uv_index):
        self.time = time
        self.temperature = temperature
        self.precipitation = precipitation
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.uv_index = uv_index
    
    def getTime(self):
        return self.time
    
    def getTemperature(self):
        return self.temperature
    
    def getPrecipitation(self):
        return self.precipitation

    def getMaxTemp(self):
        return self.max_temp
    
    def getMinTemp(self):
        return self.min_temp
    
    def getUvIndex(self):
        return self.uv_index
    
def _get_api_json(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
        })
    return json.loads(urllib.request.urlopen(req).read().decode('utf-8'))

def _parse_json(json):
    i = 0
    times = []
    while i < len(json['hourly']['time']):
        times.append(json['hourly']['time'][i].split('T')[1])
        i += 1
    weather = WeatherReport(
        time=times,
        temperature=json['hourly']['temperature_120m'],
        precipitation=json['hourly']['rain'],
        max_temp=json['daily']['temperature_2m_max'],
        min_temp=json['daily']['temperature_2m_min'],
        uv_index=json['daily']['uv_index_max']
    )
    return weather

def getWeather() -> WeatherReport:
    json = _get_api_json(API_LINK)
    return _parse_json(json)