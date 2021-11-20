from domain.weather import Weather


class WeatherForecastReport:

    def __init__(self, date, weather=Weather(temperature=0, humidity=0, pressure=0)):
        self.date = date
        self.weather = weather
