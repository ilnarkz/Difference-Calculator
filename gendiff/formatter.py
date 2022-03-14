from gendiff.formatters.json import format_to_json
from gendiff.formatters.plain import format_to_plain
from gendiff.formatters.stylish import format_to_stylish


STYLISH = 'stylish'
PLAIN = "plain"
JSON = 'json'


def render(common_dict, format_name):
    if format_name == PLAIN:
        return format_to_plain(common_dict)
    if format_name == JSON:
        return format_to_json(common_dict)
    if not format_name or format_name == STYLISH:
        return format_to_stylish(common_dict)
    raise Exception('Incorrect format')
