from gendiff.engine import render_of_diff
from gendiff.formatter import get_format
from gendiff.parsing import parse
from gendiff.read_file import get_read_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    open_file1 = get_read_file(file_path1)
    open_file2 = get_read_file(file_path2)
    dictionary1 = parse(open_file1)
    dictionary2 = parse(open_file2)
    if dictionary1 == 'error' or dictionary2 == 'error':
        return 'Incorrect file extension'
    common_dict = render_of_diff(dictionary1, dictionary2)
    if get_format(common_dict, format_name) == 'error':
        return 'Incorrect format'
    return get_format(common_dict, format_name)
