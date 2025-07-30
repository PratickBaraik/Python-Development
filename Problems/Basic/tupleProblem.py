# creating a tuple with 5 elements and printing the second element
tuple_5 = ('aplha', 'beta', 'gamma', 'delta', 'epsilon')
print("second element of tuple_5:", tuple_5[1])

# unpacking tuple into three variables
tuple_3 = ('A', 'B', 'C')
a, b, c = tuple_3
print("unpacked values -")
print('a:', a)
print('b:', b)
print('c:', c)

# counting the occurrences of element from tuple
tuple_count = (1, 4, 4, 2, 4)
print("original tuple_count:", tuple_count)
print("count of 4:", tuple_count.count(4))

# using tuple as a key in a dictionary
tuple_key = {
    (1, 2): "first coordinate",
    (2, 3): "second coordinate",
    (3, 4): "third coordinate"
}
# printing dictionary elements with key and value together
for key, value in tuple_key.items():
    print(f"Key: {key}, Value: {value}")

# creating named tuple
from collections import namedtuple
student = namedtuple("Name", ["maths_grade", "science_grade", "hindi_grade", "english_grade"])
Grade = student("A+", "A", "B", "A+")
print("Student maths grade:", Grade.maths_grade)
print("Student science grade:", Grade.science_grade)
print("Student hindi grade:", Grade.hindi_grade)
print("Student english grade:", Grade.english_grade)