# list examples
number = [1, 2, 3, 4, 5]
print("original number list:", number)
number.append(6)
print("number list after appending element:", number)
# removing an element
number.remove(4)
print("number list after removing element:", number)
# updating an element
number[3] = 4
print("number list after updating element:", number)
# deleting an element from list using del 
del number[4]
print("number list after deleting last element:", number )