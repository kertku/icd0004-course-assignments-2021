import json
from domain.weather import Weather
from helpers import date_converter


class CurrentWeatherReport:
    def __init__(self, date="", weather=Weather()):
        self.date = date
        self.weather = weather

    def parse_json_result_to_current_weather_report(self, json_input):
        try:
            self.date = date_converter.convert_unix_dateformat_to_utc(json_input["dt"])
            self.weather.temperature = json_input['main']["temp"]
            self.weather.humidity = json_input['main']['humidity']
            self.weather.pressure = json_input['main']['pressure']
        except KeyError:
            print("Something went wrong! Invalid json format!")
            exit(1)

    def convert_weather_report_to_string(self):
        return json.dumps({"currentWeatherReport": self.__dict__}, default=lambda o: o.__dict__, indent=4)
