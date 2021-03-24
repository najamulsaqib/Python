from functools import *

lst = list(range(0,10))

even = list(filter(lambda a : a%2 == 0, lst))
print(even)

double = list(map(lambda a: a*2, even))
print(double)

add = reduce(lambda a,b : a+b, double)
print(add)