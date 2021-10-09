from api_caller import ApiCalls

if __name__ == '__main__':
    api = ApiCalls('Keila', 'https://api.openweathermap.org/data/2.5/weather?', '84e')
    print(api.get_data_from_api())
