from gendiff.engine import get_external_view
from gendiff.formatters.json import convert_json
from gendiff.formatters.plain import convert_plain
from gendiff.read_file import get_read_file
from gendiff.formatters.stylish import convert_stylish


def generatediff(file_path1, file_path2, format_name='stylish'):
    file1 = get_read_file(file_path1)
    file2 = get_read_file(file_path2)
    common_dict = get_external_view(file1, file2)
    if format_name == 'plain':
        return convert_plain(common_dict)
    if format_name == 'json':
        return convert_json(common_dict)
    return convert_stylish(common_dict)
