# declaring first tuple 
my_tuple = (1, 20, 300, 4000, 50000)
print("my_tuple:", my_tuple)

# ways of declaring tuple
tuple_1 = (1, 2, 3, 4) # withing parentheses
print("tuple withing parentheses:", tuple_1)

tuple_2 = 1, 2, 3, 4 # without parentheses
print("tuple without parentheses:", tuple_2) # outputs data enclosed in parentheses

tuple_3 = (1,) # tuple with single element
print("tuple with single element:", tuple_3) # single tuple must hava a comma

tuple_4 = 1, # single tuple without parentheses
print("single tuple without parentheses:", tuple_4) # outputs data enclosed in parentheses

# accessing tuple data
access_data = ("aplha", "beta", "gamma", "delta", "epsilon")
print("access_data original data:", access_data)
print("access_data first element:", access_data[0])
print("access_data middle element:", access_data[2])
print("access_data last element:", access_data[-1])

# slicing tuple data
tuple_slice = "one", "two", "three", "four", "five"
print("original data of tuple_slice:", tuple_slice)
print("slicing from 2 to 4:", tuple_slice[2 : 4])
print("slicing from 2 to end:", tuple_slice[2 :])
print("slicing from start to 2:", tuple_slice[: 2])

# unpacking tuple data
tuple_unpack = ("mositurizer", "facial cream", "shaving blade", "trimmer", "charger", "shampoo", "power bank")
print("original data of tuple_unpack:", tuple_unpack)
first, *rest = tuple_unpack
print("unpacked items:", first) # printing the first unpacked item
# printing unpacked data using loop
for items in rest:
    print("unpacked items:", items)

# updating tuple data
org_tuple = (10, 20)
print("org_tuple data:", org_tuple)
# trying to append data to tuple
try:
    org_tuple.append(30)
except AttributeError as e:
    print("Error message while appending to tuple:", e)
# trying to change data in tuple
try:
    org_tuple[0] = 1
except TypeError as e:
    print("Error message while updating tuple:", e)

# using the tuple methods
tuple_m_data = (9, 4, 4, 4, 4, 4, 3, 2, 1)
print("data of tuple_m_data:", tuple_m_data)
print("count of 4 in tuple:", tuple_m_data.count(4))
print("index of 3 in tuple:", tuple_m_data.index(3))

# iterating over tuple data
tuple_iterate = ("uno", "dos", "tres", "cuatro", "cinco")
for x in tuple_iterate:
    print("tuple data:", x)

# nesting tuple
nested_tuple = (("x1", "y1"), ("x2", "y2"), ("x3", "y3"))
print("original nested tuple:", nested_tuple)
print("first row of nested tuple:", nested_tuple[0])
print("first element of first row of nested tuple:", nested_tuple[0][0])

# using tuple as dictionary keys
locations = {
    (10.34, 30.45) : "Location A",
    (23.78, 42.19) : "Location B"
}
print("locations tuple:", locations)
print("first location:", locations[(10.34, 30.45)])
print("second location:", locations[(23.78, 42.19)])
# accessing co-ordinates from tuple using values
for coordinates, location in locations.items():
    print(f"Coordinates: {coordinates}, Location: {location}")

# packing and unpacking with *
a, *b, c = (1, 2, 3, 4, 5)
print("a:", a)
print("b:", b)
print("c:", c)

# advanced: named tuples
from collections import namedtuple
Point = namedtuple("Point", ["A", "B", "C"])
P = Point(1, 2, 3)
print("Named tuple P:", P.A, P.B, P.C)