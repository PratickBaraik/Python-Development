# creating a set
my_set = {1, 2, 3, 4}
print("my_set:", my_set)

print()

# adding element to set
my_set.add(10)
print("my_set after adding an item:", my_set)

# adding duplicate element
my_set.add(4)
print("Updated elements in set:", my_set) # no duplicate element in set 

print()

# removing elements
my_set.remove(4)
print("my_set after removing element:", my_set)

try:
    my_set.remove(4)
    print("my_set after removing same element again:", my_set)
except:
    print("Cannot remove same element twice from a set")

print()

# using discard function for removal of element from set
my_set.discard(4)
print("my_set after removing same element using discard function:", my_set)
# discard function doesn't raise any KeyError if element is not present in the set

# performing union operation on two sets
set_1 = {'a', 'b', 'c', 'd', 'e'}
set_2 = {'d', 'e', 'f', 'g', 'h'}
# using | operator for union
first_union = set_1 | set_2
print("first_union elements:", sorted(first_union))
# using union() function
second_union = set_1.union(set_2)
print("second_union elements:", sorted(second_union))

print()

# performing intersection opertion on two sets
# using & operator for intersection
first_intersection = set_1 & set_2
print("first_intersection elements:", sorted(first_intersection))
# using intersection() function
second_intersection = set_1.intersection(set_2)
print("second_intersection elements:", sorted(second_intersection))

print()

# performing difference operation on two sets
num_set_one = {1, 2, 3, 4}
num_set_two = {3, 4, 5, 6, 7}
num_set_three = {8, 9, 0}
# using - operator for difference
first_difference = num_set_one - num_set_two
print("first_difference element:", sorted(first_difference))
# using difference() function
second_difference = num_set_one.difference(num_set_three)
print("second_difference element:", sorted(second_difference))
third_difference = num_set_three.difference(num_set_one)
print("third_difference element:", sorted(third_difference))

print()

# performing symmetric difference
# TODO

# membership testing on set
# TODO

# iterating over a set
# TODO

# set comprehension
# TODO

# immutable set (frozenset)
# TODO
