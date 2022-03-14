from gendiff.engine import make_diff
from gendiff.formatter import render
from gendiff.parsing import parse
from gendiff.read_file import read_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data_of_file1, file_extension1 = read_file(file_path1)
    data_of_file2, file_extension2 = read_file(file_path2)
    dictionary1 = parse(data_of_file1, file_extension1)
    dictionary2 = parse(data_of_file2, file_extension2)
    common_dict = make_diff(dictionary1, dictionary2)
    return render(common_dict, format_name)
