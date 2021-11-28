import json

from apis.weather_api import WeatherApi
from current_weather_report import CurrentWeatherReport
from helpers.read_json_file import read_json_from_file
from weather_forcast_report import WeatherForecastReport
from weather_report_main_details import WeatherReportDetails


class FullWeatherReport:

    def __init__(self, city_name=""):
        self.city_name = city_name

    def show_full_weather_report(self):
        weather_api_result = WeatherApi(self.city_name).get_current_weather_data_from_api()
        weather_report_main_details = WeatherReportDetails(
            weather_api_result).convert_weather_report_details_to_string()
        current_weather_report = CurrentWeatherReport(weather_api_result).convert_weather_report_to_string()
        weather_forecast = WeatherForecastReport().three_days_forecast(location=self.city_name)
        return json.dumps(json.loads(weather_report_main_details) | json.loads(current_weather_report) | json.loads(
            weather_forecast), indent=2)

    def read_city_name_from_file(self, path):
        cities_json = read_json_from_file(path)
        self.city_name = cities_json['cities'][0]['name']
        return self.city_name
