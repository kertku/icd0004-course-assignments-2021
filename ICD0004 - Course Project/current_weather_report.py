import json

import date_converter
from date_converter import convert_unix_dateformat_to_utc


class CurrentWeatherReport:
    def __init__(self, date="", temperature="", humidity="", pressure=""):
        self.date = date
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def parse_json_result_to_current_weather_report(self, json_input):
        try:
            self.date = date_converter.convert_unix_dateformat_to_utc(json_input["dt"])
            self.temperature = json_input['main']["temp"]
            self.humidity = json_input['main']['humidity']
            self.pressure = json_input['main']['pressure']
        except KeyError:
            print("Something went wrong! Invalid json format!")
            exit(1)

    def convert_weather_report_to_string(self):
        return json.dumps(self.__dict__, indent=2)
