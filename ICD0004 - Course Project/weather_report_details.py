import json


class WeatherReportDetails:

    def __init__(self):
        self.coordinates = ""
        self.city = ""
        self.temperature_units = "Celsius"

    def get_coordinates(self):
        return self.coordinates

    def get_city_name(self):
        return self.city

    def parse_json_result_to_weather_report_details(self, json_input):
        try:
            self.coordinates = f"{json_input['coord']['lat']},{json_input['coord']['lon']}"
            self.city = json_input["name"]
        except KeyError:
            print("Something went wrong! Invalid json format!")
            exit(1)

    def convert_weather_report_details_to_string(self):
        return json.dumps(self.__dict__, indent=2)

