"""
Dictionary is list with its own id
dictionary = {id : value}
"""
dict1 = {1: "Najam", 2: 2.0, 3: 3}
print(dict1)

dict2 = dict1.copy() # To copy dictionary
print(dict2)

print(dict1.get(1)) # To get given id's value

dict2.pop(1) # it will remove given id's value [ in dictionary you have to give id to pop() ]
print(dict2)

# From key can be used to assign different keys one value
# You can pass range function in keys portion
# like dict.fromkeys(range(10), "Null")
d = dict.fromkeys(["Name", "age", "Gender"], "Unknown")
print(d)

print(d.items()) # return items in dictionary

print(d.keys()) # return all keys in dictionary

d.popitem() # remove last added item
print(d)

print(dict1.values()) # return values of dictionary
