from dataclasses import dataclass


@dataclass
class Weather:
    temperature: int = 0
    humidity: int = 0
    pressure: int = 0
