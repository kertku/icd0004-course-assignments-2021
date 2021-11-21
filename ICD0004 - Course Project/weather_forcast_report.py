import datetime
import json
from datetime import datetime
from apis.forecast_api import ForecastApi
from domain.weather import Weather
from domain.weather_forecast import WeatherForecast
from helpers.date_converter import convert_unix_dateformat_to_utc


class WeatherForecastReport:

    @staticmethod
    def three_days_forecast(city):
        forecast_data = ForecastApi(city).get_forecast_data_from_api()
        forecast_report = [WeatherForecast(weather=Weather()) for i in range(3)]
        for forecast in forecast_data['list']:
            date = datetime.strptime(convert_unix_dateformat_to_utc(forecast['dt']), '%Y-%m-%d')
            for i in range(3):
                if date.day == datetime.now().day + i:
                    forecast_report[i].date = date.strftime('%Y-%m-%d')
                    if forecast_report[i].weather.pressure == 0:
                        forecast_report[i].weather.pressure = forecast['main']['pressure']
                        forecast_report[i].weather.temperature = forecast['main']['temp']
                        forecast_report[i].weather.humidity = forecast['main']['humidity']
                    else:
                        forecast_report[i].weather.pressure = int(
                            (forecast['main']['pressure'] + forecast_report[i].weather.pressure) / 2)
                        forecast_report[i].weather.temperature = int(
                            (forecast['main']['temp'] + forecast_report[i].weather.temperature) / 2)
                        forecast_report[i].weather.humidity = int(
                            (forecast['main']['humidity'] + forecast_report[i].weather.humidity) / 2)
        return json.dumps({"forecastReport": forecast_report}, default=lambda o: o.__dict__, sort_keys=True)
