# List
list = [1, 2, 3, 4]
print(list)

print(list[1:3])  # To print Specific values a[Starting index : Ending index + 1]

print(list[0], list[-1])  # To print first and last value only

print(list[::-1])  # To Print list in reverse order

# You can also insert any data-type in list

list.insert(4, "Najam")  # To insert value at specific index
print("list.insert(x): ", list)

list.append("Lalian")  # To insert value at last
print("list.append(x): ", list)

list.pop(4)  # To remove value from specific index
print("list.pop(x): ", list)

list.remove("Lalian")  # To remove specific Value
print("list.remove(x): ", list)

list.extend([5, 6, 7, 8, 9])  # To add multiple values
print("list.extend(x,y,z, ...): ", list)

del list[4:8]  # To delete multiple values a[starting index: ending index + 1]
print("del list[x:y]: ", list)

print("Min value is: ", min(list))  # To find minimum value from list

print("Max value is: ", max(list))  # To find Maximum value from list

print("Sum of list is: ", sum(list))  # To find Sum of List

list.sort()  # To sort list values
print("list.sort(): ", list)

b = list.copy()  # to copy list to another list
print("list.copy(): ", b)

print("list.count(x): ", list.count(2))  # To find duplicates of data in list
# <list.count(x) will tell how many times '2' is present in list>

print("list.index(x): ", list.index(3))  # It will return index of given value

list.reverse()  # It will reverse and save list
print("list.reverse: ", list)

list.clear()  # to clear whole list
print("list.clear(): ", list)

# You can also use List inside a List
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]  # Saving both lists in another list
print("Saving multiple lists in another list: ", c)
