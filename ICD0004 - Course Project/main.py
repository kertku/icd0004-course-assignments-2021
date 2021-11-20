from current_weather_report import CurrentWeatherReport
from forecast_api import ForecastApi
from weather_api import WeatherApi
from weather_report_main_details import *


def ask_city_name():
    return input("Please enter the city name for witch You want weather info for: ")


if __name__ == '__main__':
    city = ask_city_name()
    weather_api = WeatherApi(city)

    current_weather_report_from_api = weather_api.get_current_weather_data()

    weather_report_details = WeatherReportDetails()
    weather_report_details.parse_json_result_to_weather_report_details(current_weather_report_from_api)

    current_weather_report = CurrentWeatherReport()
    current_weather_report.parse_json_result_to_current_weather_report(current_weather_report_from_api)

    forecast_api = ForecastApi(city)
    forecast = forecast_api.forecast_data_to_string()

    print(weather_report_details.convert_weather_report_details_to_string())
    print(current_weather_report.convert_weather_report_to_string())
    print(forecast)
