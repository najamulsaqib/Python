# Tuple
"""
Tuple is type of List Whoe's values you cannot Change.
"""
tuple = (1, 2, 1)
print(tuple)
# You cannot insert or delete values in tuple
# There are only 2 functions you can perform in Tuple

print("tuple.index(1): ",tuple.index(1)) # It will return index of value

print("tuple.count(1): ",tuple.count(1)) # To find duplicates of data in tuple
# <a.count(x) will tell how many times '2' is present in tuple>

print("Min value is: ", min(tuple)) # To find minimum value from tuple

print("Max value is: ", max(tuple)) # To find Maximum value from tuple

print("Sum of list is: ", sum(tuple)) # To find Sum of tuple

# You can also use tuple inside a tuple
a = (1,2,3)
b = (4,5,6)
c = (a, b) # Saving both tuple in another tuple
print("Saving multiple lists in another list: ", c)