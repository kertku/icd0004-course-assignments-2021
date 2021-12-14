from full_weather_report import FullWeatherReport
from helpers.read_and_write_json_file import write_to_json_file


def ask_city_name():
    return input("Please enter the city name for witch You want weather info for: ")


def ask_output_file_name():
    return input("Please enter output file name without extension: ")


def ask_file_path():
    return input("Please enter json file path: ")


def return_json_weather_reports():
    file_path = ask_file_path()
    cities = FullWeatherReport.read_city_names_from_file(file_path)
    [print(write_to_json_file(f"{city}_full_weather_report",
                              FullWeatherReport(city).show_full_weather_report())) for city in cities]


if __name__ == '__main__':
    return_json_weather_reports()
