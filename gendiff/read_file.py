import os


def read_file(path):
    file_path = os.path.abspath(path)
    filename, file_extension = os.path.splitext(file_path)
    with open(file_path, 'r') as f:
        content = f.read()
    return content, file_extension
