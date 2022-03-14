import json
import yaml


def parse(data_file, file_extension):
    if file_extension == '.json':
        return json.loads(data_file)
    elif file_extension in ['.yaml', '.yml']:
        return yaml.load(data_file, Loader=yaml.SafeLoader)
    else:
        raise Exception('Incorrect file extension')
