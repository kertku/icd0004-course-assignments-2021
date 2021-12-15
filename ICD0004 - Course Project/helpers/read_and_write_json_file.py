import json
import os
from os.path import abspath

from helpers.file_operations import log_file_created_status, absolute_file_path


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


def write_to_json_file(file_name, data, output_dir="output_files"):
    if data == 404: return f"{file_name}.json not created. No data for this city!"
    file_path = absolute_file_path(f'{output_dir}/{file_name}.json')
    file_created_message = log_file_created_status(file_name, file_path)
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    return file_created_message
