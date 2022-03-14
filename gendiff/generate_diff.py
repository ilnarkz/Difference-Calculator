from gendiff.engine import render_of_diff
from gendiff.formatter import render
from gendiff.parsing import parse
from gendiff.read_file import read_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    open_file1 = read_file(file_path1)
    open_file2 = read_file(file_path2)
    dictionary1 = parse(open_file1)
    dictionary2 = parse(open_file2)
    common_dict = render_of_diff(dictionary1, dictionary2)
    return render(common_dict, format_name)
