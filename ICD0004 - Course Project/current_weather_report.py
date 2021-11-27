import json
from dataclasses import dataclass

from apis.weather_api import WeatherApi
from domain.weather import Weather
from helpers import date_converter


class CurrentWeatherReport:
    def __init__(self, json_input, date="", weather=Weather()):
        self.date = date
        self.weather = weather
        self.json_input = json_input

    def parse_json_result_to_current_weather_report(self):
        try:
            self.date = date_converter.convert_unix_dateformat_to_utc(self.json_input["dt"])
            self.weather.temperature = self.json_input['main']["temp"]
            self.weather.humidity = self.json_input['main']['humidity']
            self.weather.pressure = self.json_input['main']['pressure']
        except KeyError:
            print("Something went wrong! Invalid json format!")
            exit(1)

    def convert_weather_report_to_string(self):
        self.parse_json_result_to_current_weather_report()
        return json.dumps({"currentWeatherReport": {"date": self.date, "weather": self.weather}},
                          default=lambda o: o.__dict__)
