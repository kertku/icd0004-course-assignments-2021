import json


class Helpers:

    @staticmethod
    def load_from_file_to_JSON(file_path):
        with open(file_path) as f:
            return json.load(f)

    @staticmethod
    def JSON_response_to_object(to_class, api_response):
        return to_class(**(json.loads(api_response)))
