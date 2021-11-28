from dataclasses import dataclass
from domain.weather import Weather


@dataclass
class WeatherForecast:
    weather: Weather() = Weather()
    date: str = ""
