import json
from dataclasses import dataclass, field
from apis.forecast_api import ForecastApi
from domain.weather import Weather
from domain.weather_forecast import WeatherForecast


@dataclass
class WeatherForecastReport:
    forecastReport: [] = field(default_factory=list)

    def three_days_forecast(self, location):
        weather_forecast_pandas_dataframe = ForecastApi(location).json_to_pandas_dataframe()
        for index, row in weather_forecast_pandas_dataframe.head(3).iterrows():
            self.forecastReport.append(WeatherForecast(date=index, weather=Weather(pressure=int(row['pressure']),
                                                                                   temperature=int(row['temp']),
                                                                                   humidity=int(row['humidity']))))

        return json.dumps(self.__dict__, default=lambda o: o.__dict__, sort_keys=True)
