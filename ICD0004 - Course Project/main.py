from api_caller import ApiCalls


if __name__ == '__main__':
    city = input("Please enter the city name for witch You want weather info for: ")
    api = ApiCalls(city, 'https://api.openweathermap.org/data/2.5/weather?', '84e4560ea21a19b05777ab2b8db01083')
    print(api.get_data_from_api())
