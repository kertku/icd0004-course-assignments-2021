import json
from apis.api_caller import ApiCaller


class WeatherApi(ApiCaller):
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

    def __init__(self, location, uri=BASE_URL):
        super().__init__(location, uri)

    def get_city_name(self):
        return self.location

    def get_current_weather_data_from_api(self):
        return self.get_data_from_api()

    def weather_data_to_string(self):
        return json.dumps(self.get_current_weather_data_from_api(), indent=2)
