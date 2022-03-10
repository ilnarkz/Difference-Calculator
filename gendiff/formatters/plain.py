import json
from gendiff.engine import REMOVED, ADDED, CHANGED, NESTED


def format_to_plain(dictionary, parent=''):
    result = []
    for key, value_condition in dictionary.items():
        type_ = value_condition.get('type')
        value_ = value_condition.get('value')
        children_ = value_condition.get('children')
        path = parent + '.' + key
        if type_ == REMOVED:
            result.append(f"Property '{path.strip('.')}' was removed")
        elif type_ == ADDED:
            if isinstance(value_, dict):
                result.append(f"Property '{path.strip('.')}' was added with value: [complex value]")
            else:
                result.append(f"Property '{path.strip('.')}' was added with value: {lower(value_)}")
        elif type_ == CHANGED:
            if isinstance(value_.get("old_value"), dict):
                result.append(f"Property '{path.strip('.')}' was updated. From [complex value] to {lower(value_.get('new_value'))}")
            elif isinstance(value_.get("new_value"), dict):
                result.append(f"Property '{path.strip('.')}' was updated. From {lower(value_.get('old_value'))} to [complex value]")
            else:
                result.append(f"Property '{path.strip('.')}' was updated. From {lower(value_.get('old_value'))} to {lower(value_.get('new_value'))}")
        elif type_ == NESTED:
            if isinstance(children_, dict):
                result.append(format_to_plain(children_, path))
    return '\n'.join(result)


def lower(item):
    if isinstance(item, str):
        return f"'{item}'"
    return json.dumps(item)
