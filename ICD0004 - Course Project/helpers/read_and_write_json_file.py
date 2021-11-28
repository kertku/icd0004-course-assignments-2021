import json
import os
from os.path import abspath


def read_json_from_file(path):
    location = os.path.join(abspath(os.path.dirname(__file__)), '../' + path)
    try:
        with open(location) as f:
            if path.endswith('.json'):
                return json.load(f)
            else:
                exit("Wrong file type! Only JSON format is supported!")
    except FileNotFoundError:
        file_path = os.path.join(abspath(os.path.dirname(__file__)), path)
        exit(f"File {file_path} not found!")


def write_to_json_file(file_name, data):
    location = os.path.join(abspath(os.path.dirname(__file__)), f'../output_files/{file_name}.json')
    with open(location, 'w') as outfile:
        json.dump(data, outfile, indent=4)
        print(f"File {file_name}.json created to output_files folder!")
