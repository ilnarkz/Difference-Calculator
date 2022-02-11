import json
import yaml
import os

from gen_diff.read_file import get_read_file


def lower(item):
    if isinstance(item, str):
        return item
    return json.dumps(item)


def generate_diff(path1, path2):
    file1 = get_read_file(path1)
    file2 = get_read_file(path2)
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


# print(get_read_file('/home/ilnar/python-project-lvl2/tests/fixtures/file1.json'))
# print(get_read_file('/home/ilnar/python-project-lvl2/tests/fixtures/file1.yaml'))
# print(get_read_file('/home/ilnar/python-project-lvl2/tests/fixtures/file2.json'))
# print(get_read_file('/home/ilnar/python-project-lvl2/tests/fixtures/file2.yaml'))
# print(generate_diff('/home/ilnar/python-project-lvl2/tests/fixtures/file1.json', '/home/ilnar/python-project-lvl2/tests/fixtures/file2.yaml'))
