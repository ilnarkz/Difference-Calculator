import json
import os
import yaml


def parse(file_path):
    filename, file_extension = os.path.splitext(file_path)
    if file_extension == '.json':
        return json.load(open(file_path))
    if file_extension in ['.yaml', '.yml']:
        return yaml.safe_load(open(file_path))
    else:
        return 'Incorrect file extension'
