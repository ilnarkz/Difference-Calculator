import pytest
from gen_diff.engine import generate_diff

FILE1 = 'tests/fixtures/file1.json'
FILE2 = 'tests/fixtures/file2.json'
EXPECTED = 'tests/fixtures/result_json.txt'

def read_files():
	file1 = open(EXPECTED).read()
	return file1



def test_json():
	assert generate_diff(FILE1, FILE2) == read_files()