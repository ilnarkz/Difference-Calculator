import json
import yaml


def parse(contents_data):
    if contents_data[1] == '.json':
        return json.load(contents_data[0])
    elif contents_data[1] in ['.yaml', '.yml']:
        return yaml.safe_load(contents_data[0])
    else:
        return 'error'
