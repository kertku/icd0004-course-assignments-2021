import requests


class ApiCalls:
    def __init__(self, location, uri, api_key):
        self.location = location
        self.uri = uri
        self.api_key = api_key

    def get_data_from_api(self):
        api_call_parameters = {'q': self.location, 'appid': self.api_key}
        try:
            api_request = requests.get(self.uri, api_call_parameters)
            return api_request.json(), api_request.status_code
        except requests.ConnectionError as error:
            print(error)
            return error
