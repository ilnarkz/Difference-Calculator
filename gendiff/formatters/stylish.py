import itertools
import json

INDENT = '    '
UNCHANGED = '    '
REMOVED = '  - '
ADDED = '  + '


def convert_stylish(dictionary, depth=0):
    result = []
    depth += 1
    for key, value_condition in dictionary.items():
        type_ = value_condition.get('type')
        value_ = value_condition.get('value')
        children_ = value_condition.get('children')
        indent = INDENT * (depth - 1)
        if type_ == 'removed':
            result.append('{}{}{}: {}'.format(indent, REMOVED, key, lower(value_, depth + 1)))
        elif type_ == 'added':
            result.append('{}{}{}: {}'.format(indent, ADDED, key, lower(value_, depth + 1)))
        elif type_ == 'unchanged':
            result.append('{}{}{}: {}'.format(indent, UNCHANGED, key, lower(value_, depth + 1)))
        elif type_ == 'changed':
            result.append('{}{}{}: {}'.format(indent, REMOVED, key, lower(value_.get('old_value'), depth + 1)))
            result.append('{}{}{}: {}'.format(indent, ADDED, key, lower(value_.get('new_value'), depth + 1)))
        else:
            result.append('{}{}{}: {}'.format(indent, UNCHANGED, key, convert_stylish(children_, depth)))
    output = itertools.chain('{', result, [indent + '}'])
    return '\n'.join(output)


def lower(item, depth):
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        result = []
        indent = INDENT * depth
        end_indent = INDENT * (depth - 1)
        for key, key_value in item.items():
            result.append('{}{}: {}'.format(indent, key, lower(key_value, depth + 1)))
        output = itertools.chain('{', result, [end_indent + '}'])
        return '\n'.join(output)
    return json.dumps(item)
