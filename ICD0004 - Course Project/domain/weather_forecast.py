from dataclasses import dataclass, field
from datetime import datetime

from domain import weather
from domain.weather import Weather


@dataclass
class WeatherForecast:
    weather: Weather() = Weather()
    date: str = ""
