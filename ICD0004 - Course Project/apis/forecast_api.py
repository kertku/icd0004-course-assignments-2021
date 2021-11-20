import json
from apis.api_caller import ApiCaller


class ForecastApi(ApiCaller):
    BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast??'

    def __init__(self, city, uri=BASE_URL):
        super().__init__(city, uri)

    def get_city_name(self):
        return self.location

    def get_forecast_data_from_api(self):
        return self.get_data_from_api()

    def forecast_data_to_string(self):
        return json.dumps(self.get_forecast_data_from_api(), indent=2)
