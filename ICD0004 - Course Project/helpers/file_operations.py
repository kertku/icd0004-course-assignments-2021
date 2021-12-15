import os
from os.path import abspath


def log_file_created_status(file_name, file_path):
    log_message = f"{file_name}.json in output_files folder already exists! File overridden!" if file_exists(
        file_path) else f"New file: {file_name}.json created to output_files folder!"
    return log_message


def file_exists(file_path):
    return os.path.exists(file_path)


def if_file_exists_then_delete_file(file_path):
    if file_exists(file_path): os.remove(file_path)


def absolute_file_path(file_path):
    return os.path.join(abspath(os.path.dirname(__file__)), f'../{file_path}')
