import pytest
from gen_diff.engine import generate_diff

FILE1_JSON = 'tests/fixtures/file1.json'
FILE2_JSON = 'tests/fixtures/file2.json'
FILE1_YAML = 'tests/fixtures/file1.yaml'
FILE2_YAML = 'tests/fixtures/file2.yaml'
EXPECTED = 'tests/fixtures/result_json.txt'

def read_files(EXPECTED):
	file1 = open(EXPECTED).read()
	return file1


@pytest.mark.parametrize('file1, file2, expected', [(FILE1_JSON, FILE2_JSON, EXPECTED),
													(FILE1_YAML, FILE2_JSON, EXPECTED),
													(FILE1_JSON, FILE2_YAML, EXPECTED),
													(FILE1_YAML, FILE2_YAML, EXPECTED)])
def test_json(file1, file2, expected):
	assert generate_diff(file1, file2) == read_files(expected)