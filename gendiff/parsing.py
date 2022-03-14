import json
import yaml


def parse(contents_data):
    if contents_data[1] == '.json':
        return json.loads(contents_data[0])
    elif contents_data[1] in ['.yaml', '.yml']:
        return yaml.load(contents_data[0], Loader=yaml.SafeLoader)
    else:
        raise Exception('Incorrect file extension')
