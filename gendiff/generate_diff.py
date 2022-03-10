from gendiff.engine import get_external_view
from gendiff.formatters.json import format_to_json
from gendiff.formatters.plain import format_to_plain
from gendiff.parsing import parse
from gendiff.read_file import get_full_path
from gendiff.formatters.stylish import format_to_stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    path1 = get_full_path(file_path1)
    path2 = get_full_path(file_path2)
    file1 = parse(path1)
    file2 = parse(path2)
    common_dict = get_external_view(file1, file2)
    if format_name == 'plain':
        return format_to_plain(common_dict)
    if format_name == 'json':
        return format_to_json(common_dict)
    return format_to_stylish(common_dict)
