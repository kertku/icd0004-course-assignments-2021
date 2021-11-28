import json
import os
from os.path import abspath


def read_json_from_file(path):
    location = os.path.join(abspath(os.path.dirname(__file__)), '../' + path)
    with open(location) as f:
        if path.endswith('.json'):
            return json.load(f)
        else:
            raise TypeError("Wrong file type! Only JSON format is supported!")
