import requests


class ApiCalls:
    def __init__(self, location, uri, api_key):
        self.location = location
        self.uri = uri
        self.api_key = api_key
