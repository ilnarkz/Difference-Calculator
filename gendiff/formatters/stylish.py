import itertools
import json
from gendiff.engine import REMOVED, ADDED, CHANGED, UNCHANGED


SPACE_INDENT = '    '
UNCHANGED_INDENT = '    '
REMOVED_INDENT = '  - '
ADDED_INDENT = '  + '


def format_to_stylish(dictionary, depth=0):
    result = []
    depth += 1
    for key, value_condition in dictionary.items():
        type_ = value_condition.get('type')
        value_ = value_condition.get('value')
        children_ = value_condition.get('children')
        indent = SPACE_INDENT * (depth - 1)
        if type_ == REMOVED:
            result.append('{}{}{}: {}'.format(indent, REMOVED_INDENT, key, lower(value_, depth + 1)))
        elif type_ == ADDED:
            result.append('{}{}{}: {}'.format(indent, ADDED_INDENT, key, lower(value_, depth + 1)))
        elif type_ == UNCHANGED:
            result.append('{}{}{}: {}'.format(indent, UNCHANGED_INDENT, key, lower(value_, depth + 1)))
        elif type_ == CHANGED:
            result.append('{}{}{}: {}'.format(indent, REMOVED_INDENT, key, lower(value_.get('old_value'), depth + 1)))
            result.append('{}{}{}: {}'.format(indent, ADDED_INDENT, key, lower(value_.get('new_value'), depth + 1)))
        else:
            result.append('{}{}{}: {}'.format(indent, UNCHANGED_INDENT, key, format_to_stylish(children_, depth)))
    output = itertools.chain('{', result, [indent + '}'])
    return '\n'.join(output)


def lower(item, depth):
    if isinstance(item, str):
        return item
    if isinstance(item, dict):
        result = []
        indent = SPACE_INDENT * depth
        end_indent = SPACE_INDENT * (depth - 1)
        for key, key_value in item.items():
            result.append('{}{}: {}'.format(indent, key, lower(key_value, depth + 1)))
        output = itertools.chain('{', result, [end_indent + '}'])
        return '\n'.join(output)
    return json.dumps(item)
