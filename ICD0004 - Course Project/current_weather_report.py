import json
from domain.current_weather import CurrentWeather
from helpers import date_converter


class CurrentWeatherReport:
    def __init__(self, json_input, date="", current_weather=CurrentWeather()):
        self.date = date
        self.current_weather = current_weather
        self.json_input = json_input

    def parse_json_result_to_current_weather_report(self):
        try:
            self.current_weather.date = date_converter.convert_unix_dateformat_to_utc(self.json_input["dt"])
            self.current_weather.weather.temperature = self.json_input['main']["temp"]
            self.current_weather.weather.humidity = self.json_input['main']['humidity']
            self.current_weather.weather.pressure = self.json_input['main']['pressure']
        except KeyError:
            print("Something went wrong! Invalid json format!")
            exit(1)

    def convert_weather_report_to_string(self):
        self.parse_json_result_to_current_weather_report()
        return json.dumps({"currentWeatherReport": {"date": self.date,
                                                    "weather": self.current_weather}},
                          default=lambda o: o.__dict__)
