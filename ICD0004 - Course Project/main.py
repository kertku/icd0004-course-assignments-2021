from full_weather_report import FullWeatherReport


def ask_city_name():
    return input("Please enter the city name for witch You want weather info for: ")


if __name__ == '__main__':
    city = ask_city_name()
    print(FullWeatherReport(city).show_full_weather_report())
    FullWeatherReport().read_city_name_from_file('cities.json')