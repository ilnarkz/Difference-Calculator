from gendiff.formatters.json import format_to_json
from gendiff.formatters.plain import format_to_plain
from gendiff.formatters.stylish import format_to_stylish


def change_format(common_dict, format_name):
    if format_name == 'plain':
        return format_to_plain(common_dict)
    if format_name == 'json':
        return format_to_json(common_dict)
    if not format_name or format_name == 'stylish':
        return format_to_stylish(common_dict)
    return 'Incorrect format'
