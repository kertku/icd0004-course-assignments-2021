import json


class WeatherReportDetails:

    def __init__(self, json_input, coordinates="", city="", temperature_units="Celsius"):
        self.city = city
        self.coordinates = coordinates
        self.temperature_units = temperature_units
        self.json_input = json_input

    def get_coordinates(self):
        return self.coordinates

    def get_city_name(self):
        return self.city

    def parse_json_result_to_weather_report_details(self):
        try:
            self.coordinates = f"{self.json_input['coord']['lat']},{self.json_input['coord']['lon']}"
            self.city = self.json_input["name"]
        except KeyError:
            print("Something went wrong! Invalid json format!")
            exit(1)

    def convert_weather_report_details_to_string(self):
        self.parse_json_result_to_weather_report_details()
        return json.dumps({"weatherReportDetails": {
            "city": self.city,
            "coordinates": self.coordinates,
            "temperature_units": self.temperature_units
        }}, indent=4)
