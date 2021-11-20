from dataclasses import dataclass


@dataclass
class Weather:
    temperature: int
    humidity: int
    pressure: int
