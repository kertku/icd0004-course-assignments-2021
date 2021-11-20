import requests


class ApiCaller:
    APPID = '84e4560ea21a19b05777ab2b8db01083'

    def __init__(self, location, uri, api_key=APPID, units='metric'):
        self.location = location
        self.uri = uri
        self.api_key = api_key
        self.units = units

    def get_data_from_api(self):
        api_call_parameters = {'q': self.location, 'appid': self.api_key, 'units': self.units}
        try:
            api_request_response = requests.get(self.uri, api_call_parameters)
            return api_request_response.json()
        except requests.ConnectionError as error:
            return error
