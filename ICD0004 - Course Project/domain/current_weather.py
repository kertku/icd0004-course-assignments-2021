from dataclasses import dataclass
from domain.weather import Weather


@dataclass
class CurrentWeather:
    weather: Weather() = Weather()
    date: str = ""
