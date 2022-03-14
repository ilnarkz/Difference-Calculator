import os


def read_file(path):
    file_path = os.path.abspath(path)
    filename, file_extension = os.path.splitext(file_path)
    content = open(file_path).read()
    return content, file_extension
