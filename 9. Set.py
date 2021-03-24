# Set
"""
Set don't support duplicate values
There is no indexing in setd
"""
setA = {1, 2}
setB = {2, 3, 4}

setA.add(3) # to add value in set
print(setA)

setx = setA.copy() # to hard copy data
print(setx)

setx.clear() # to clear whole set
print(setx)

print(setA.difference(setB)) # to find value of setA which is not in setB

setx = setA.copy()
setx.difference_update(setB) # it will find value of setA which is not in setB and update set A
print(setx)

setx.discard(1) # will remove given element or give error if element didn't exist.
print(setx)

print(setA.isdisjoint(setB)) # check weather set A is disjoint to set b

print(setA.issubset(setB)) # check weather set A is subset of set b

print(setA.issuperset(setB))  # check weather set A is superset of set b

setA.pop() # it will remove any random value mostly first value
print(setA)

setA.remove(2) # it will remove given value
print(setA)

print(setA.symmetric_difference(setB)) # to find symmetric difference from both sets
"""
Difference is used to find difference value of set A to B
like setA = {1,2,3} and set B = {3,2,4}
(difference of A to B)it will return 1 
while symmetric difference will return difference values from both sets
symmetric difference will return 1,4
"""
setA.symmetric_difference_update(setB) # to find symmetric difference from both sets and update setA
print(setA)

#Again assigning values
setA = {1, 2, 3}
setB = {2, 3, 4}

print(setA.union(setB)) # to find union of set A to set B

print(setA.intersection(setB)) # to fing intersection of set A and b

setA.intersection_update(setB) # it find intersection and update setA
print(setA)

