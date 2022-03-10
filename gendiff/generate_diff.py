from gendiff.engine import get_external_view
from gendiff.formatter import change_format
from gendiff.parsing import parse
from gendiff.read_file import get_full_path


def generate_diff(file_path1, file_path2, format_name='stylish'):
    path1 = get_full_path(file_path1)
    path2 = get_full_path(file_path2)
    file1 = parse(path1)
    file2 = parse(path2)
    common_dict = get_external_view(file1, file2)
    return change_format(common_dict, format_name)
