from full_weather_report import FullWeatherReport
from helpers.read_and_write_json_file import write_to_json_file


def ask_city_name():
    return input("Please enter the city name for witch You want weather info for: ")


def ask_output_file_name():
    return input("Please enter output file name without extension: ")


def ask_file_path():
    return input("Please enter json file path: ")


if __name__ == '__main__':
    path = ask_file_path()
    # city = ask_city_name()
    full_weather_report = FullWeatherReport()
    full_weather_report.read_city_name_from_file(path)
    output_file_name = ask_output_file_name()
    write_to_json_file(output_file_name, full_weather_report.show_full_weather_report())
