import json

from api_caller import ApiCalls


class WeatherApi:
    APPID = '84e4560ea21a19b05777ab2b8db01083'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

    def __init__(self, city):
        self.city = city

    def get_city_name(self):
        return self.city

    def get_current_weather_data(self):
        weather_data_from_api = ApiCalls(self.city, self.BASE_URL, self.APPID)
        return weather_data_from_api.get_data_from_api()

    def weather_data_to_string(self):
        return json.dumps(self.get_current_weather_data(), indent=2)
