# creating a list of squares till 30
squares = [x ** 2 for x in range(1, 31)]
print("squares till 30:", squares)
print()

# creating a list of cubes till 30
cubes = [x ** 3 for x in range(1, 31)]
print("cubes till 30:", cubes)
print()

# creating a list of even numbers till 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print("even numbers till 20:", evens)
print()

# creating a list of odd numbers till 20
odds = [x for x in range(1, 21) if x % 2 != 0]
print("odd numbers till 20:", odds)
print()

# converting strings to uppercase
words = ['hello', 'world', 'python', 'coder']
upper_words = [abc.upper() for abc in words]
print("Uppercase words:", upper_words)
lower_words = [lower.lower() for lower in upper_words]
print("Lowercase words:", lower_words)
print()

# nested list comprehension example
matrix_23 = [[1, 2], [3, 4], [5, 6]]
print("original matrix_23:", matrix_23)
flattened_23 = [num for row in matrix_23 for num in row]
print("flattened matrix:", flattened_23)
print("reversed flattened matrix:", flattened_23[::-1])
print("reversed matrix:", matrix_23[::-1])
print()

# flattening 3 * 3 matrix
matrix_33 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("original matrix_33:", matrix_33)
flattened_33 = [num for row in matrix_33 for num in row]
print("flattened 3*3 matrix:", flattened_33)
print()