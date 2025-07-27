# integer (int) - immutable
x = 10
print("x (integer) =", x)
# printing address of the x (int) variable
print("x address =", id(x))
# assiging value of x to y and also printing address to match 
y = x
print("y (x) =", y)
print("y address =", id(y))
# creating a new object
y = x + 1
print("y (x + 1) =", y)
# printing address of y variable
print("y (x + 1) address =", id(y))

print()

# float - immutable
y_float = 30.23
print("y_float =", y_float)
print("y_float address =", id(y_float))

# string - immutable
my_str = "This is a string value"
print("my_str =", my_str)
print("my_str address =", id(my_str))

# tuple - immutable
tuple_t = (1, 2, 3, 4, 5)
print("tuple_t =", tuple_t)
print("tuple_t address =", id(tuple_t))

# frozenset - immutable set
frozenset_f = frozenset([1, 2, 3, 4, 5, 6])
print("frozenset_f =", frozenset_f)
print("frozenset_f address =", id(frozenset_f))

# bytes - immutable sequence of bytes
b_byte = b"one"
print("b_byte =", b_byte)
print("b_byte address =", id(b_byte))

# NoneType - immutable
none_value = None
print("none_value =", none_value)
print("none_value address =", id(none_value))

# boolean - immutable
bool_flag = False
print("bool_flag =", bool_flag)
print("bool_flag address =", id(bool_flag))