from apis.weather_api import WeatherApi
from current_weather_report import CurrentWeatherReport
from weather_forcast_report import WeatherForecastReport
from weather_report_main_details import *


def ask_city_name():
    return input("Please enter the city name for witch You want weather info for: ")


def show_full_weather_report(city_name):
    weather_api_result = WeatherApi(city_name).get_current_weather_data_from_api()
    weather_report_main_details = WeatherReportDetails(weather_api_result).convert_weather_report_details_to_string()
    current_weather_report = CurrentWeatherReport(weather_api_result).convert_weather_report_to_string()
    weather_forecast = WeatherForecastReport().three_days_forecast(location=city_name)
    return json.dumps(json.loads(weather_report_main_details) | json.loads(current_weather_report) | json.loads(
        weather_forecast), indent=2)


if __name__ == '__main__':
    city = ask_city_name()

    print(show_full_weather_report(city))
