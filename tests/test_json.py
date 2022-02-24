import pytest
from gen_diff.generate_diff import generate_diff


FILE1_JSON = 'tests/fixtures/file1.json'
FILE2_JSON = 'tests/fixtures/file2.json'
FILE1_YAML = 'tests/fixtures/file1.yaml'
FILE2_YAML = 'tests/fixtures/file2.yaml'
FILE1_NESTED_JSON = 'tests/fixtures/file1_nested.json'
FILE2_NESTED_JSON = 'tests/fixtures/file2_nested.json'
FILE1_NESTED_YAML = 'tests/fixtures/file1_nested.yaml'
FILE2_NESTED_YAML = 'tests/fixtures/file2_nested.yaml'
EXPECTED_PLAIN = 'tests/fixtures/result_json.txt'
EXPECTED_NESTED = 'tests/fixtures/result_nested.txt'


def read_files(expected_result):
	file1 = open(expected_result).read()
	return file1


@pytest.mark.parametrize('file1, file2, expected', [(FILE1_JSON, FILE2_JSON, EXPECTED_PLAIN),
													(FILE1_YAML, FILE2_JSON, EXPECTED_PLAIN),
													(FILE1_JSON, FILE2_YAML, EXPECTED_PLAIN),
													(FILE1_YAML, FILE2_YAML, EXPECTED_PLAIN),
													(FILE1_NESTED_JSON, FILE2_NESTED_JSON, EXPECTED_NESTED),
													(FILE1_NESTED_YAML, FILE2_NESTED_JSON, EXPECTED_NESTED),
													(FILE1_NESTED_JSON, FILE2_NESTED_YAML, EXPECTED_NESTED),
													(FILE1_NESTED_YAML, FILE2_NESTED_YAML, EXPECTED_NESTED)])
def test_json(file1, file2, expected):
	assert generate_diff(file1, file2) == read_files(expected)
