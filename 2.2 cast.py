# Casting in python <Converting types of variables>
i = 2   # initially it is of int type
print(type(i))

i = str(i)  # str() will convert it into string type
print(type(i))

i = float(i)    # float() will convert it into float type
print(type(i))

i = int(i)  # int() will convert it into int type
print(type(i))

c = complex(i) # Complex function will convert your values in complex form
# You can also insert 2 in parameters complex(a,b) first will be real number and 2nd will be imaginary
print(type(c))

print(id(i)) # will return address of variable
print(type(c)) # Will return type of variable

