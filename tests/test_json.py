from gen_diff.engine import generate_diff


def test_json():
	file1 = open('./tests/fixtures/file1.json', 'r')
	file2 = open('./tests/fixtures/file2.json', 'r')
	assert generate_diff(file1, file2) == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'