import json
import os


def lower(item):
    if isinstance(item, str):
        return item
    return json.dumps(item)


def generate_diff(path1, path2):
    file1_path = os.path.abspath(path1)
    file2_path = os.path.abspath(path2)
    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))
    keys = [key for key in file1.keys()]
    result = '{\n'
    for key in file2.keys():
        if key not in keys:
            keys.append(key)
    for item in sorted(keys):
        if item in file1 and item in file2:
            if file1[item] == file2[item]:
                result += '    {}: {}\n'.format(item, lower(file1[item]))
            else:
                result += '  - {}: {}\n'.format(item, lower(file1[item]))
                result += '  + {}: {}\n'.format(item, lower(file2[item]))
        elif item in file1 and item not in file2:
            result += '  - {}: {}\n'.format(item, lower(file1[item]))
        else:
            result += '  + {}: {}\n'.format(item, lower(file2[item]))
    result += '}'
    return result
