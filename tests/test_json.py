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
EXPECTED_LEVEL = 'tests/fixtures/result_json_level.txt'
EXPECTED_NESTED = 'tests/fixtures/result_nested.txt'
EXPECTED_PLAIN = 'tests/fixtures/result_plain.txt'
EXPECTED_LEVEL_JSON = 'tests/fixtures/result_json.txt'
EXPECTED_JSON = 'tests/fixtures/result_nested_json.txt'
STYLISH = 'stylish'
PLAIN = "plain"
JSON = 'json'


@pytest.mark.parametrize('file1, file2, format_name, expected', [(FILE1_JSON, FILE2_JSON, STYLISH, EXPECTED_LEVEL),
													(FILE1_JSON, FILE2_YAML, STYLISH, EXPECTED_LEVEL),
													(FILE1_JSON, FILE2_YAML, JSON, EXPECTED_LEVEL_JSON),
													(FILE1_NESTED_JSON, FILE2_NESTED_JSON, STYLISH, EXPECTED_NESTED),
													(FILE1_NESTED_JSON, FILE2_NESTED_JSON, PLAIN, EXPECTED_PLAIN),
													(FILE1_NESTED_JSON, FILE2_NESTED_JSON, JSON, EXPECTED_JSON),
													(FILE1_NESTED_YAML, FILE2_NESTED_YAML, STYLISH, EXPECTED_NESTED),
													(FILE1_NESTED_YAML, FILE2_NESTED_YAML, PLAIN, EXPECTED_PLAIN),
													(FILE1_NESTED_YAML, FILE2_NESTED_YAML, JSON, EXPECTED_JSON)])
def test_json(file1, file2, format_name, expected):
	assert generate_diff(file1, file2, format_name) == open(expected).read()
