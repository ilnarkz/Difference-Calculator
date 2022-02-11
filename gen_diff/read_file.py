import json
import os
import yaml


def get_read_file(path):
    file_path = os.path.abspath(path)
    filename, file_extension = os.path.splitext(file_path)
    if file_extension == '.json':
        return json.load(open(file_path))
    else:
        return yaml.safe_load(open(file_path))
