from gen_diff.engine import get_external_view
from gen_diff.read_file import get_read_file
from gen_diff.stylish import convert


def generate_diff(file_path1, file_path2):
    file1 = get_read_file(file_path1)
    file2 = get_read_file(file_path2)
    common_dict = get_external_view(file1, file2)
    return convert(common_dict)
