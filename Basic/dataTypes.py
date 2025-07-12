import pdb
# data types
# integer data type - int: can hold whole numbers (positive or negative, or even zero)
age = 25
print("Age:", age, type(age))
pdb.set_trace()

# float data type - float: can hold decimal numbers
pi = 3.14
print("Pi:", pi, type(pi))
pdb.set_trace()

# string data type - str: can hold sequences of characters
name = "Pratick"
print("Name:", name, type(name))
pdb.set_trace()

# boolean data type - bool: can hold True or False values
is_student = False
print("Student: ", is_student, type(is_student))
pdb.set_trace()

# list data type - list: can hold ordered collections of items, can be of any type, enclosed in square brackets []
fruits = ["apple", "banana", "mango"]
print("Fruits:", fruits, type(fruits))
pdb.set_trace()

# tuple data type - tuple: can hold ordered, immutable collection (cannot be changed), enclosed in parentheses ()
coordinates = (20, 30)
print("Coordinates:", coordinates, type(coordinates))
pdb.set_trace()

# dictionary data type - dict: can hold unordered collection of key-value pairs, enclosed in curly braces {}
person = {"name": "Pratick", "age": 25, "is_student": False}
print("Person:", person, type(person))
pdb.set_trace()

# set data type - set: can hold unordered collection of unique items, enclosed in curly braces {}
numbers = {1, 2, 3, 4, 5}
print("Numbers:", numbers, type(numbers))
pdb.set_trace()
