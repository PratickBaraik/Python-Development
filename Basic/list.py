#creating a list containing fruits name
fruits = ["apple", "banana", "cherry"]
#printing the original list
print("Original list:", fruits) # output: ['apple', 'banana', 'cherry']
# accessing the first fruit
print("First fruit:", fruits[0]) # output: apple

# modifying the elements
fruits[2] = "papaya"
# printing the modified list
print("Modified List:", fruits) # output: ['apple', 'banana', 'papaya']

# adding a fruit at the end
fruits.append("watermelon")
# printing the list after addition
print("List after addition using append function:", fruits)

# adding at a specific position
fruits.insert(2, "pineapple")
# printing the list after insertion in specific position
print("List after insertion in specific position:", fruits)

# removing a fruit or element from list
# removing by value name
fruits.remove("apple")
# printing list after first type of removal
print("List after removing using value name:", fruits)

# removing by index
del fruits[2]
# printing the newly updated list after removal of item using its index
print("List after removing item using index:", fruits)

# removing the last item
fruits.pop()
# printing the list after removing the last item
print("List after removing the last item:", fruits)

print() # empty print function for jumping to new line

# creating a new list of cars
cars = ["Hyundai", "Suzuki", "Mercedes", "BMW", "Tata"]
# printing the original list of cars
print("Original list of cars:", cars)

# slicing the list - getting first two car names
print("First two cars:", cars[:2])
# slicing the list - getting last two car names
print("Last two cars:", cars[-2:])

# iterating over list
for car in cars:
    print("Car list:", car)

# printing the length of the list
print("Length of the car list:", len(cars))

# list comprehension - creating a list of squares
squares = [x ** 2 for x in range(1, 21)]
# printing the list of squares
print("List of squares:", squares)

print() # for jumping to new line

# practical example - grocery shopping
grocery = ['milk', 'bread', 'tomato sauce', 'cheese', 'sugar']
# printing the original grocery list
print("Original grocery list:", grocery)
# adding an item in the grocery list
grocery.append('soyabeans')
# grocery list after adding soyabeans
print("Grocery list after addition of items:", grocery)
# removing item from list
grocery.remove('tomato sauce')
# printing the list after removal of item
print("Grocery list after removing item:", grocery)
# checking item in the list
if 'soyabeans' in grocery:
    print("Buy soyabeans")

print() # empty print function for jumping to new line
# sorting and reversing of list
# creating a number list
number = [1, 2, 8, 9, 10, 3, 7, 4, 6, 5]
print("Original number list:", number)
# printing the sorted list 
print("Sorted number list:", sorted(number))
# printing the reversed list
print("Reversed number list:", number[::-1])

print() # empty print function for jumping to new line

# real-life problem: unique visitors
visitors = ['Pratick', 'Munna', 'Vicky', 'Munna', 'Vishal', 'Vicky']
unique_visitors = list(set(visitors)) # computing unique list
#printing the unique visitor list
print("Unique visitors:", unique_visitors)

# TODO : Nested list practice