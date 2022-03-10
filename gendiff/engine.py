ADDED = 'added'
REMOVED = 'removed'
UNCHANGED = 'unchanged'
CHANGED = 'changed'
NESTED = 'nested'


def get_external_view(file1, file2):
    keys = [key for key in file1.keys()]
    for key in file2.keys():
        if key not in keys:
            keys.append(key)
    result = {}
    for item in sorted(keys):
        if item in file1 and item not in file2:
            result[item] = {
                'type': REMOVED,
                'value': file1[item],
                'children': None
            }
        elif item not in file1 and item in file2:
            result[item] = {
                'type': ADDED,
                'value': file2[item],
                'children': None
            }
        elif file1[item] == file2[item]:
            result[item] = {
                'type': UNCHANGED,
                'value': file1[item],
                'children': None
            }
        elif isinstance(file1[item], dict) and isinstance(file2[item], dict):
            result[item] = {
                'type': NESTED,
                'value': None,
                'children': get_external_view(file1[item], file2[item])
            }
        else:
            result[item] = {
                'type': CHANGED,
                'value': {
                    'old_value': file1[item],
                    'new_value': file2[item]
                },
                'children': None
            }
    return result
