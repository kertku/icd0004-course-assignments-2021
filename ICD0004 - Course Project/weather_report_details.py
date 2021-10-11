import json


class WeatherReportDetails:

    def __init__(self):
        self.coordinates = ""
        self.city = ""
        self.temperature_units = ""

    def parse_json_result_to_weather_report_details(self, json_input):
        json_result = json.loads(json_input)
        self.coordinates = json_result["coordinates"]
        self.city = json_result["city"]

    def convert_weather_report_to_json(self):
        return json.dumps(self.__dict__)
