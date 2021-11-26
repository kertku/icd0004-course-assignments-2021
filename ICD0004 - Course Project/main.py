from apis.forecast_api import ForecastApi
from apis.weather_api import WeatherApi
from current_weather_report import CurrentWeatherReport
from weather_forcast_report import WeatherForecastReport

from weather_report_main_details import *


def ask_city_name():
    return input("Please enter the city name for witch You want weather info for: ")


def show_full_weather_report(city_name):
    weather_api_result = WeatherApi(city_name).get_current_weather_data_from_api()
    weather_report_main_details = WeatherReportDetails()
    weather_report_main_details.parse_json_result_to_weather_report_details(weather_api_result)
    weather_report_main_details_string = weather_report_main_details.convert_weather_report_details_to_string()
    current_weather_report = CurrentWeatherReport()
    current_weather_report.parse_json_result_to_current_weather_report(weather_api_result)
    current_weather_report = current_weather_report.convert_weather_report_to_string()
    weather_forecast = WeatherForecastReport.three_days_forecast(city_name)
    return json.dumps(json.loads(weather_report_main_details_string) | json.loads(current_weather_report) | json.loads(
        weather_forecast), indent=2)


if __name__ == '__main__':
    city = ask_city_name()

    print(ForecastApi(city).json_to_pandas_dataframe())
