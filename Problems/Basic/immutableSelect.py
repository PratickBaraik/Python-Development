'''
Input: data = [1, 2.0, 'apple', (1, 2), b'hi', 1, 'apple', None, True, (1, 2)]

Output: (6, ['bool', 'bytes', 'float', 'int', 'NoneType', 'str', 'tuple'])
'''

def count_unique_immutables(data):
    immutable_types = (int, float, str, tuple, bytes, frozenset, type(None), bool)
    # Get unique immutable elements
    unique_immutables = {item for item in set(data) if isinstance(item, immutable_types)}
    # Get unique type names
    type_names = {type(item).__name__ for item in unique_immutables}
    return len(unique_immutables), sorted(type_names)

data = [1, 2.0, 'apple', (1, 2), b'hi', 1, 'apple', None, True, (1, 2)]
print(count_unique_immutables(data))